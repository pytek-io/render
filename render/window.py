import asyncio
import datetime
import enum
import inspect
import math
import reprlib
import sys
import traceback
import urllib
import weakref
from collections import defaultdict
from itertools import chain, count
from typing import Callable, Coroutine, Dict, Iterable, Set

import anyio

from .async_objects import AsyncCachedEvaluation, AsyncGenerator
from .common import CURRENT_CONTROLLER, CURRENT_WINDOW, SubscribeToKernelUpdates
from .components import (
    Callback,
    Component,
    InputComponent,
    JSMethod,
    JSPartiallyAppliedCall,
    Props,
    js,
)
from .controller import Controller
from .mapping import Mapping
from .observability import AutoRun, CachedEvaluation, ObservableValue
from .props import DEFAULT_ARGS_NO_CHILDREN_NAMES
from .utils import (
    CatchError,
    add_data_namespace,
    await_coroutine,
    call_maybe_coroutine,
    catch_errors_async,
    extract_client_stack,
    identity,
    is_async_context,
    method_description,
)

POD_TYPE = str, float, int, bool, type(None)
DEFAULT_ARGS_NAMES = DEFAULT_ARGS_NO_CHILDREN_NAMES

LINKS_REGISTER = defaultdict(set)
RGB_WHITE = 255, 255, 255
DEFAULT_BODY_STYLE = {"backgroundColor": f"rgb{RGB_WHITE}", "margin": 0}
js_free_method_call = "js free method call"


class MountStatus:
    mounting = "mounting"
    unmounted = "unmounted"
    mounted = "mounted"


class WindowSize(enum.IntEnum):
    xxl = 1600
    xl = 1200
    lg = 992
    md = 768
    sm = 576
    xs = 0

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


def media_size(width):
    if width >= 1600:
        return WindowSize.xxl
    if width >= 1200:
        return WindowSize.xl
    if width >= 992:
        return WindowSize.lg
    if width >= 768:
        return WindowSize.md
    if width >= 576:
        return WindowSize.sm
    return WindowSize.xs


def create_link_definition(href, cross_origin):
    return (
        ("rel", "stylesheet"),
        ("type", "text/css"),
        ("href", add_data_namespace(href)),
        ("cross_origin", cross_origin),
    )


def register_css_for_module(module, href, cross_origin=None):
    global LINKS_REGISTER
    LINKS_REGISTER[module].add(create_link_definition(href, cross_origin))


def is_pod_or_component(value):
    return isinstance(value, (str, bool, int, float, Component, js)) or value is None


def check_children_value(component, children_values):
    wrong_child_value = next(
        (child_value for child_value in children_values if not is_pod_or_component(child_value)),
        None,
    )
    if wrong_child_value is not None:
        raise Exception(
            f"{component} has unsupported child type {type(wrong_child_value)} {reprlib.repr(children_values)}."
        )


def deserialize(value):
    data_type, data_value = value
    if data_type == "list":
        return [deserialize(element) for element in data_value]
    if data_type == "datetime":
        return datetime.fromtimestamp(data_value / 1000)
    if data_type == "dict":
        return {key: deserialize(value) for key, value in data_value}
    assert data_type == "value"
    return data_value


async def delayed_callback(callbacks_sink, delay, callback, args):
    await anyio.sleep(delay)
    await callbacks_sink.send((callback, args))


def is_callable_but_not_input_component(arg):
    return callable(arg) and not isinstance(arg, InputComponent)


def is_pod_or_input_component(arg):
    return not callable(arg) or isinstance(arg, InputComponent)


def call_if_not_input_component(arg):
    while is_callable_but_not_input_component(arg):
        arg = arg()
    return arg


def wrap_result_in_list_if_needed(method):
    def result():
        r = method()
        if not isinstance(r, (tuple, list)):
            return [r]
        return r

    return result


