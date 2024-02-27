from render import Component, create_callback


class Blockquote(Component):
    Module = "mantine"
    JSXName = "Blockquote"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "cite",
        "color",
        "icon",
        "iconSize",
        "radius",
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
        cite=None,
        color=None,
        icon=None,
        iconSize=None,
        radius=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.cite = cite
        self.color = color
        self.icon = icon
        self.iconSize = iconSize
        self.radius = radius
