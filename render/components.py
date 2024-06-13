from collections.abc import Iterable

from more_itertools import first

from .common import get_window
from .reactor.observability import ObservableValue, ObserverBase
from .reactor.dict_of_observables import ObservableElement
from .reactor.observable_collections import ObservableList
from .utils import CatchError

JSMETHODS_REPOSITORY = {}


class JSRemoteCallError(Exception):
    pass


class js_call:
    def __init__(self, name: str, *args):
        self.name = name
        self.args = args


class JSMethod:
    def __init__(self, name: str, definition: str):
        JSMETHODS_REPOSITORY[name] = self
        self.name = name
        self.definition = definition
        self.modules = ()

    def __call__(self, *args):
        return JSPartiallyAppliedCall(self, args)


def create_js_callback(name: str, definition: str):
    return JSMethod(name, definition)


class JSPartiallyAppliedCall:
    def __init__(self, js_method, arguments):
        self.js_method = js_method
        self.arguments = arguments


class Props:
    """This is a marker class for the props of a component. It is transformed into a regular JS object."""

    pass


class RemoteObject:
    def __init__(self):
        self._nb = None

    async def call_method(self, method_name, args=()):
        window = self._window()
        assert self._nb is not None, (
            f"cannot call a method before the component has been rendered: {self}.{method_name}."
            f"You might want to use componentDidMount for proper synchronization."
        )
        result_id, remote_call_outcome = window.create_pending_result()
        arguments = [window._serialize(None, arg) for arg in args]
        await window.wait_for_modules_to_load()
        window.send_nowait("remote call", (self._nb, method_name.split("."), arguments, result_id))
        success, result = await remote_call_outcome
        if not success:
            with CatchError():
                raise JSRemoteCallError(result, method_name, args)
        return result

    def __del__(self):
        if getattr(self, "_nb", None) and self._window():
            self._window().delete_component(self._nb)


class Component(ObserverBase, RemoteObject):

    JSXName = None
    REF_HOOK = None
    CALLBACKS = []
    DATA = []
    ATTRIBUTES = []

    def __init__(
        self,
        key,
        controller=None,
        children=None,
        componentDidMount=None,
        componentWillUnmount=None,
    ):
        ObserverBase.__init__(self, controller=controller, key=key)
        RemoteObject.__init__(self)
        self.children = children
        self._cached_children = None
        self._props_values = {}
        self.on_didmount = componentDidMount
        self.on_unmount = componentWillUnmount
        self.mount_status = "unknown"
        self.is_stale = False
        self.parent = None
        self.parent_relationship = None
        self._callbacks_holder = []
        self.children_counter = 0

    def _window(self):
        maybe_window = get_window(throw_if_none=True)
        return maybe_window.weak_ref() if maybe_window else None

    def _children(self):
        children = self.children
        while not isinstance(children, InputComponent) and callable(children):
            children = children()
        if children is None:
            return []
        # children can be a single child or a list of children
        if not isinstance(children, Iterable) or isinstance(children, (str, Component)):
            children = first(children)
        return children

    def __repr__(self) -> str:
        return f"<{self.Module}.{self.JSXName or type(self).__name__}:{self.key}>"

    def _update(self):
        if self.mount_status != "unknown":
            self._window().record_stale_component(self)

    def finalize(self):
        """will be called in the __init__ of the subclass if needed"""
        raise NotImplementedError("finalize must be implemented in the subclass")


class InputComponent(Component):
    """
    We need to be able to tell when an input component has been updated or whether its underlying observable value has been updated.
    We don't send an update back to the component in the former case as it causes antd datepicker to enter in an infinite loop.
    """

    NewValuePath = ""
    ChangeEventName = "onChange"

    def __init__(self, key, controller, children, onChange, value, default_value):
        super().__init__(key, controller, children)
        self.input_value_update = False
        if isinstance(value, (ObservableValue, ObservableElement, ObservableList)):
            if default_value is not None:
                raise Exception("Input component value and default value cannot be both speficied.")
            self._value, default_value = value, value._eval()
        else:
            if value is not None:
                raise TypeError(
                    f"{self.InputName} must be one of (ObservableValue, ObservableElement) if specified found {type(value)} instead"
                )
            self._value = ObservableValue(default_value, controller=controller, key=key)
        with self.register_as_current_observer():
            self._displayed_value = self._value()
        if default_value is not None:
            setattr(
                self,
                "default" + self.InputName[0].upper() + self.InputName[1:],
                default_value,
            )
        if onChange:
            if not callable(onChange):
                raise Exception(
                    f"When specified, an onChange argument must be a callback taking the new value as argument, received {onChange} instead."
                )

        def onchange_callback(new_value):
            if onChange:
                new_value = onChange(new_value)
            self._displayed_value = new_value
            try:
                if not hasattr(self, "validate") or self.validate(new_value):
                    self.input_value_update = True
                    self._value.set(new_value)
                    with self.register_as_current_observer():
                        self._value()
            except Exception as e:
                print("change callback failed", e)
            finally:
                self.input_value_update = False

        setattr(
            self,
            self.ChangeEventName,
            Callback(
                onchange_callback,
                data_paths=[[0] + (self.NewValuePath.split(".") if self.NewValuePath else [])],
            ),
        )

    def displayed_value(self):
        return self._displayed_value

    def set(self, value):
        self._value.set(value)

    def __call__(self):
        return self._value()

    def eval(self):
        return self._value.eval()

    def evaluate(self):
        return self()

    def _update(self):
        if self.input_value_update:
            return
        Component._update(self)
        self._displayed_value = self._value._eval()


class Callback:

    def __init__(
        self,
        method=None,
        data_paths=(),
        prevent_default=False,
        stop_propagation=False,
        is_promise=False,
        callback_name=None,
    ):
        assert not isinstance(method, Callback)
        self.method = method
        self.data_paths = data_paths
        self.is_promise = is_promise
        self.stop_propagation = stop_propagation
        self.prevent_default = prevent_default
        self.callback_name = callback_name
        self.callback_id = next(get_window().callback_counter)


def create_callback(maybe_callback_or_callable, argument_name="", data_paths=(), is_promise=False):
    if maybe_callback_or_callable is None or isinstance(maybe_callback_or_callable, Callback):
        return maybe_callback_or_callable
    assert callable(
        maybe_callback_or_callable
    ), f"{argument_name} must be callable, {maybe_callback_or_callable}"
    return Callback(maybe_callback_or_callable, data_paths, is_promise=is_promise)


def js_arrow(name: str, definition: str, modules=()) -> JSMethod:
    result = JSMethod(name, definition)
    result.modules = [
        module.replace("render_", "").replace("ant_icons", "ant-icons") for module in modules
    ]
    return result
