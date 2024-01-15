import pytest

import render as r

from .utils import setup_controller  # noqa: F401
from .utils import run_and_check_calls_count


def call(callable: callable, *args, **kwargs):
    return callable(*args, **kwargs)


OBSERVER_TYPES = {
    "memoize": lambda observable: r.memoize("observer")(observable),
    "cached_evaluation": lambda observable: r.CachedEvaluation(observable),
}


def create_check_number_of_calls(observer):
    method = run_and_check_calls_count(observer)

    def check_number_of_calls(number_of_calls, operation, expected_value=None):
        with method.check_number_of_calls(number_of_calls):
            if not expected_value:
                expected_value = operation()
            else:
                operation()
        assert method() == expected_value
        return expected_value

    return check_number_of_calls


class BaseTest:
    def accessor(self):
        return self.observable()

    def initialize(self):
        pass

    @pytest.mark.parametrize("observer_type", OBSERVER_TYPES)
    def test_commit_revert(self, observer_type):
        self.initialize()
        with self.controller:
            observer = OBSERVER_TYPES[observer_type](self.accessor)
            check = create_check_number_of_calls(observer)
        value_1 = check(1, self.mutation_1)
        # commit does not change existing value, nor trigger observers
        check(0, self.controller.commit, value_1)
        # mutation does change existing value, and trigger observers
        value_2 = check(1, self.mutation_2)
        # commit does not change existing value, nor trigger observers
        check(0, self.controller.commit, value_2)
        # mutation does change existing value, and trigger observers
        value_3 = check(1, self.mutation_3)
        # revert does revert to previously commited value, and trigger observers
        check(1, self.controller.revert, value_2)
        # revert is idempotent
        check(1, self.controller.revert, value_2)
        value_3 = check(1, self.mutation_3)
        # commit is idempotent
        check(0, self.controller.commit, value_3)
        check(0, self.controller.commit, value_3)


class TestObservableValueAlteringValue(BaseTest):
    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableValue(0)

    def mutation_1(self):
        self.observable.set(1)
        return 1

    def mutation_2(self):
        self.observable.set(2)
        return 2

    def mutation_3(self):
        self.observable += 1
        return 3


class TestDictOfObservablesAlteringValue(BaseTest):
    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.DictOfObservables({"a": 1})

    def accessor(self):
        return self.observable["a"]()

    def mutation_1(self):
        self.observable.set({"a": 2})
        return 2

    def mutation_2(self):
        self.observable.set({"a": 3})
        return 3

    def mutation_3(self):
        self.observable["a"] *= 4
        return 12


class TestDictOfObservables(BaseTest):
    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.DictOfObservables({"a": 1})

    def accessor(self):
        return self.observable["a"]()

    def mutation_1(self):
        self.observable["a"] = 2
        return 2

    def mutation_2(self):
        self.observable["a"] *= 3
        return 6

    def mutation_3(self):
        self.observable["a"] *= 2
        return 12


class TestObservableListOfDictOfObservables(BaseTest):
    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableList()
            self.m = r.Mapping(r.DictOfObservables, self.observable, key="l2")
            self.m1 = r.Mapping(lambda x: x["a"](), self.m, key="l2")

    def initialize(self):
        self.observable.set([{"a": 2}])

    def accessor(self):
        return self.m1()[0]

    def mutation_1(self):
        self.m()[0]["a"] = 3
        return 3

    def mutation_2(self):
        self.m()[0]["a"] *= 4
        return 12

    def mutation_3(self):
        self.m()[0]["a"] *= 2
        return 24


class TestObservableDict(BaseTest):
    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableDict()

    def initialize(self):
        self.observable.set({"a": 1})

    def mutation_1(self):
        self.observable["b"] = 2
        return {"a": 1, "b": 2}

    def mutation_2(self):
        self.observable.pop("a")
        return {"b": 2}

    def mutation_3(self):
        self.observable.update({"a": 2})
        return {"a": 2, "b": 2}


class TestObservableDictSet(BaseTest):
    def initialize(self):
        self.observable.set({"a": 1})

    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableDict({"a": 1})

    def mutation_1(self):
        self.observable["a"] = 2
        return {"a": 2}

    def mutation_2(self):
        self.observable["a"] = 3
        return {"a": 3}

    def mutation_3(self):
        self.observable["a"] *= 4
        return {"a": 12}


class TestObservableListSet(BaseTest):
    def initialize(self):
        self.observable.set([0])

    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableList()

    def mutation_1(self):
        self.observable[0] = 1
        return [1]

    def mutation_2(self):
        self.observable[0] = 3
        return [3]

    def mutation_3(self):
        self.observable[0] *= 2
        return [6]


class TestObservableListAppendExtendRemove(BaseTest):
    def initialize(self):
        self.observable.set([0])

    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableList()

    def mutation_1(self):
        self.observable.append(1)
        return [0, 1]

    def mutation_2(self):
        self.observable.extend([2, 3])
        return [0, 1, 2, 3]

    def mutation_3(self):
        self.observable.remove(1)
        return [0, 2, 3]


class TestObservableListAppendExtendRemoveMapping(BaseTest):
    def initialize(self):
        self.observable.set([0])

    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableList()
            self.mapping = r.create_mapping(lambda x: x * x, self.observable)

    def accessor(self):
        return self.mapping()

    def mutation_1(self):
        self.observable.append(1)
        return [0, 1]

    def mutation_2(self):
        self.observable.extend([2, 3])
        return [0, 1, 4, 9]

    def mutation_3(self):
        self.observable.remove(1)
        return [0, 4, 9]


class TestObservableListAppendExtendRemoveChainedMapping(BaseTest):
    def initialize(self):
        self.observable.set([0])

    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.ObservableList()
            mapping = r.create_mapping(lambda x: x * x, self.observable)
            self.mapping = r.create_mapping(lambda x: x + 1, mapping)

    def accessor(self):
        return self.mapping()

    def mutation_1(self):
        self.observable.append(1)
        return [1, 2]

    def mutation_2(self):
        self.observable.extend([2, 3])
        return [1, 2, 5, 10]

    def mutation_3(self):
        self.observable.remove(1)
        return [1, 5, 10]


class TestRecombiningDependencies(BaseTest):
    """Observable mutations trigger indirect observers updates exactely once."""

    def initialize(self):
        self.observable.set(0)

    def accessor(self):
        return self.observer()

    def setup_class(self) -> None:
        with r.Controller() as self.controller:
            self.observable = r.create_observable(0, key="value")
            observer_1 = r.CachedEvaluation(self.observable, key="observer_1")
            observer_2 = r.CachedEvaluation(self.observable, key="observer_2")
            self.observer = r.CachedEvaluation(
                lambda: observer_1() + observer_2(), key="observer_3"
            )

    def mutation_1(self):
        self.observable.set(1)
        return 2

    def mutation_2(self):
        self.observable.set(2)
        return 4

    def mutation_3(self):
        self.observable.set(3)
        return 6
