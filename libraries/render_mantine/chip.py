from render import Component, create_callback, InputComponent, Props


class Chip(InputComponent):
    Module = "mantine"
    JSXName = "Chip"
    InputName = "checked"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "icon",
        "radius",
        "rootRef",
        "size",
        "type",
        "wrapperProps",
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
        onChange=None,
        defaultChecked=None,
        checked=None,
        autoContrast=None,
        color=None,
        icon=None,
        radius=None,
        rootRef=None,
        size=None,
        type=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.icon = icon
        self.radius = radius
        self.rootRef = rootRef
        self.size = size
        self.type = type
        self.wrapperProps = wrapperProps

    class Group(InputComponent):
        Module = "mantine"
        JSXName = "Chip.Group"
        InputName = "value"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "multiple"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            onChange=None,
            defaultValue=None,
            value=None,
            multiple=None,
            controller=None,
        ):
            super().__init__(key, controller, onChange, value, defaultValue)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.multiple = multiple
