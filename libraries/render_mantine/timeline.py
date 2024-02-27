from render import Component, create_callback


class Timeline(Component):
    Module = "mantine"
    JSXName = "Timeline"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "align",
        "autoContrast",
        "bulletSize",
        "color",
        "lineWidth",
        "radius",
        "reverseActive",
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
        active=None,
        align=None,
        autoContrast=None,
        bulletSize=None,
        color=None,
        lineWidth=None,
        radius=None,
        reverseActive=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.active = active
        self.align = align
        self.autoContrast = autoContrast
        self.bulletSize = bulletSize
        self.color = color
        self.lineWidth = lineWidth
        self.radius = radius
        self.reverseActive = reverseActive

    class Item(Component):
        Module = "mantine"
        JSXName = "Timeline.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "bullet",
            "color",
            "lineVariant",
            "radius",
            "title",
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
            bullet=None,
            color=None,
            lineVariant=None,
            radius=None,
            title=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.bullet = bullet
            self.color = color
            self.lineVariant = lineVariant
            self.radius = radius
            self.title = title
