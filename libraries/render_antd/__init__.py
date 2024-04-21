import contextlib
import render as r


from render.common import get_window

from ._auto import *
from .auto_complete import AutoComplete as AutoCompleteBase
from .input_number import InputNumber as InputNumberBase
from .modal import Modal as ModalBase
from .upload import Upload as UploadBase

from .form import Form as BaseForm
from .grid import Col, Row

DATE_FORMAT = "dayjs"


def create_row(elements, col_kwargs={}, gutter=10, align="middle", **kwargs):
    return Row(
        [Col(element, **col_kwargs) for element in elements],
        gutter=gutter,
        align=align,
        **kwargs,
    )


def create_method_call(js_method):
    def result(*args):
        get_window().call_js_method(js_method(*args))

    return result


class notification:
    open = create_method_call(r.js_arrow("notification_open", "render_antd.notification.open"))
    info = create_method_call(r.js_arrow("notification_info", "render_antd.notification.info"))
    success = create_method_call(
        r.js_arrow("notification_success", "render_antd.notification.success")
    )
    warning = create_method_call(
        r.js_arrow("notification_warning", "render_antd.notification.warning")
    )
    error = create_method_call(r.js_arrow("notification_error", "render_antd.notification.error"))
    destroy = create_method_call(
        r.js_arrow("notification_destroy", "render_antd.notification.destroy")
    )


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
    loading = create_method_call(r.js_arrow("message_loading", "render_antd.message.loading"))
    open = create_method_call(r.js_arrow("message_open", "render_antd.message.open"))
    info = create_method_call(r.js_arrow("message_info", "render_antd.message.info"))
    success = create_method_call(r.js_arrow("message_success", "render_antd.message.success"))
    warning = create_method_call(r.js_arrow("message_warning", "render_antd.message.warning"))
    error = create_method_call(r.js_arrow("message_error", "render_antd.message.error"))
    destroy = create_method_call(r.js_arrow("message_destroy", "render_antd.message.destroy"))


class Modal(ModalBase):
    confirm = create_method_call(r.js_arrow("modal_confirm", "render_antd.Modal.confirm"))


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


class Wrapper:
    """Wrapper to make can be weakreferred."""
    def __init__(self, method):
        self.method = method

    def __call__(self, *args):
        return self.method(*args)


class Upload(UploadBase):
    def initialize_hidden_arguments(self):
        window = r.get_window()
        self._value = r.ObservableDict()
        self.update_value = Wrapper(self._value.__setitem__)
        callback_id = id(self.update_value)
        window.callbacks[callback_id] = self.update_value
        self.action = f"/post?kernel={window.kernel.kernel_id}&session={window.session_id}&callback={callback_id}"
