from render import Component, create_callback


class Skeleton(Component):
    Module = "mantine"
    JSXName = "Skeleton"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "animate",
        "circle",
        "height",
        "radius",
        "visible",
        "width",
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
        animate=None,
        circle=None,
        height=None,
        radius=None,
        visible=None,
        width=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.animate = animate
        self.circle = circle
        self.height = height
        self.radius = radius
        self.visible = visible
        self.width = width
