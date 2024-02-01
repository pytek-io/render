from typing import Dict

import anyio

import render as r

from .utils import (  # noqa: F401
    count_calls,
    identity,
    pytestmark,
    run_and_check_calls_count,
    setup_controller,
)


def test_observable_list_length():
    """Mutating methods trigger observer exactely once.."""
    observed_value = None
    observable = r.ObservableList([], key="value")

    @run_and_check_calls_count
    def update_observed_value():
        nonlocal observed_value
        for i in observable:
            print(i)
        observed_value = len(observable())

    for i in range(5):
        with update_observed_value.check_number_of_calls():
            observable.append(i)
        assert observed_value == i + 1


def get_value_item(dict_obj):
    return dict_obj["value"]


def set_object_attribute(obj):
    obj.a = 3


def get_object_attribute(obj):
    return obj.a


def test_memoize():
    a = r.ObservableValue(2, key="a")
    func = count_calls(lambda: a() * 2)
    test = r.memoize(key="test")(func)
    assert test() == 4
    assert test() == 4
    assert func.counter == 1
    a.set(3)
    assert test() == 6
    assert func.counter == 2


def test_controlled_memoize():
    controller = r.Controller()
    a = r.ObservableValue(2, key="a", controller=controller)
    func = count_calls(lambda: a() * 2)
    test = r.memoize(key="test")(func)
    assert test() == 4
    a.set(3)
    assert a() == 3
    assert test() == 4
    controller.commit()
    assert test() == 6
    assert func.counter == 2


def test_observable_list():
    actual_list = []
    observable_list = r.ObservableList(actual_list)
    index = 0

    def check():
        assert observable_list() == actual_list, "observable_list != actual_list"
        assert actual_list == list(range(index))
        for i in range(index):
            assert observable_list[i] == i

    test = run_and_check_calls_count(check)
    for i in range(5):
        with test.check_number_of_calls():
            index += 1
            observable_list.append(i)
    index -= 1
    for i in range(5):
        with test.check_number_of_calls():
            observable_list.remove(index)
            index -= 1


def test_multi_mapping():
    def test(a, b):
        print("test_multi_mapping")
        return a, b

    l = [{"a": 2}]
    l1 = r.ObservableList(l)
    l2 = r.Mapping(identity, l1, key="l2")
    m = r.MultiMapping(test, [l2, l1], key="m")
    print(list(m))
    print("-" * 20)
    l1.append({"b": 2})
    print(list(m))


class A:
    pass


def test_list_set():
    l = []
    o = r.ObservableList[int](l)
    o.append(1)
    o.set([2])
    print(o())


def test_simple():
    l = []
    o = r.ObservableList[r.ObservableList[int]](l)
    o.append([1])
    print(o(), l)
    o.set([[2]])
    print(o(), l)


def test_nested():
    for constructor, is_nested, is_typed in (
        (r.ObservableList, False, False),
        (r.ObservableList[Dict], False, True),
        (r.ObservableList[str], False, True),
        (r.ObservableList[r.ObservableDict], True, True),
    ):
        suffix = ""
        values = [{"value": "ATPVJCDGLL"}]
        values_obs = constructor(values)
        collections = [values_obs, values]
        getattr(values_obs, "append" + suffix)({"value": "DEFTR"})
        assert {"value": "DEFTR"} in values
        if not is_nested:
            assert {"value": "DEFTR"} in values_obs()
        assert all(len(collection) == 2 for collection in collections)
        getattr(values_obs, "remove" + suffix)({"value": "DEFTR"})
        assert all({"value": "DEFTR"} not in collection for collection in collections)
        assert all(len(collection) == 1 for collection in collections)
        print(values_obs())


def test_controlled_cached_evaluation():
    value = r.ObservableValue(1)
    controller = r.Controller()
    cached_eval = r.CachedEvaluation(lambda: value() * 2, controller=controller)
    r.autorun(lambda: print(cached_eval()))
    value.set(2)
    print(cached_eval())


async def test_controlled_cached_evaluation_async():
    try:
        async with anyio.create_task_group() as tg:
            tg.start_soon(test)
    except Exception as e:
        print(e)


def test_notification_during_updates():
    obs1 = r.ObservableValue(1)
    obs2 = r.ObservableValue(2)

    def update():
        obs1()
        obs2.set(3)

    auto_run_1 = r.AutoRun(update, "auto_run_1")
    auto_run_2 = r.AutoRun(obs2, "auto_run_2")
    obs1.set(2)
