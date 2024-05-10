from contextlib import contextmanager
from typing import Callable, Iterable, List, Optional, Set
from weakref import ReferenceType

from itertools import chain
from ..common import CURRENT_CONTROLLER
from .observability import ObservableBase, ObserverBase, Revertable
from ..utils import groupby, print_exception, resolve_weak_refs


class Controller:
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name
        self.revertables: Set[Revertable] = set()
        self.stale_outside_observers: Set[ReferenceType[ObserverBase]] = set()
        self.stale_inside_observers: Set[ObserverBase] = set()
        self.inside_transaction = False
        self.previous_controller = None

    def _touch_objects(self, observables):
        for observable in observables:
            if (
                observable in self.stale_inside_observers
                or observable in self.stale_outside_observers
            ):
                continue
            if observable.controller is self:
                self.stale_inside_observers.add(observable)
                if isinstance(observable, ObserverBase):
                    observable.notify()
                if isinstance(observable, ObservableBase):
                    self._touch_objects(resolve_weak_refs(observable.observers))
                    observable.observers.clear()
            else:
                self.stale_outside_observers.add(observable)

    @contextmanager
    def notify_transaction(self):
        inside_transaction, self.inside_transaction = (self.inside_transaction, True)
        try:
            yield
        finally:
            self.inside_transaction = inside_transaction
        if not inside_transaction:
            self.stale_inside_observers, stale_inside_observers = set(), self.stale_inside_observers
            try:
                for observer in stale_inside_observers:
                    with print_exception():
                        observer._update()
            finally:
                self.inside_transaction = False

    def notify_observers(self, observers: Iterable[ObserverBase]):
        with self.notify_transaction():
            for observer in observers:
                if not (
                    observer in self.stale_inside_observers
                    or observer in self.stale_outside_observers
                ):
                    if observer.controller is self:
                        self.stale_inside_observers.add(observer)
                        observer.notify()
                    else:
                        self.stale_outside_observers.add(observer)
        # In rare cases, new observers may have been notified during the updates (eg: inside AutoRun updates)
        if not self.inside_transaction and self.stale_inside_observers:
            self.stale_inside_observers, stale_inside_observers = set(), self.stale_inside_observers
            self.notify_observers(stale_inside_observers)

    def notify_observables_observers(self, observables: List[ObservableBase]):
        observers = set(chain.from_iterable(observable.observers for observable in observables))
        for observable in observables:
            observable.observers.clear()
        self.notify_observers(observer() for observer in observers if observer())

    def revert(self):
        observables, self.revertables = self.revertables, set()
        for revertable in observables:
            revertable.revert()
        self.notify_observables_observers(observables)

    def commit(self):
        for revertable in self.revertables:
            revertable.commit()
        self.revertables.clear()
        key: Callable[[ObservableBase], Controller] = lambda o: o.controller  # noqa: E731
        for controller, observers in groupby(self.stale_outside_observers, key):
            controller.notify_observers(observers)
        self.stale_outside_observers.clear()

    def __enter__(self):
        self.previous_controller = CURRENT_CONTROLLER.get()
        CURRENT_CONTROLLER.set(self)
        return self

    def __exit__(self, _type, _value, _traceback):
        CURRENT_CONTROLLER.set(self.previous_controller)
        self.previous_controller = None
