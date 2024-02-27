from render import Component, create_callback, InputComponent


class Tabs(InputComponent):
    Module = "mantine"
    JSXName = "Tabs"
    InputCallback = "onTabChange"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "activateTabWithKeyboard",
        "allowTabDeactivation",
        "autoContrast",
        "color",
        "inverted",
        "keepMounted",
        "loop",
        "orientation",
        "placement",
        "radius",
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
        defaultValue=None,
        value=None,
        activateTabWithKeyboard=None,
        allowTabDeactivation=None,
        autoContrast=None,
        color=None,
        inverted=None,
        keepMounted=None,
        loop=None,
        orientation=None,
        placement=None,
        radius=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.activateTabWithKeyboard = activateTabWithKeyboard
        self.allowTabDeactivation = allowTabDeactivation
        self.autoContrast = autoContrast
        self.color = color
        self.inverted = inverted
        self.keepMounted = keepMounted
        self.loop = loop
        self.orientation = orientation
        self.placement = placement
        self.radius = radius

    class List(Component):
        Module = "mantine"
        JSXName = "Tabs.List"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "grow", "justify"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            grow=None,
            justify=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.grow = grow
            self.justify = justify

    class Panel(Component):
        Module = "mantine"
        JSXName = "Tabs.Panel"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "keepMounted", "value"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            keepMounted=None,
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
            self.keepMounted = keepMounted
            self.value = value

    class Tab(Component):
        Module = "mantine"
        JSXName = "Tabs.Tab"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "color",
            "leftSection",
            "rightSection",
            "size",
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
            color=None,
            leftSection=None,
            rightSection=None,
            size=None,
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
            self.color = color
            self.leftSection = leftSection
            self.rightSection = rightSection
            self.size = size
            self.value = value
