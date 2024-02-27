from render import Component, create_callback


class Progress(Component):
    Module = "mantine"
    JSXName = "Progress"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "animated",
        "autoContrast",
        "color",
        "radius",
        "size",
        "striped",
        "transitionDuration",
        "value",
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
        animated=None,
        autoContrast=None,
        color=None,
        radius=None,
        size=None,
        striped=None,
        transitionDuration=None,
        value=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.animated = animated
        self.autoContrast = autoContrast
        self.color = color
        self.radius = radius
        self.size = size
        self.striped = striped
        self.transitionDuration = transitionDuration
        self.value = value

    class Root(Component):
        Module = "mantine"
        JSXName = "Progress.Root"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoContrast",
            "radius",
            "size",
            "transitionDuration",
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
            radius=None,
            size=None,
            transitionDuration=None,
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
            self.radius = radius
            self.size = size
            self.transitionDuration = transitionDuration

    class Section(Component):
        Module = "mantine"
        JSXName = "Progress.Section"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "animated",
            "color",
            "striped",
            "value",
            "withAria",
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
            animated=None,
            color=None,
            striped=None,
            value=None,
            withAria=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.animated = animated
            self.color = color
            self.striped = striped
            self.value = value
            self.withAria = withAria
