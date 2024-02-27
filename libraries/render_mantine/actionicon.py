from render import Component, create_callback, Props


class ActionIcon(Component):
    Module = "mantine"
    JSXName = "ActionIcon"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "disabled",
        "gradient",
        "loaderProps",
        "loading",
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
        disabled=None,
        gradient=None,
        loaderProps=None,
        loading=None,
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
        self.disabled = disabled
        self.gradient = gradient
        self.loaderProps = loaderProps
        self.loading = loading
        self.radius = radius
        self.size = size

    class Group(Component):
        Module = "mantine"
        JSXName = "ActionIcon.Group"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "borderWidth", "orientation"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            borderWidth=None,
            orientation=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.borderWidth = borderWidth
            self.orientation = orientation
