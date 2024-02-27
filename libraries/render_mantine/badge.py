from render import Component, create_callback


class Badge(Component):
    Module = "mantine"
    JSXName = "Badge"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "circle",
        "color",
        "fullWidth",
        "gradient",
        "leftSection",
        "radius",
        "rightSection",
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
        circle=None,
        color=None,
        fullWidth=None,
        gradient=None,
        leftSection=None,
        radius=None,
        rightSection=None,
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
        self.circle = circle
        self.color = color
        self.fullWidth = fullWidth
        self.gradient = gradient
        self.leftSection = leftSection
        self.radius = radius
        self.rightSection = rightSection
        self.size = size
