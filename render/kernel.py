from __future__ import annotations

import argparse
import os
import platform
import sys
import urllib.parse
from contextlib import ExitStack, contextmanager
from functools import partial
from itertools import islice
from typing import Dict

import anyio
import msgpack
import websockets
from anyio import create_memory_object_stream
from asyncstdlib.builtins import map as amap
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK

from .common import MessageToClient, SessionEnd, get_window
from .utils import (import_module, msgpack_dumps_many, msgpack_loads_many,
                    scoped_dict_insert, scoped_set_insert)
from .window import Window

stdout, stderr = sys.stdout, sys.stderr


CLIENT_MESSAGE_PREFIX = 0
KERNEL_MESSAGE_PREFIX = 1
MAX_KERNEL_UPDATE_LAG = 100
MAX_CHANNEL_LAG = 100


def import_uv_loop():
    try:
        import uvloop  # noqa: F401

        return True
    except ModuleNotFoundError:
        return False


def try_import_module(module_path):
    try:
        return import_module(module_path)
    except ModuleNotFoundError as e:
        raise Exception(f"Failed to load {module_path}. {e}")


class RedirectOutput:
    def flush(self):
        stdout.flush()

    def write(self, line):
        stdout.write(line)
        if window := get_window(throw_if_none=False):
            window.write_line(line)
        return len(line)


async def connection_closed_ok(connection):
    try:
        async for message in connection:
            yield message
    except (ConnectionClosedError, ConnectionClosedOK):
        pass


class Channel:
    """handles serialization/deserialization, as well as providing a synchronous send API"""

    def __init__(self, channel_manager: ChannelManager, prefix, receive_stream):
        self.prefix = prefix
        self.receive_stream = receive_stream
        self.channel_manager = channel_manager

    async def recv(self):
        return await self.receive_stream.receive()

    async def __aiter__(self):
        while True:
            yield await self.recv()

    async def send(self, message):
        await self.channel_manager.send(self.prefix, message)

    async def send_to_server(self, message):
        await self.channel_manager.connection.send(msgpack_dumps_many(message))

    def send_nowait(self, message):
        self.channel_manager.send_sink.send_nowait((self.prefix, message))


class ChannelManager:
    def __init__(self, connection):
        self.connection = connection
        self.receive_sinks: Dict[int, Channel] = {}
        self.send_sink, self.send_stream = create_memory_object_stream(MAX_CHANNEL_LAG)

    async def forward_messages_to_connection(self):
        try:
            async for prefix, message in self.send_stream:
                await self.send(prefix, message)
        finally:
            await self.connection.close()

    async def dispatch(self, session_id, message):
        if receive_sink := self.receive_sinks.get(session_id):
            await receive_sink.send(message)

    async def send(self, prefix, message):
        try:
            await self.connection.send(prefix + msgpack.dumps(message))
        except (ConnectionClosedError, ConnectionClosedOK):
            pass

    @contextmanager
    def channel(self, channel_id: int):
        receive_sink, receive_stream = anyio.create_memory_object_stream(MAX_CHANNEL_LAG)
        with scoped_dict_insert(self.receive_sinks, channel_id, receive_sink):
            yield Channel(
                channel_manager=self,
                prefix=msgpack_dumps_many(MessageToClient, channel_id),
                receive_stream=receive_stream,
            )


