from render import Component, create_callback


class CloseButton(Component):
    Module = "mantine"
    JSXName = "CloseButton"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "disabled",
        "icon",
        "iconSize",
        "radius",
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
        disabled=None,
        icon=None,
        iconSize=None,
        radius=None,
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
        self.disabled = disabled
        self.icon = icon
        self.iconSize = iconSize
        self.radius = radius
        self.size = size
