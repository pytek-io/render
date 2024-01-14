from functools import wraps
from typing import Callable, Generic, Iterable, List, TypeVar

from .common import call_if_callable
from .observability import CachedEvaluation
from .observable_collections import ObservableList, SmartObject

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
X = TypeVar("X")


class Mapping(SmartObject, Generic[X, V]):
    """
    Observe the Wrap all evaluations individually so as to cache evaluations elementwise. This allows client code to have a fine dependency structure. This means that if an argument value is altered only its dependencies are invalidated.
    """

    def __init__(
        self,
        method: Callable[[T], V],
        arguments: ObservableList[T],
        key=None,
        controller=None,
        evaluate_argument=False,
    ):
        super().__init__(key=key)
        self.method = method
        self.arguments = arguments
        self.controller = controller
        if evaluate_argument:

            @wraps(method)
            def _method(arg):
                return method(call_if_callable(arg))

            self.method = _method
        self.previous_evaluations = {}
        self.cached_evaluations = CachedEvaluation(self.evaluations, key=key, controller=controller)

    def __evaluate__(self):
        return self.cached_evaluations()

    def __iter__(self) -> Iterable[V]:
        return (v() for v in self.cached_evaluations())

    def __getitem__(self, index) -> Callable[[], V]:
        return self.cached_evaluations()[index]

    def __len__(self):
        return len(self.cached_evaluations())

    def __call__(self) -> List[V]:
        return [value() for value in self.cached_evaluations()]

    def evaluations(self):
        new_values = [
            (
                (
                    argument_id,
                    self.previous_evaluations[argument_id]
                    if argument_id in self.previous_evaluations
                    else CachedEvaluation(
                        self.method,
                        args=[argument],
                        key=f"{self.key}[{argument_id}]",
                        controller=self.controller,
                        argument_id=argument_id,
                    ),
                )
            )
            for argument_id, argument in ((id(argument), argument) for argument in self.arguments())
        ]
        self.previous_evaluations = dict(new_values)
        _, results = zip(*new_values) if new_values else ([], [])
        return results


def MultiMapping(method, args, key=None):
    @wraps(method)
    def star_method(args):
        return method(*args)

    return Mapping(star_method, lambda: zip(*args), key=key)