def cache_children(children, controller):
    """'Will return a "cached" and flatten version of the children data structure (using a depth first traversal)"""
    counter = count()

    def _cache_children(children):
        if isinstance(
            children,
            (
                Mapping,
                AsyncGenerator,
                AsyncCachedEvaluation,
                CachedEvaluation,
                InputComponent,
            ),
        ):
            yield children
        elif inspect.isasyncgenfunction(children):
            yield AsyncGenerator(children)
        elif inspect.iscoroutinefunction(children):
            yield AsyncCachedEvaluation(children)
        elif callable(children):
            evaluation = CachedEvaluation(
                children,
                key=f"cached_evaluation_{next(counter)}",
                controller=controller,
            )
            value = evaluation()
            yield evaluation if evaluation.has_dependencies else value
        elif isinstance(children, Iterable) and not isinstance(children, str):
            for child in children:
                yield from _cache_children(child)
        elif children is not None:
            yield children

    return _cache_children(children)


def evaluate_child(component: Component):
    def _evaluate_children(children):
        if isinstance(children, Iterable) and not isinstance(children, str):
            for child in children:
                yield from _evaluate_children(child)
        elif isinstance(
            children,
            (
                Mapping,
                AsyncGenerator,
                AsyncCachedEvaluation,
                CachedEvaluation,
                ObservableValue,
            ),
        ):
            yield from _evaluate_children(children())
        else:
            if isinstance(children, Component) and children.key is None:
                children.key = str(component.children_counter)
                component.children_counter += 1
            yield children

    return _evaluate_children(component._cached_children)


