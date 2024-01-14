from contextvars import ContextVar

MessageToClient = 1
SessionEnd = 2
SubscribeToKernelUpdates = 3


CURRENT_CONTROLLER = ContextVar("CURRENT_CONTROLLER", default=None)
CURRENT_WINDOW = ContextVar("CURRENT_WINDOW", default=None)
OUT_OF_SESSION_ERROR = "Trying to access current window out of a session."


def get_current_controller():
    if controller := CURRENT_CONTROLLER.get():
        return controller
    raise Exception("no controller set")


def get_window(throw_if_none=True):
    maybe_window = CURRENT_WINDOW.get()
    if maybe_window is None:
        if throw_if_none:
            raise Exception(OUT_OF_SESSION_ERROR)
    else:
        return maybe_window()


def call_if_callable(maybe_callable):
    return maybe_callable() if callable(maybe_callable) else maybe_callable
