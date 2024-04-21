from __future__ import annotations

import inspect
import pprint
from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar
from functools import wraps
from itertools import count
from typing import TYPE_CHECKING, Generic, Optional, Set, TypeVar
from weakref import ReferenceType, ref

from typing_extensions import Self

if TYPE_CHECKING:
    from .window import Window
    from .controller import Controller

from .common import get_current_controller, get_window
from .utils import await_coroutine, copy_value

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
X = TypeVar("X")


CURRENT_OBSERVER = ContextVar["ObserverBase"]("CURRENT_OBSERVER", default=None)
OBJECT_KEYS = defaultdict(count)


class Revertable(ABC):
    @abstractmethod
    def revert(self):
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()


class SmartObject:
    """
    Creates a unique key for each instance of a class.
    This is not only mandated by React but also useful to troubleshoot dependency issues.
    """

    def __init__(self, key):
        assert isinstance(
            key, (str, int, type(None))
        ), f"invalid key type {type(key)} passed to {type(self)}"
        class_name = type(self).__name__
        key = f"<{class_name}:{key}:{next(OBJECT_KEYS[class_name])}>"
        self.key = key
        self.weak_ref: ReferenceType[Self] = ref(
            self,  # lambda _: print(f"{key} has been garbage collected")
        )

    def __str__(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return self.key


def touch_object():
    def result(func):
        @wraps(func)
        def touch_wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            finally:
                self.notify()

        return touch_wrapper

    return result


def record_observers(func):
    @wraps(func)
    def record_observers_wrapper(self, *args, **kwargs):
        if (observer := CURRENT_OBSERVER.get()) is not None:
            observer.has_dependencies = True
            self.add_observer(observer.weak_ref)
        return func(self, *args, **kwargs)

    return record_observers_wrapper


class ObserverBase(SmartObject):
    def __init__(self, key=None, controller: Optional[Controller] = None):
        super().__init__(key)
        self.controller = controller or get_current_controller()
        self.has_dependencies = False

    @abstractmethod
    def _update(self):
        pass

    @contextmanager
    def register_as_current_observer(self):
        previous_observer = CURRENT_OBSERVER.get()
        try:
            CURRENT_OBSERVER.set(self)
            yield
        finally:
            CURRENT_OBSERVER.set(previous_observer)

    def notify(self):
        pass


class ObservableBase(SmartObject, Revertable, Generic[T]):
    def __init__(self, key=None, controller: Optional[Controller] = None):
        super().__init__(key)
        self.controller = controller or get_current_controller()
        self.observers: Set[ReferenceType[ObserverBase]] = set()

    def add_observer(self, observer_handle):
        self.observers.add(observer_handle)

    def notify(self):
        self.controller.revertables.add(self)
        self.controller.notify_observables_observers([self])

    @property
    def value(self) -> T:
        return self.read()

    @value.setter
    def value(self, new_value: T):
        with self.write():
            self.update_value(new_value)

    @record_observers
    def read(self) -> T:
        return self._eval()

    @contextmanager
    def write(self) -> Generator[T]:
        try:
            yield self._eval()
        finally:
            self.notify()

    def eval(self) -> T:
        """Unmonitored access to the value. To be used with care."""
        if CURRENT_OBSERVER.get():
            raise Exception(
                f"{self}.eval should not be called while observers are being recorded"
            )
        return self._eval()

    def __call__(self) -> T:
        return self.read()

    def commit(self):
        self.previous_value = copy_value(self.value)

    def revert(self):
        self.update_value(self.previous_value)

    def __iadd__(self, value):
        self.value += value
        return self

    def __isub__(self, value):
        self.value -= value
        return self

    def __imul__(self, value):
        self.value *= value
        return self

    def __itruediv__(self, value):
        self.value /= value
        return self

    def __ifloordiv__(self, value):
        self.value //= value
        return self

    def toggle(self):
        self.value = not self.eval()


class Observable(ObservableBase[T]):
    def __init__(
        self,
        value: Optional[T] = None,
        key=None,
        controller=None,
    ):
        super().__init__(key=key, controller=controller)
        self._value = value
        self.previous_value = value

    def update_value(self, new_value):
        if self._value is not new_value:
            if isinstance(self._value, dict):
                self._value.clear()
                self._value.update(new_value)
            elif isinstance(self._value, list):
                self._value.clear()
                self._value.extend(new_value)
            else:
                self._value = new_value

    def reset(self, value):
        self._value = value
        self.notify()

    def _eval(self):
        return self._value


class ObservableValue(Generic[T]):
    def __init__(
        self,
        value=None,
        key=None,
        controller=None,
    ):
        self._value = Observable(value, key=key, controller=controller)

    def eval(self):
        return self._value.eval()

    def _eval(self):
        return self._value._eval()

    def set(self, value=None):
        self._value.value = value

    def notify(self):
        self._value.notify()

    def __call__(self) -> T:
        try:
            return self._value.read()
        except Exception as e:
            raise Exception(f"Error while evaluating {self}") from e

    def __bool__(self):
        raise Exception(
            f"{type(self)} does not implement boolean conversion. You almost certainly want to evaluate its content instead, in that case just add a pair of brackets at the end."
        )

    def __iter__(self):
        return self._value.value.__iter__()

    def __iadd__(self, value):
        self._value += value
        return self

    def __isub__(self, value):
        self._value -= value
        return self

    def __imul__(self, value):
        self._value *= value
        return self

    def __itruediv__(self, value):
        self._value /= value
        return self

    def __ifloordiv__(self, value):
        self._value //= value
        return self

    def toggle(self):
        self._value.toggle()


class AutoRun(ObserverBase):
    def __init__(self, method, key=None, controller=None):
        assert callable(
            method
        ), "autorun argument must be callable. You might have forgotten to put a lambda in front of the expression to evaluate..."
        super().__init__(key=key, controller=controller)
        self.method = method
        self.maybe_window: Optional[ReferenceType[Window]] = None
        if window := get_window(throw_if_none=False):
            self.maybe_window = window.weak_ref
            # autoruns are kept alive throughout a sesssion
            window.hard_references.add(self)
        self.stopped = False
        self._update()

    def stop(self):
        self.stopped = True
        if self.maybe_window:
            self.maybe_window().hard_references.discard(self)

    def update_method(self, method):
        self.method = method

    def _update(self):
        if self.stopped:
            return
        with self.register_as_current_observer():
            result = self.method()
            if inspect.isawaitable(result):
                self.maybe_window().start_soon(await_coroutine, result, name=f"{self} autorun")


class CachedEvaluation(ObserverBase):
    def __init__(
        self,
        method,
        args=(),
        key=None,
        controller=None,
        argument_id=None,
    ):
        super().__init__(key=key, controller=controller)
        self.method = method
        self.args = args
        self.is_stale = True
        self.current_value = Observable(None, key=key, controller=controller)
        self.argument_id = argument_id

    def __call__(self):
        if self.is_stale:
            self.is_stale = False
            with self.register_as_current_observer():
                r = self.method(*self.args)
                self.current_value.update_value(r)
        return self.current_value.read()

    def notify(self):
        self.is_stale = True
        self.current_value.notify()


class MemoizedMethod:
    def __init__(self, method, key=None, controller=None):
        self.controller = controller or get_current_controller()
        self.key = key
        self._cached_results = {}
        self.method = method

    def __call__(self, *args):
        if args not in self._cached_results:
            self._cached_results[args] = CachedEvaluation(
                self.method,
                args=args,
                key=f"{self.key}{args}",
                controller=self.controller,
            )
        return self._cached_results[args]()


def memoize(key=None, controller=None):
    def result(method):
        return MemoizedMethod(method, key=key, controller=controller)

    return result


def autoprint(method, key=None, controller=None):
    return AutoRun(lambda: print(method()), key=key, controller=controller)


def autopprint(method, key=None, controller=None):
    return AutoRun(lambda: pprint.pprint(method()), key=key, controller=controller)


def autorun(method, key=None, controller=None):
    return AutoRun(method, key=key, controller=controller)
