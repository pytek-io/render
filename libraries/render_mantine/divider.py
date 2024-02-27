from render import Component, create_callback


class Divider(Component):
    Module = "mantine"
    JSXName = "Divider"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "label",
        "labelPosition",
        "orientation",
        "size",
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
        color=None,
        label=None,
        labelPosition=None,
        orientation=None,
        size=None,
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
        self.label = label
        self.labelPosition = labelPosition
        self.orientation = orientation
        self.size = size
