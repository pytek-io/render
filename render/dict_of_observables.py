from typing import Callable, Dict, Generic, Optional, TypeVar

from .observability import (ObservableBase, ObservableValue, copy_value,
                            get_current_controller)

K = TypeVar("K")
V = TypeVar("V")


class ObservableElement(ObservableBase):
    def __init__(self, collection, index_or_key, key=None, controller=None):
        super().__init__(
            key=key or index_or_key,
            controller=controller,
        )
        self.collection: DictOfObservables = collection
        self.index_or_key = index_or_key
        self.previous_value = copy_value(self.collection.actual_value._eval()[self.index_or_key])

    def update_value(self, new_value):
        current_value = self.collection.actual_value._eval()[self.index_or_key]
        if current_value is not new_value:
            if isinstance(current_value, dict):
                current_value.clear()
                current_value.update(new_value)
            elif isinstance(current_value, list):
                current_value.clear()
                current_value.extend(new_value)
            else:
                self.collection.actual_value._eval()[self.index_or_key] = new_value

    def _eval(self):
        return self.collection.actual_value._eval()[self.index_or_key]

    def set(self, value):
        self.update_value(value)
        self.notify()


class DictOfObservables(Generic[K, V]):
    underlying_type = dict

    def __init__(self, values: Optional[Dict[K, V]] = None, key=None, controller=None):
        self.key = key
        self.controller = controller or get_current_controller()
        self.actual_value = ObservableValue({} if values is None else values)
        self.observable_elements = {
            k: ObservableElement(self, k, controller=controller) for k in values
        }

    def __getitem__(self, key: K) -> Callable[[], V]:
        return self.observable_elements[key]

    def __setitem__(self, key: K, value: V):
        # incremental operations update the underlying value but still call this method with the OservableElement
        if isinstance(value, ObservableElement):
            return
        if key not in self.observable_elements:
            self.observable_elements[key] = ObservableElement(self, key)
        self.observable_elements[key].value = value

    def items(self):
        return ((k, v()) for k, v in self.observable_elements.items())

    def set(self, values):
        self.actual_value.set(values)
        for element in self.observable_elements.values():
            element.notify()

    def back_reference(self):
        return self.actual_value()
