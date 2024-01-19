from render import Component, create_callback


class Divider(Component):
    Module = "ant"
    JSXName = "Divider"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "dashed",
        "orientation",
        "orientationMargin",
        "plain",
        "type",
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
        dashed=None,
        orientation=None,
        orientationMargin=None,
        plain=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.dashed = dashed
        self.orientation = orientation
        self.orientationMargin = orientationMargin
        self.plain = plain
        self.type = type
