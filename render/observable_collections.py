from typing import Dict, Generic, Iterable, List, Optional, TypeVar

from .observability import Observable, SmartObject

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class ObservableCollectionMixin(SmartObject):
    def __len__(self) -> int:
        return self.values.read().__len__()

    def _eval(self):
        return self.values._eval()

    def clear(self):
        with self.values.write() as write_values:
            write_values.clear()

    def notify(self):
        self.values.notify()


class ObservableList(ObservableCollectionMixin, Generic[T]):
    def __init__(
        self,
        values: Optional[List[T]] = None,
        key=None,
        controller=None,
    ):
        super().__init__(key=key)
        if values is None:
            values = []
        if not isinstance(values, list):
            raise ValueError(f"Expected list, got {type(values)}")
        self.values = Observable[List[T]](values, key=f"{key} values", controller=controller)

    def __call__(self) -> List[T]:
        return self.values.read()

    def set(self, values: List[T]):
        self.values.reset(values)

    def __setitem__(self, index: int, value: V):
        with self.values.write() as write_values:
            write_values[index] = value

    def append(self, value: T):
        with self.values.write() as write_values:
            write_values.append(value)

    def pop(self, index: int) -> T:
        with self.values.write() as write_values:
            return write_values.pop(index)

    def extend(self, values: Iterable[T]):
        with self.values.write() as write_values:
            write_values.extend(values)

    def clear(self):
        with self.values.write() as write_values:
            write_values.clear()

    def remove(self, value):
        with self.values.write() as write_values:
            write_values.remove(value)

    def __contains__(self, value):
        return self.values.read().__contains__(value)

    def __iter__(self) -> Iterable[T]:
        return self.values.read().__iter__()

    def __getitem__(self, index: int) -> T:
        return self.values.read().__getitem__(index)

    def count(self, value):
        return self.values.read().count(value)

    def index(self, value):
        return self.values.read().index(value)

    def insert(self, index, value):
        with self.values.write() as write_values:
            write_values.insert(index, value)


class ObservableDict(ObservableCollectionMixin, Generic[K, V]):
    def __init__(self, values=None, key=None, controller=None):
        super().__init__(key=key)
        self.values = Observable[Dict[K, V]](values or {}, key=f"{key} values", controller=controller)

    def set(self, values: Dict[K, V]):
        self.values.reset(values)

    def __setitem__(self, key: K, value: V):
        with self.values.write() as write_values:
            write_values[key] = value

    def __getitem__(self, key: K) -> T:
        return self.values.read()[key]

    def update(self, values):
        with self.values.write() as write_values:
            write_values.update(values)

    def pop(self, key: K) -> T:
        with self.values.write() as write_values:
            return write_values.pop(key)

    def get(self, key: K, default=None) -> T:
        return self.values.read().get(key, default)

    def setdefault(self, key: K, default=None) -> T:
        return self.values.read().setdefault(key, default)

    def keys(self):
        return self.values.read().keys()

    def values(self):
        return self.values.read().values()

    def items(self):
        return self.values.read().items()

    def __contains__(self, key: K):
        return self.values.read().__contains__(key)

    def __iter__(self) -> Iterable[K]:
        return self.values.read().__iter__()

    def __call__(self) -> Dict[K, V]:
        return self.values.read()

    def __delattr__(self, key: K) -> None:
        return self.pop(key)


class ObservableObject(ObservableCollectionMixin):
    def __init__(self, obj=None, key=None, controller=None):
        ObservableCollectionMixin.__init__(self, obj.__dict__, obj, key, controller=controller)

    def set(self, new_object):
        assert all(
            k1 == k2 for k1, k2 in zip(self.back_ref.keys(), new_object.__dict__.keys())
        ), f"{list(self.back_ref.keys()): }{list(new_object.__dict__.keys())}"
        self.back_ref = new_object.__dict__


def create_getter(name):
    def result(self):
        return self.back_ref[name]

    return result
