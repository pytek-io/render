import contextlib

from render_html import label

from render.common import call_if_callable, get_window
from render.components import JSMethod
from render.props import Container

from ._auto import *
from .input import Input as InputBase
from .input import Password as InputPassword, Group as InputGroup
from .input import Search as InputSearchBase
from .input import TextArea as InputTextAreaBase
from .list import List as ListBase, Item as ListItem
from .anchor import Anchor as AnchorBase, Link as AnchorLink
from .auto_complete import AutoComplete as AutoCompleteBase
from .avatar import Avatar as AvatarBase, Group as AvatarGroup
from .badge import Badge as BadgeBase, Ribbon as BadgeRibbon
from .button import Button as ButtonBase
from .card import Card as CardBase, Grid as CardGrid
from .checkbox import Checkbox as CheckboxBase, Group as CheckboxGroup
from .collapse import Collapse as CollapseBase, Panel as CollapsePanel
from .date_picker import DatePicker as DatePickerBase
from .date_picker import RangePicker as DateRangePicker
from .descriptions import Descriptions as DescriptionsBase, Item as DescriptionsItem
from .dropdown import Dropdown as DropdownBase, Button as DropdownButton
from .empty import Empty
from .float_button import (
    FloatButton as FloatButtonBase,
    Group as FloatButtonGroup,
    BackTop as FloatButtonBackTop,
)
from .form import Form as BaseForm, Item as FormItem, List as FormList
from .grid import Col, Row
from .image import Image as ImageBase
from .input_number import InputNumber as InputNumberBase
from .layout import (
    Layout as LayoutBase,
    Content as LayoutContent,
    Footer as LayoutFooter,
    Header as LayoutHeader,
    Sider as LayoutSider,
)
from .modal import Modal as ModalBase
from .radio import Radio as RadioBase, Group as RadioGroup
from .statistic import Statistic as StatisticBase, Countdown as StatisticCountdown
from .table import Table
from .time_picker import RangePicker as TimeRangePicker
from .time_picker import TimePicker as TimePickerBase
from .tree import Tree as TreeBase
from .tree import TreeNode as TreeNodeBase
from .tree_select import TreeSelect as TreeSelectBase, TreeNode as TreeSelectTreeNode
from .typography import (
    Link as TypographyLink,
    Paragraph as TypographyParagraph,
    Text as TypographyText,
    Title as TypographyTitle,
)


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


class notification:
    open = create_method_call("notification", "open")
    info = create_method_call("notification", "info")
    success = create_method_call("notification", "success")
    warning = create_method_call("notification", "warning")
    error = create_method_call("notification", "error")
    close = create_method_call("notification", "close")


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


class PreviewGroup(Container):
    Module = "ant"
    JSXName = "Image.PreviewGroup"


class Image(ImageBase):
    PreviewGroup = PreviewGroup


Table.SELECTION_ALL = "SELECT_ALL"
Table.SELECTION_INVERT = "SELECT_INVERT"
Table.SELECTION_NONE = "SELECT_NONE"


class Avatar(AvatarBase):
    Group = AvatarGroup


class Collapse(CollapseBase):
    Panel = CollapsePanel


class Descriptions(DescriptionsBase):
    Item = DescriptionsItem


class Badge(BadgeBase):
    Ribbon = BadgeRibbon


class Button(ButtonBase):
    class Group(Container):
        JSXName = "Button.Group"
        Module = "ant"


class List(ListBase):
    Item = ListItem


class Statistic(StatisticBase):
    Countdown = StatisticCountdown


class Anchor(AnchorBase):
    Link = AnchorLink


class Form(BaseForm):
    Item = FormItem
    List = FormList

    async def resetFields(self):
        return await self.call_method("resetFields")

    async def getFieldsValue(self):
        return await self.call_method("getFieldsValue")

    async def setFieldsValue(self, values):
        return await self.call_method("setFieldsValue", (values,))


class Checkbox(CheckboxBase):
    NewValuePath = "target.checked"
    Group = CheckboxGroup


class DatePicker(DatePickerBase):
    class RangePicker(DateRangePicker):
        pass


class TimePicker(TimePickerBase):
    class RangePicker(TimeRangePicker):
        pass


Empty.PRESENTED_IMAGE_SIMPLE = "PRESENTED_IMAGE_SIMPLE"


class Card(CardBase):
    Grid = CardGrid


class TreeSelect(TreeSelectBase):
    SHOW_PARENT = "SHOW_PARENT"
    SHOW_ALL = "SHOW_ALL"
    SHOW_CHILD = "SHOW_CHILD"
    TreeNode = TreeSelectTreeNode


# DirectoryTree.JSXName = "Tree.DirectoryTree"


# class Tree(TreeBase):
#     DirectoryTree = DirectoryTree

#     class TreeNode(TreeNodeBase):
#         JSXName = "TreeTreeNode"
#         DirectoryTree = DirectoryTree


class Dropdown(DropdownBase):
    Button = DropdownButton


class Layout(LayoutBase):
    class Header(LayoutHeader):
        JSXName = "Layout.Header"

    class Content(LayoutContent):
        JSXName = "Layout.Content"

    class Footer(LayoutFooter):
        JSXName = "Layout.Footer"

    class Sider(LayoutSider):
        JSXName = "Layout.Sider"


class Radio(RadioBase):
    NewValuePath = "target.checked"

    class Group(RadioGroup):
        NewValuePath = "target.value"

    class Button(RadioBase):
        NewValuePath = "target.checked"


class Typography(TypographyText):
    Link = TypographyLink
    Title = TypographyTitle
    Paragraph = TypographyParagraph
    Text = TypographyText


class InputSearch(InputSearchBase):
    Search = NewValuePath = ""


class InputTextArea(InputTextAreaBase):
    NewValuePath = "target.value"


class Input(InputBase):
    NewValuePath = "target.value"
    Password = InputPassword
    Search = InputSearch
    TextArea = InputTextArea
    Group = InputGroup


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


class FloatButton(FloatButtonBase):
    Group = FloatButtonGroup
    BackTop = FloatButtonBackTop


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