class Window:
    def __init__(
        self,
        kernel,
        task_group,
        session_id,
        connection,
        script_path,
        hash_argument,
        width,
        height,
        title,
    ):
        if is_async_context():
            # creating this first thing before we send anything
            self.outputs_ready = anyio.Event()
            self.pending_outputs = []
        self.kernel = kernel
        self.script_path = script_path
        self.title = title
        self.hash_argument = hash_argument
        self.weak_ref = weakref.ref(self)
        CURRENT_WINDOW.set(self.weak_ref)
        CURRENT_CONTROLLER.set(Controller())
        self.task_group = task_group
        self.session_id = session_id
        self._connection = connection
        self.kwargs = {}
        self.root_components = {}
        self.components = weakref.WeakValueDictionary()
        self.callbacks = weakref.WeakValueDictionary()
        self.callbacks_hard_refs = set()
        self.callback_counter = count()
        self.components_counter = count()
        self.pending_results_counter = count()
        self.stored_object_id = count()
        self.message_id = count()
        self.stale_components = set()
        self.deleted_components = []
        self.delayed_callbacks = []
        self.pending_results: Dict[int, asyncio.Future] = {}
        self.loaded_modules: Set[str] = set(["html", "core"])
        self.loaded_links = set()
        self.pending_modules = {}
        self.js_methods = {}
        self.notification_hook = None
        self.log_file = None  # FIXME: remove?
        self.hash = ObservableValue(hash_argument, key="hash_argument")
        self.hash.set, self.hash_set = self.update_hash, self.hash.set
        self.width = ObservableValue(width, key="width")
        self.height = ObservableValue(height, key="height")
        self.size = ObservableValue(WindowSize.lg, key="size")
        self.hard_references = set()
        self.events_callbacks = {}
        self.user_data = {}
        self.document = Document(self)
        w = self.weak_ref
        if is_async_context():
            (
                self.callback_sink,
                self.callback_stream,
            ) = anyio.create_memory_object_stream()
            (
                self.client_message_sink,
                self.client_connection,
            ) = anyio.create_memory_object_stream()
            (
                self.reset_client_thread_sink,
                self.reset_client_thread_stream,
            ) = anyio.create_memory_object_stream()
            (
                self.stale_components_event_sink,
                self.stale_components_event_stream,
            ) = anyio.create_memory_object_stream(math.inf)
            self.hash_updater = AutoRun(lambda: w().update_hash(w().hash()))
        self.update_title(title)

    def __str__(self) -> str:
        return f"<SessionManager:{self.session_id}>"

    def write_line(self, line):
        self.pending_outputs.append(line)
        self.outputs_ready.set()

    async def write_outputs(self):
        try:
            continue_writing = True
            while continue_writing:
                try:
                    await self.outputs_ready.wait()
                    self.outputs_ready = anyio.Event()
                    await anyio.sleep(0.1)  # buffering
                except anyio.get_cancelled_exc_class():
                    continue_writing = False
                finally:
                    if self.pending_outputs:
                        self.pending_outputs, pending_outputs = [], self.pending_outputs
                        self.send_nowait("python", pending_outputs)
                        if self.log_file:
                            self.log_file.writelines(self.pending_outputs)
                            self.log_file.flush()
        finally:
            if self.log_file:
                self.log_file.close()

    def send_nowait(self, code, payload):
        try:
            self._connection.send_nowait((next(self.message_id), (code, payload)))
        except:  # noqa: E722
            print(code, payload)
            traceback.print_exc()

    def set_notification_hook(self, hook):
        self.notification_hook = hook

    def create_return_promise_result(self, method, promise_id):
        async def result(*args):
            try:
                result, success = await call_maybe_coroutine(method, args), True
            except:  # noqa: E722
                result, success = traceback.format_exc(-1), False
            self.send_nowait("promise_result", (promise_id, success, result))

        return result

    async def schedule_callback_execution(self, method, args):
        await self.callback_sink.send((method, args))

    def start_soon(self, func: Callable[..., Coroutine], *args, name=None) -> None:
        if self.task_group.cancel_scope.cancel_called:
            print(f"Error task group already terminated {self.task_group}, {self}")
        self.task_group.start_soon(
            catch_errors_async(func, self.display_error_message), args, name=name
        )

    def update_browser_details(self, data):
        for observable, method, new_value in zip(
            [self.width, self.height, self.size],
            [identity, identity, media_size],
            ["width", "height", "width"],
        ):
            new_value = method(data[new_value])
            if observable.value != new_value:
                observable.set(new_value)
        self.browser_details = data

    async def connection_loop(self):
        async for code, data in self._connection:
            if code == "event":
                callback_description, callback_id, promise_id, value = data
                method = self.callbacks.get(callback_id, None)
                if method:
                    if promise_id:
                        method = self.create_return_promise_result(method, promise_id)
                    await self.schedule_callback_execution(method, deserialize(value))
                else:
                    message = (
                        f"Callback {(callback_description + ' ') if callback_description else ''}"
                        f"not found. It might have been GC'ed, in that case you should take a hard reference on it."
                    )
                    self.display_error_message(message)
            elif code == "componentDidMount":
                component_id = data
                if component := self.components.get(component_id, None):
                    if component.mount_status == "unmounted":
                        self.record_stale_component(component)
                    component.mount_status = "mounted"
                    on_didmount = component.on_didmount
                    if on_didmount:
                        await self.schedule_callback_execution(on_didmount, ())
            elif code == "componentWillUnmount":
                component = self.components.get(data, None)
                if component:
                    component.mount_status = "unmounted"
                    on_unmount = component.on_unmount
                    if on_unmount:
                        await self.schedule_callback_execution(on_unmount, ())
                    self.root_components.pop(data, None)
            elif code == "remote call outcome":
                result_id, success, result = data
                self.pending_results.pop(result_id).set_result((success, deserialize(result)))
            elif code == "message_from_client":
                await self.client_message_sink.send(data)
            elif code == "module loaded":
                self.loaded_modules.add(data)
                m = self.pending_modules.pop(data, None)
                if m:
                    m.set()
            elif code == "remote call error":
                print("remote call error", data)
                # ref_id, method_name, error = data
                # logging.error(f"remote method call failed object nb: {ref_id}, method: {'.'.join(method_name)}, {error}")
            elif code == "ping":
                self.send_nowait("pong", None)
            elif code == "hash":
                if data:
                    data = urllib.parse.unquote(data)
                    if self.hash.eval() != data:
                        self.hash_set(data)
            elif code == "browser_details":
                self.update_browser_details(data)
            elif code == "event fired":
                event_name, result = data
                self.events_callbacks[event_name](result)
            else:
                print(f"unknown code {code} received", code, data)

    async def wait_for_modules_to_load(self):
        [(await event.wait()) for event in list(self.pending_modules.values())]

    async def update_components(self):
        counter = count()
        async for _ in self.stale_components_event_stream:
            with CatchError():
                updates = []
                if stale_components := [w() for w in self.stale_components if w()]:
                    for component in sorted(
                        stale_components,
                        key=lambda c: c._nb if c._nb is not None else sys.maxint,
                    ):
                        if component.is_stale and (data := self._serialize(None, component)):
                            updates.append(data)
                            component.is_stale = False
                    await self.wait_for_modules_to_load()
                    if updates:
                        self.send_nowait("update", [next(counter), updates])

    def call_js_method(self, js_method, args=()):
        if not isinstance(js_method, str):
            js_method, args = self.serialize_js_method(js_method)
        self.send_nowait(
            js_free_method_call,
            self._serialize(None, [js_method, args]),
        )

    def register_js_method(self, name, args, definition):
        with CatchError():
            self.send_nowait("method_def", (name, args, definition))

    def display_error_message(self, message):
        self.send_nowait("error", message)

    async def execution_loop(self):
        async for callback, args in self.callback_stream:
            with CatchError():
                try:
                    maybe_awaitable = callback(*args)
                except:  # noqa: E722
                    print(method_description(callback))
                    raise
                if inspect.isawaitable(maybe_awaitable):
                    await self.task_group.start(
                        await_coroutine, maybe_awaitable, self.display_error_message
                    )
            # rmk: we might want to invoke (asynchronously) the gc from time to time
            if self.deleted_components:
                for component_nb in self.deleted_components:
                    self.send_nowait("delete", component_nb)
                self.deleted_components.clear()
            if self.delayed_callbacks:
                delayed_callbacks, self.delayed_callbacks = (self.delayed_callbacks, [])
                for delay, callback, args in delayed_callbacks:
                    self.start_soon(
                        delayed_callback,
                        self.callback_sink,
                        delay,
                        callback,
                        args,
                        name="delayed_callback",
                    )

    def create_pending_result(self):
        result_id, remote_call_outcome = (
            next(self.pending_results_counter),
            asyncio.Future(),
        )
        self.pending_results[result_id] = remote_call_outcome
        return result_id, remote_call_outcome

    def serialize_children(self, component: Component):
        if component._cached_children is None:
            component._cached_children = list(
                cache_children(getattr(component, "children", []), component.controller)
            )
        children_value = list(evaluate_child(component))
        check_children_value(component, children_value)
        return [self._serialize(component, child) for child in children_value]

    def serialize_js_method(self, value):
        js_method, arguments, modules = (
            (value.js_method, value.arguments, value.js_method.modules)
            if isinstance(value, JSPartiallyAppliedCall)
            else (value, [], ())
        )
        for module in modules:
            self.load_js_module(module)
        maybe_method = self.js_methods.get(js_method.name, None)
        if maybe_method:
            if maybe_method != js_method:
                print(f"Created different version of {js_method.name} twice.")
        else:
            self.send_nowait(
                "method_def",
                (js_method.name, js_method.definition),
            )
            self.js_methods[js_method.name] = js_method
        return js_method.name, arguments

    def serialize_object(self, parent, key, value):
        obj_type = type(value)
        module, type_name = obj_type.__module__, obj_type.__name__
        if (
            module == "numpy"
            and type_name == "ndarray"
            or "pandas" in module
            and type_name == "Series"
        ):
            result = value.tolist()
        elif type_name == "DataFrame" and module.split(".", 1)[0] == "pandas":
            result = {name: value[name].to_list() for name in value.columns}
        elif "vegalite" in module and hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, enum.Enum):
            result = value.value
        else:
            raise Exception(f"Cannot serialize {value} of type {type(value)}")
        return self._serialize_value(parent, key, result)

    def _serialize_value(self, parent, key, value):
        if isinstance(value, POD_TYPE):
            return "value", value
        if isinstance(value, dict):
            return "dict", [
                (name, self._serialize(parent, attribute)) for name, attribute in value.items()
            ]
        if isinstance(value, (list, tuple, set)):
            return "list", [self._serialize(parent, element) for element in value]
        if isinstance(value, js):
            return "js_method", (
                value.name,
                [self._serialize(parent, arg) for arg in value.args],
            )
        if isinstance(value, (JSMethod, JSPartiallyAppliedCall)):
            name, arguments = self.serialize_js_method(value)
            return "js_method", (
                name,
                [self._serialize(parent, argument) for argument in arguments],
            )
        if isinstance(value, datetime.date):
            value = datetime.datetime(value.year, value.month, value.day)
        if isinstance(value, (datetime.datetime, datetime.time)):
            return "date", value.timestamp()
        if callable(value):
            # callable inside data are treated as callbacks
            value = Callback(value, None)
        if isinstance(value, Callback):
            return "callback", self.serialize_callback(key, value, None)
        if result := self.serialize_object(parent, key, value):
            return result
        raise Exception(
            f"Cannot serialize '{key}' argument. Value can be any arbitrarily nested list, tuple, dict containing the following types: {', '.join(x.__name__ for x in POD_TYPE)}. Received {value} of type: {type(value)}."
        )

    def serialize_props(self, parent, component: Component):
        result = {}
        for name in component.ATTRIBUTES + component.DATA:
            attribute = getattr(component, name)
            if attribute is None:
                continue
            # rmk: we evaluate callables at top level only, we test mapping first as they are callable
            if isinstance(attribute, Mapping):
                attribute = list(attribute())
            elif callable(attribute):
                while callable(attribute):
                    attribute = attribute()
            elif component.is_stale:
                continue  # not need to send static props again if the component is stale
            result["data-src" if name == "dataSrc" else name] = self._serialize(
                parent, attribute, name
            )
            component._props_values[name] = attribute
        if isinstance(component, InputComponent):
            component()  # forcing dependency
            if component.InputName:
                result[component.InputName] = self._serialize_value(
                    True, component.InputName, component.displayed_value()
                )
        # annoyingly defaultValue prevails on value in antd API...
        if not (result.get("defaultValue", None) is None or result.get("value", None) is None):
            if result.get("value", None):
                result.pop("defaultValue")
        return result

    def register_callback(self, method, hard_ref=False):
        callback_id = next(self.callback_counter)
        self.callbacks[callback_id] = method
        if hard_ref:
            self.callbacks_hard_refs.add(method)
        return callback_id

    def serialize_callback(self, argument_name, callback: Callback, input_control_params):
        result = callback.__dict__.copy()
        result.update(
            [
                ("argument_name", argument_name),
                ("input_control_params", input_control_params),
            ]
        )
        method = result.pop("method")
        if method is not None:
            result["callback_id"] = self.register_callback(method)
        return result

    def _serialize_component(self, parent, component: Component):
        if component._nb is None:
            self.load_js_module(component.Module)
            component._nb = component_nb = next(self.components_counter)
            component.mount_status = "mounting"
            self.components[component_nb] = component
            if parent is None:
                self.root_components[component_nb] = component
            else:
                component.parent = parent.weak_ref
            if component._window() is not self:
                raise Exception(
                    f"{component} has been created by another session. Component from other sessions cannot be reused or shared."
                )
        elif not component.is_stale:
            return "component", {"nb": component._nb, "reuse": True}
        result = {
            "key": component.key,
            "component_type": component.jsx_component_name(),
            "error": None,
            "nb": component._nb,
            "ref_hook": component.REF_HOOK,
        }
        with component.register_as_current_observer():
            result["_children"] = self.serialize_children(component)
            result["props"] = self.serialize_props(parent, component)
            # react children need to be keyed, we want the wrapper to have the same key if any (this is needed when wrapping ant menu items)
            callbacks = []
            callback_names = component.CALLBACKS
            if isinstance(component, InputComponent):
                callback_names = chain(callback_names, ["onChange"])
            for attribute_name in callback_names:
                if value := getattr(component, attribute_name):
                    callbacks.append(
                        self.serialize_callback(
                            attribute_name,
                            value,
                            input_control_params=[
                                component.InputName,
                                component.NewValuePath,
                            ]
                            if isinstance(component, InputComponent)
                            and attribute_name == getattr(component, "ChangeEventName", "onChange")
                            else None,
                        )
                    )
            result["callbacks"] = callbacks
        result["statefull"] = bool(
            parent is None
            or isinstance(component, InputComponent)
            or component.has_dependencies
            or component.on_didmount
            or component.on_unmount
            or component.REF_HOOK
        )
        return "component", result

    def _serialize(self, parent, component, name=None):
        if isinstance(component, Component):
            return self._serialize_component(parent, component)
        if isinstance(component, Props):
            component = {k: v for k, v in component.__dict__.items() if v is not None}
        return self._serialize_value(parent, name, component)

    def load_js_module(self, module):
        if module not in chain(self.loaded_modules, self.pending_modules):
            self.pending_modules[module] = anyio.Event()
            self.send_nowait("load js module", module)
            if links := LINKS_REGISTER.get(module, None):
                self.send_nowait("add links", tuple(links))

    def update_title(self, name):
        self.send_nowait("update tab name", name)

    def set_title(self, title):
        if callable(title):
            self.update_title = AutoRun(lambda: self.update_title(title()))
        else:
            self.update_title(title)
        self.title = title

    def update_client_links(self, links):
        if new_links := set(links).difference(self.loaded_links):
            self.send_nowait("add links", tuple(new_links))
            self.loaded_links.update(new_links)

    def add_css(self, hrefs):
        self.update_client_links([create_link_definition(href, None) for href in hrefs])

    def delete_component(self, component_nb):
        self.deleted_components.append(component_nb)

    def record_stale_component(self, component):
        component.is_stale = True
        self.stale_components.add(component.weak_ref)
        self.stale_components_event_sink.send_nowait(None)

    def update_hash(self, value):
        # we need the value to be updated immediately since the client code would expect it to contain the new value.
        # the actual notification will be triggerd by the client
        self.call_js_method("update_hash", [value])

    def location_reload(self):
        self.call_js_method("location.reload")

    def add_event_listener(self, event_name, method, js_callback=None):
        self.events_callbacks[event_name] = method
        self.call_js_method("add_event_listener", [event_name, js_callback])

    def update_full_screen(self, full_screen):
        self.call_js_method("update_full_screen", [full_screen])

    def stop(self):
        self.task_group.cancel_scope.cancel()

    def update_tag_style(self, properties, tag_name="body"):
        self.call_js_method("update_element_prop", [tag_name, [0, "style"], list(properties)])

    async def tear_down(self):
        try:
            await anyio.sleep_forever()
        finally:
            self.app_root = None
            self.root_components = None
            self.user_data.clear()

    async def start_app(self, update_client_history: bool, module):
        for method in (
            self.write_outputs,
            self.execution_loop,
            self.connection_loop,
            self.tear_down,
        ):
            self.task_group.start_soon(method)
        try:
            if update_client_history:
                self.call_js_method("history.pushState", ["app/" + self.script_path])
            # app_root must be kept alive throughout the whole connection lifespan
            self.add_css(getattr(module, "CSS", []))
            js_modules = getattr(module, "JS_MODULES", [])
            app = getattr(module, "app", None)
            if app is None or not callable(app):
                raise Exception(f"{inspect.getfile(module)} must define an app method!")
            self.app_root = await call_maybe_coroutine(app, (self,))
            if not isinstance(self.app_root, Component):
                raise TypeError(
                    f"Unexpected return type, application method must return a component. Received {type(self.app_root)} instead"
                )
            self.update_tag_style(
                dict(
                    chain(
                        DEFAULT_BODY_STYLE.items(),
                        getattr(module, "BODY_STYLE", {}).items(),
                    )
                ).items()
            )
            # this will cause relevant modules to be loaded
            serialized_root = self._serialize(None, self.app_root)
            for module in js_modules:
                self.load_js_module(module)
            await self.wait_for_modules_to_load()
        except Exception as e:
            try:
                # reset counter since it the root component
                self.components_counter = count()
                message = str(e) or type(e).__name__
                self.display_error_message(message)
                self.update_tag_style(DEFAULT_BODY_STYLE.items())
                from render_html import pre

                self.app_root = pre("".join(extract_client_stack()))
                serialized_root = self._serialize(None, self.app_root)
            except:  # noqa: E722
                traceback.print_exc()
                raise
        self.send_nowait("root", serialized_root)
        await self.update_components()

    async def subscribe_to_kernel_updates(self):
        await self._connection.send_to_server(SubscribeToKernelUpdates)


class Document:
    def __init__(self, window: Window) -> None:
        self.window = window

    def scrollTo(self, x: int, y: int):
        self.window.call_js_method(
            "call_js_builtin_method", ("document.documentElement.scroll", [x, y])
        )
