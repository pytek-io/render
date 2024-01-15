import pytest

pytestmark = pytest.mark.anyio

import contextlib
from typing import Any

import render as r
from render import autorun
from render.common import CURRENT_CONTROLLER


@pytest.fixture(scope="session", autouse=True)
def setup_controller(request):
    CURRENT_CONTROLLER.set(r.Controller())


def square(value: int) -> int:
    return value * value


def identity(value):
    if callable(value):
        return value()
    else:
        return value


def evaluate_values(values):
    return [(value() if callable(value) else value) for value in values]


class CallCounter:
    def __init__(self, method) -> None:
        self.method = method
        self.counter = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.counter += 1
        return self.method(*args, **kwargs)


class CallChecker:
    def __init__(self, method, controller=None, create_autorun=True):
        self.method = CallCounter(method)
        if create_autorun:
            self.autorun = autorun(self, controller=controller)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.method(*args, **kwargs)

    @contextlib.contextmanager
    def check_number_of_calls(self, expected_number_calls=1, description=""):
        previous_counter = self.method.counter
        yield self
        if self.method.counter != previous_counter + expected_number_calls:
            message = f"{self.method.method} called {self.method.counter - previous_counter} times, expected {expected_number_calls}"
            if description:
                message = f"{description} failed {message}"
            raise Exception(message)


def run_and_check_calls_count(method, controller=None) -> CallChecker:
    return CallChecker(method, controller)


def count_calls(method) -> CallCounter:
    return CallCounter(method)
