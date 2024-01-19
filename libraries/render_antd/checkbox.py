from render import Component, create_callback, InputComponent


class Checkbox(InputComponent):
    Module = "antd"
    JSXName = "Checkbox"
    InputName = "checked"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "autoFocus", "disabled", "indeterminate"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        onChange=None,
        defaultChecked=None,
        checked=None,
        autoFocus=None,
        disabled=None,
        indeterminate=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoFocus = autoFocus
        self.disabled = disabled
        self.indeterminate = indeterminate


class Group(InputComponent):
    Module = "antd"
    JSXName = "Checkbox.Group"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "disabled", "name", "options"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        onChange=None,
        defaultValue=None,
        value=None,
        disabled=None,
        name=None,
        options=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.disabled = disabled
        self.name = name
        self.options = options
