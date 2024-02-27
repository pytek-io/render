from render import Component, create_callback


class Overlay(Component):
    Module = "mantine"
    JSXName = "Overlay"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "backgroundOpacity",
        "blur",
        "center",
        "color",
        "fixed",
        "gradient",
        "radius",
        "zIndex",
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
        backgroundOpacity=None,
        blur=None,
        center=None,
        color=None,
        fixed=None,
        gradient=None,
        radius=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.backgroundOpacity = backgroundOpacity
        self.blur = blur
        self.center = center
        self.color = color
        self.fixed = fixed
        self.gradient = gradient
        self.radius = radius
        self.zIndex = zIndex
