from __future__ import annotations

from contextvars import ContextVar
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .window import Window
    from .reactor.controller import Controller

MESSAGE_TO_CLIENT = 1
SESSION_END = 2
SUBSCRIBE_TO_KERNEL_UPDATES = 3


CURRENT_CONTROLLER = ContextVar("CURRENT_CONTROLLER", default=None)
CURRENT_WINDOW = ContextVar("CURRENT_WINDOW", default=None)
CURRENT_TASK_GROUP = ContextVar("CURRENT_TASK_GROUP", default=None)
OUT_OF_SESSION_ERROR = "Trying to access current window out of a session."


def get_current_controller() -> Controller:
    if controller := CURRENT_CONTROLLER.get():
        return controller
    raise Exception("no controller set")


def get_window(throw_if_none=True) -> Window:
    maybe_window = CURRENT_WINDOW.get()
    if maybe_window is None:
        if throw_if_none:
            raise Exception(OUT_OF_SESSION_ERROR)
    else:
        return maybe_window()


def call_if_callable(maybe_callable):
    return maybe_callable() if callable(maybe_callable) else maybe_callable


def schedule_callback(delay: int, callback):
    get_window().schedule_callback(delay, callback)
