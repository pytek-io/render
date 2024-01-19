from render import Component, create_callback, InputComponent


class Segmented(InputComponent):
    Module = "antd"
    JSXName = "Segmented"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "block", "disabled", "options", "size"]

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
        block=None,
        disabled=None,
        options=None,
        size=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.block = block
        self.disabled = disabled
        self.options = options
        self.size = size
