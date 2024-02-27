from render import Component, create_callback


class ThemeIcon(Component):
    Module = "mantine"
    JSXName = "ThemeIcon"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "gradient",
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
        autoContrast=None,
        color=None,
        gradient=None,
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
        self.autoContrast = autoContrast
        self.color = color
        self.gradient = gradient
        self.radius = radius
        self.size = size
