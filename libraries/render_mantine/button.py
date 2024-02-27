from render import Component, create_callback, Props


class Button(Component):
    Module = "mantine"
    JSXName = "Button"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "disabled",
        "fullWidth",
        "gradient",
        "justify",
        "leftSection",
        "loaderProps",
        "loading",
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
        color=None,
        disabled=None,
        fullWidth=None,
        gradient=None,
        justify=None,
        leftSection=None,
        loaderProps=None,
        loading=None,
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
        self.color = color
        self.disabled = disabled
        self.fullWidth = fullWidth
        self.gradient = gradient
        self.justify = justify
        self.leftSection = leftSection
        self.loaderProps = loaderProps
        self.loading = loading
        self.radius = radius
        self.rightSection = rightSection
        self.size = size

    class Group(Component):
        Module = "mantine"
        JSXName = "Button.Group"
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
