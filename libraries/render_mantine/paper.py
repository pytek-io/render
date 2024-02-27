from render import Component, create_callback


class Paper(Component):
    Module = "mantine"
    JSXName = "Paper"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "radius", "shadow", "withBorder"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        radius=None,
        shadow=None,
        withBorder=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.radius = radius
        self.shadow = shadow
        self.withBorder = withBorder
