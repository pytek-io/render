from render import Component, create_callback


class Timeline(Component):
    Module = "antd"
    JSXName = "Timeline"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "items",
        "mode",
        "pending",
        "pendingDot",
        "reverse",
    ]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        items=None,
        mode=None,
        pending=None,
        pendingDot=None,
        reverse=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.items = items
        self.mode = mode
        self.pending = pending
        self.pendingDot = pendingDot
        self.reverse = reverse
