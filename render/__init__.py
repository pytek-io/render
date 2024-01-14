import os
import pprint
import sys
from os.path import dirname, join
from subprocess import run
from typing import Optional

from lxml.html import parse

from .async_objects import AsyncCachedEvaluation, AsyncGenerator
from .common import get_window as _get_window
from .components import (JSMETHODS_REPOSITORY, Callback, Component,
                         InputComponent, JSMethod, Props, console,
                         create_callback, create_js_callback, js, js_arrow,
                         schedule_callback)
from .controller import Controller
from .dict_of_observables import DictOfObservables
from .mapping import Mapping, MultiMapping
from .observability import (AutoRun, CachedEvaluation, MemoizedMethod,
                            ObservableValue)
from .observable_collections import ObservableDict, ObservableList
from .props import ChildContainer, Container
from .utils import ResponsiveValue, add_data_namespace, call_maybe_coroutine
from .window import Window, WindowSize, register_css_for_module

__version__ = "0.8.0"


OBSERVABLE_TYPES = {
    list: ObservableList,
    dict: ObservableDict,
}


def location():
    return dirname(__file__)


def launch_server():
    run([join(dirname(__file__), "render")] + sys.argv[1:])


def get_js_entry_point(render_data_path):
    return dict(parse(os.path.join(render_data_path, "index.html")).find(".//script").items())[
        "src"
    ]


def read_version(version: str):
    return [int(x) for x in version.split(".")]


def assert_render_version(version):
    if read_version(__version__) < read_version(version):
        raise Exception(
            f"Client code requires Render version {version}, but found {__version__}. Please upgrade render."
        )


def get_window() -> Window:
    return _get_window()


def create_mapping(method, arguments, key=None, controller=None, evaluate_argument=True) -> Mapping:
    return Mapping(
        method,
        arguments,
        key=key,
        controller=controller,
        evaluate_argument=evaluate_argument,
    )


def _zip(*args):
    return CachedEvaluation(lambda: zip(*args))


def unzip(args):
    return CachedEvaluation(lambda: zip(*args))


def memoize(key=None, controller=None):
    def result(method):
        return MemoizedMethod(method, key=key, controller=controller)

    return result


def autoprint(method, key=None, controller=None):
    return AutoRun(lambda: print(method()), key=key, controller=controller)


def autopprint(method, key=None, controller=None):
    return AutoRun(lambda: pprint.pprint(method()), key=key, controller=controller)


def create_observable(value=None, key=None, controller: Optional["Controller"] = None):
    return OBSERVABLE_TYPES.get(type(value), ObservableValue)(value, key=key, controller=controller)


def create_async_generator(async_gen, initial_value):
    return AsyncGenerator(async_gen, create_observable(initial_value))


def autorun(method, key=None, controller=None):
    return AutoRun(method, key=key, controller=controller)
