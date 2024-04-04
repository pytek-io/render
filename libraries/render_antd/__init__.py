import contextlib

from render_html import label

from render.common import call_if_callable, get_window
from render.components import JSMethod

from ._auto import *
from .auto_complete import AutoComplete as AutoCompleteBase
from .form import Form as BaseForm
from .grid import Col, Row
from .input_number import InputNumber as InputNumberBase
from .modal import Modal as ModalBase

DATE_FORMAT = "dayjs"

def create_row(elements, col_kwargs={}, gutter=10, align="middle", **kwargs):
    return Row(
        [Col(element, **col_kwargs) for element in elements],
        gutter=gutter,
        align=align,
        **kwargs,
    )


def create_method_call(message_type, notification_type):
    def result(args, duration=None):
        if duration is not None and isinstance(args, str):
            args = [args, duration]
        get_window().call_js_method(
            "call_ant_free_function",
            [message_type, notification_type, args],
        )

    return result


class notification:
    open = create_method_call("notification", "open")
    info = create_method_call("notification", "info")
    success = create_method_call("notification", "success")
    warning = create_method_call("notification", "warning")
    error = create_method_call("notification", "error")
    close = create_method_call("notification", "close")


@contextlib.contextmanager
def create_loading_message(message_):
    key = "whatever"
    try:
        message.loading({"content": message_, "key": key})
        yield
        message_, success = f"{message_} completed!", True
    except Exception as e:
        message_, success = f"{message_} failed, {e}", False
    finally:
        (message.success if success else message.error)(
            {
                "content": message_,
                "key": key,
                "duration": 1,
            }
        )


if get_window(throw_if_none=False):
    get_window().set_notification_hook(create_loading_message)


class message:
    loading = create_method_call("message", "loading")
    info = create_method_call("message", "info")
    success = create_method_call("message", "success")
    error = create_method_call("message", "error")
    warning = create_method_call("message", "warning")


class Modal(ModalBase):
    confirm = create_method_call("Modal", "confirm")
    info = create_method_call("Modal", "info")
    success = create_method_call("Modal", "success")
    error = create_method_call("Modal", "error")
    warning = create_method_call("Modal", "warning")


class Form(BaseForm):

    async def resetFields(self):
        return await self.call_method("resetFields")

    async def getFieldsValue(self):
        return await self.call_method("getFieldsValue")

    async def setFieldsValue(self, values):
        return await self.call_method("setFieldsValue", (values,))


def flatten_options_values(options):
    for option in options:
        if "value" in option:
            yield option["value"]
        elif "options" in option:
            yield from flatten_options_values(option["options"])


class AutoComplete(AutoCompleteBase):
    def validate(self, value):
        return value in set(
            flatten_options_values(call_if_callable(self.options)) if self.options else []
        )

    @classmethod
    def case_insensitive_filter_options(cls, case_insensitive=True):
        return JSMethod(
            "filter",
            f"(inputValue, {{value}}) => value{'.toUpperCase()' if case_insensitive else ''}.indexOf(inputValue{'.toUpperCase()' if case_insensitive else ''}) !== -1",
        )


class InputNumber(InputNumberBase):
    def validate(self, new_value):
        return new_value is not None


LEFT_BREAK_POINTS = dict(xs=8, sm=6)
RIGHT_BREAK_POINTS = dict(xs=16, sm=18)


def create_form_row(label_tag, component):
    return Row(
        [
            Col(
                label(label_tag),
                className="ant-form-item-label",
                **LEFT_BREAK_POINTS,
            ),
            Col(
                component,
                className="ant-form-item-control-input-content",
                **RIGHT_BREAK_POINTS,
            ),
        ],
        align="middle",
        style={"marginTop": 10},
    )


def create_form_layout(items):
    return Col(create_form_row(label, component) for label, component in items)


def centered(content, **kwargs):
    return Row(
        content,
        justify="space-around",
        align="middle",
        **kwargs,
    )
