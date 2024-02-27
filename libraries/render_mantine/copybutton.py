from render import Component, create_callback


class CopyButton(Component):
    Module = "mantine"
    JSXName = "CopyButton"
    CALLBACKS = ["children", "onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "timeout", "value"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        timeout=None,
        value=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = create_callback(children, "children")
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.timeout = timeout
        self.value = value
