from render import Component, create_callback, add_data_namespace, Props


class Avatar(Component):
    Module = "mantine"
    JSXName = "Avatar"
    CALLBACKS = ["onKeyPress", "onClick"]
    DATA = ["src"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alt",
        "autoContrast",
        "color",
        "gradient",
        "imageProps",
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
        alt=None,
        autoContrast=None,
        color=None,
        gradient=None,
        imageProps=None,
        radius=None,
        size=None,
        src=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alt = alt
        self.autoContrast = autoContrast
        self.color = color
        self.gradient = gradient
        self.imageProps = imageProps
        self.radius = radius
        self.size = size
        self.src = add_data_namespace(src)
