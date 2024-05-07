import traceback

import anyio

from ..common import CURRENT_TASK_GROUP
from .observability import Observable, ObserverBase
from ..utils import safe_execute_async


class AsyncCachedEvaluation(ObserverBase):
    def __init__(
        self,
        method,
        task_group=None,
        loading_value=None,
        reset_value=True,
        key=None,
        controller=None,
        error_constructor=None,
    ):
        super().__init__(key=key, controller=controller)
        self.method = method
        self.task_group = task_group or CURRENT_TASK_GROUP.get()
        self.current_value = Observable(loading_value)
        self.is_evaluating = False
        self.is_stale = True
        self.loading_value = loading_value
        self.reset_value = reset_value
        self.error_constructor = error_constructor

    @safe_execute_async
    async def evaluate_async(self):
        if self.is_evaluating:
            return
        self.is_evaluating = True
        with self.register_as_current_observer():
            try:
                result = await self.method()
            except anyio.get_cancelled_exc_class():
                raise
            except:  # noqa E722
                result = traceback.format_exc()
                if self.error_constructor:
                    result = self.error_constructor(result)
            self.current_value.value = result
            # FIXME: this won't work with in controlled mode ?
            self.is_evaluating = False
            self.is_stale = False

    def __call__(self):
        if self.is_stale:
            self.task_group.start_soon(self.evaluate_async)
        return self.current_value()

    def notify(self):
        self.is_stale = True
        if self.reset_value and not self.is_evaluating:
            self.current_value.value = self.loading_value


class AsyncGenerator:
    def __init__(self, async_generator, initial_value=None):
        self._value = Observable(initial_value)

        async def update():
            async for value in async_generator():
                self._value.value = value

        get_window().task_group.start_soon(safe_execute_async(update))

    def __call__(self):
        return self._value()
