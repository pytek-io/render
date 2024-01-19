from render import Component, create_callback


class Items(Component):
    Module = "ant"
    JSXName = "Items"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "color", "dot", "label", "position"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        color=None,
        dot=None,
        label=None,
        position=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.dot = dot
        self.label = label
        self.position = position


class Timeline(Component):
    Module = "ant"
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
