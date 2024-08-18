from __future__ import annotations

from os.path import dirname, join
from subprocess import run
import collections
import importlib
import inspect
import io
import json
import os
import sys
import traceback
import urllib.parse
from contextlib import contextmanager
from functools import partial, wraps
from itertools import chain
from typing import Callable, Dict, Iterable, List, Set, Tuple, TypeVar
from weakref import ReferenceType

import anyio
import msgpack
import sniffio

from .common import get_window

PARENT_FOLDER = os.path.split(__file__)[0]
SUPPORTED_BROWSER_VERSIONS = {"Chrome": 84, "Edg": 84, "Safari": 14, "Firefox": 79}

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
X = TypeVar("X")


def is_async_context():
    try:
        sniffio.current_async_library()
        return True
    except sniffio.AsyncLibraryNotFoundError:
        return False


def maybe_prefixed_content(prefix, content):
    if content.startswith(prefix):
        return content[len(prefix):]


def import_module(module_path, reload=True):
    try:
        if module_path.endswith(".py"):
            module_path = module_path[:-3]
        result = importlib.import_module(module_path.replace("/", "."))
        if reload:
            importlib.reload(result)
        return result
    except:  # noqa: E722
        lines = traceback.format_exc().splitlines()
    result = importlib.import_module("render.import_error")
    result.ERROR_STACK = lines
    return result


def method_description(method):
    if not isinstance(method, partial):
        try:
            return f"File {repr(inspect.getmodule(method).__file__)}, line {method.__code__.co_firstlineno} {method.__name__}"
        except:  # noqa: E722
            pass
    return repr(method)


@contextmanager
def CatchError(err_back=None):
    try:
        yield
    except anyio.get_cancelled_exc_class():
        raise
    except:  # noqa: E722
        traceback.print_exc()
        exc_type, e, tb = sys.exc_info()
        try:
            if err_back:
                err_back(str(e) or repr(e))
            # removing our entries from the callstack
            lines = traceback.format_exception(exc_type, e, tb)
            call_stack = "".join(chain(line for line in lines))
            window = get_window(throw_if_none=False)
            if window:
                window.display_error_message(call_stack)
        except Exception:
            print("something went wrong in CatchError", e)


def catch_errors_async(func, err_back):
    async def result(args):
        with CatchError(err_back=err_back):
            return await func(*args)

    return result


def extract_client_stack() -> List[str]:
    _exc, _file_name, frame = sys.exc_info()
    render_path, _ = os.path.split(__file__)
    client_frames = list(
        (frame, line)
        for frame, line in traceback.walk_tb(frame.tb_next)
        if not frame.f_code.co_filename.startswith(render_path)
    )
    return (
        traceback.StackSummary.extract(client_frames).format()
        if client_frames
        else traceback.format_exc()
    )


@contextmanager
def modify_attribute(obj, attribute_name, attribute_value):
    previous_value = getattr(obj, attribute_name)
    setattr(obj, attribute_name, attribute_value)
    try:
        yield
    finally:
        setattr(obj, attribute_name, previous_value)


@contextmanager
def scoped_dict_insert(values: Dict, key, value):
    try:
        values[key] = value
        yield key, value
    finally:
        values.pop(key, None)


@contextmanager
def scoped_set_insert(values: Set, value):
    try:
        values.add(value)
        yield
    finally:
        values.discard(value)


async def call_maybe_coroutine(maybe_awaitable, args=(), kwargs={}):
    try:
        result = maybe_awaitable(*args, **kwargs)
        if inspect.isawaitable(result):
            return await result
        return result
    except Exception as e:
        raise Exception(f"{maybe_awaitable} call failed {e}") from e


async def await_coroutine(result, err_back=None, task_status=None):
    with CatchError(err_back=err_back):
        if task_status:
            task_status.started()
        await result


def identity(x):
    return x


def apartial(method, *args):
    async def result(*new_args):
        return await method(*(args + new_args))

    return result


def encode_url(url, args):
    return f"{url}#{json.dumps(args)}"


def decode_url(url):
    module_path, hash_argument = urllib.parse.unquote(url), ""
    if "#" in module_path:
        module_path, hash_argument = module_path.split("#", 1)
    return module_path, hash_argument


def _add_data_namespace(path):
    if path is not None:
        result = path
        if path.startswith("http"):
            return path
        if not path.startswith("/data"):
            if not path.startswith("/"):
                result = "/" + result
            if not (result.startswith("/data") or result.startswith("/static")):
                result = "/data" + result
        return result


def add_data_namespace(path):
    if callable(path):
        from .reactor.observability import CachedEvaluation

        return CachedEvaluation(lambda: _add_data_namespace(path()))
    return _add_data_namespace(path)


def identify_browser(browser: str):
    elements = browser.split(" ")
    result = next((element.split("/") for element in elements if element.startswith("Edg/")), None)
    if result is None:
        result = next(
            (element.split("/") for element in elements if element.startswith("Firefox/")),
            None,
        )
    if result is None:
        result = next(
            (element.split("/") for element in elements if element.startswith("Chrome/")),
            None,
        )
    if result is None:
        result = next(
            (element.split("/") for element in elements if element.startswith("Version/")),
            None,
        )
        if result:
            result = "Safari", result[1]
    if result:
        browser, version = result
        return browser, int(version.split(".")[0])
    else:
        return None, None


class ResponsiveValue:
    def __init__(self, xs, sm=None, md=None, lg=None, xl=None, xxl=None) -> None:
        sm = xs if sm is None else sm
        md = sm if md is None else md
        lg = md if lg is None else lg
        xl = lg if xl is None else xl
        xxl = xl if xxl is None else xxl
        self.values = {"xs": xs, "sm": sm, "md": md, "lg": lg, "xl": xl, "xxl": xxl}

    def __call__(self):
        return self.values[get_window().size().name]


def groupby(values: Iterable[X], key: Callable[[X], K]) -> Iterable[Tuple[K, List[X]]]:
    result = collections.defaultdict(set)
    for value in values:
        result[key(value)].add(value)
    return result.items()


def resolve_weak_refs(handles: Set[ReferenceType[T]]) -> List[T]:
    return [maybe_object for maybe_object in (w() for w in handles) if maybe_object is not None]


def msgpack_dumps_many(*args):
    return b"".join(map(msgpack.dumps, args))


def msgpack_loads_many(message):
    return msgpack.Unpacker(io.BytesIO(message), strict_map_key=False)


@contextmanager
def print_exception(throw=False, callback=None):
    try:
        yield
    # FIMXE: this is failling in a non async context
    # except anyio.get_cancelled_exc_class():
    #     raise
    except:  # noqa: E722
        traceback.print_exc()
        if throw:
            raise
    if callback:
        callback()


def safe_execute_async(method):
    @wraps(method)
    async def result(*args, **kwargs):
        with print_exception():
            return await method(*args, **kwargs)

    return result


def copy_value(value):
    return value.copy() if hasattr(value, "copy") else value


def is_numpy_or_pandas_object(value):
    obj_type = type(value)
    module, type_name = obj_type.__module__, obj_type.__name__
    if module == "numpy" and type_name == "ndarray" or "pandas" in module and type_name == "Series":
        return True
    if module.startswith("pandas") and type_name == "DataFrame":
        return True
    return False


def launch_server():
    run([join(dirname(__file__), "render")] + sys.argv[1:])
