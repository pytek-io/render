from render import Component, create_callback


class Card(Component):
    Module = "mantine"
    JSXName = "Card"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "padding",
        "radius",
        "shadow",
        "withBorder",
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
        padding=None,
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
        self.padding = padding
        self.radius = radius
        self.shadow = shadow
        self.withBorder = withBorder

    class Section(Component):
        Module = "mantine"
        JSXName = "Card.Section"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "inheritPadding", "withBorder"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            inheritPadding=None,
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
            self.inheritPadding = inheritPadding
            self.withBorder = withBorder