class Kernel:
    def __init__(self, connection, task_group):
        self.connection = connection
        self.task_group = task_group
        self.kernel_id = -1
        self.dev = False
        self.windows: Dict[int, Window] = {}
        self.kernels = {}
        self.kernel_updates_subscribers = set()
        # for some reasons windows spawned python process are subprocess
        self.pid = os.getppid() if platform.system() == "Windows" else os.getpid()
        sys.stderr = sys.stdout = RedirectOutput()
        self.channels = ChannelManager(connection)

    async def manage_session(self, session_id, script_path, browser, start_time, width, height):
        with ExitStack() as stack:
            stack.callback(lambda: print(f"Session {session_id} ended."))
            script_path = urllib.parse.unquote(script_path)
            if "#" in script_path:
                script_path, hash_argument = script_path.split("#", 1)
            else:
                script_path, hash_argument = script_path, ""
            module = try_import_module(script_path)
            connection = stack.enter_context(self.channels.channel(session_id))
            stack.callback(
                partial(
                    self.task_group.start_soon,
                    self.connection.send,
                    msgpack_dumps_many(SessionEnd, session_id),
                )
            )
            async with anyio.create_task_group() as task_group:
                window = Window(
                    self,
                    task_group,
                    session_id,
                    connection,
                    script_path,
                    hash_argument,
                    width,
                    height,
                    getattr(module, "TITLE", script_path),
                )
                stack.enter_context(scoped_dict_insert(self.windows, session_id, window))
                window.send_nowait(
                    "session",
                    (
                        session_id,
                        self.kernel_id,
                        self.pid,
                        start_time,
                        self.dev,
                        script_path,
                    ),
                )
                await window.start_app(update_client_history=not script_path, module=module)

    async def manage_connection(self, task_status):
        await self.connection.send(msgpack.dumps(self.pid))
        task_status.started()
        async for message_chunks in amap(msgpack_loads_many, connection_closed_ok(self.connection)):
            prefix = next(message_chunks)
            if prefix == CLIENT_MESSAGE_PREFIX:
                session_id, message = message_chunks
                await self.channels.dispatch(session_id, message)
            elif prefix == KERNEL_MESSAGE_PREFIX:
                code, message = islice(message_chunks, 2)
                if code == "start session":
                    (
                        session_id,
                        session,
                        browser,
                        start_time,
                        width,
                        height,
                    ) = message
                    session = session[4:] if session.startswith("app/") else session
                    self.task_group.start_soon(
                        self.manage_session,
                        session_id,
                        session,
                        browser,
                        start_time,
                        width,
                        height,
                    )
                elif code == "terminate session":
                    session_id = message
                    if maybe_window := self.windows.pop(session_id, None):
                        maybe_window.stop()
                elif code == "kernel update":
                    await self.kernel_update(message, next(message_chunks))
                elif code == "kernel settings":
                    (
                        current_path,
                        self.kernel_id,
                        self.dev,
                    ) = message
                    os.chdir(current_path)
                else:
                    raise Exception(f"unexpected prefix {code} {message}")
            else:
                raise Exception(f"unexpected prefix {prefix}")

    async def kernel_update(self, code, update):
        for subscriber in self.kernel_updates_subscribers:
            await subscriber.send((code, update))
        if code == "kernels":
            self.kernels = dict(update)
        elif code == "new kernel":
            kernel_id, pid, start_time = update
            self.kernels[kernel_id] = pid, start_time, {}
        elif code == "assigned session":
            kernel_id, session_id, app = update
            self.kernels[kernel_id][2][session_id] = app
        elif code == "session end":
            kernel_id, session_id = update
            self.kernels[kernel_id][2].pop(session_id)
        elif code == "kernel ended":
            self.kernels.pop(update, None)

    @contextmanager
    def subscribe_to_kernel_updates(self):
        update_sink, update_stream = anyio.create_memory_object_stream(MAX_KERNEL_UPDATE_LAG)
        with scoped_set_insert(self.kernel_updates_subscribers, update_sink):
            yield update_stream


async def main_async(webserver_port):
    async with websockets.connect(
        f"ws://localhost:{webserver_port}/ws_kernels",
    ) as connection:
        async with anyio.create_task_group() as task_group:
            kernel = Kernel(connection, task_group)
            task_group.start_soon(kernel.channels.forward_messages_to_connection)
            await task_group.start(kernel.manage_connection)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, help="webserver port", default=8080)
    args = parser.parse_args()
    anyio.run(
        main_async,
        args.port,
        backend="asyncio",
        backend_options={"use_uvloop": import_uv_loop()},
    )
