from render import Component, create_callback


class Accordion(Component):
    Module = "mantine"
    JSXName = "Accordion"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "chevron",
        "chevronPosition",
        "chevronSize",
        "defaultValue",
        "disableChevronRotation",
        "loop",
        "multiple",
        "order",
        "radius",
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
        chevron=None,
        chevronPosition=None,
        chevronSize=None,
        defaultValue=None,
        disableChevronRotation=None,
        loop=None,
        multiple=None,
        onChange=None,
        order=None,
        radius=None,
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
        self.chevron = chevron
        self.chevronPosition = chevronPosition
        self.chevronSize = chevronSize
        self.defaultValue = defaultValue
        self.disableChevronRotation = disableChevronRotation
        self.loop = loop
        self.multiple = multiple
        self.onChange = create_callback(onChange, "onChange")
        self.order = order
        self.radius = radius
        self.transitionDuration = transitionDuration
        self.value = value

    class Chevron(Component):
        Module = "mantine"
        JSXName = "Accordion.Chevron"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "size"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
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
            self.size = size

    class Control(Component):
        Module = "mantine"
        JSXName = "Accordion.Control"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "chevron", "disabled", "icon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            chevron=None,
            disabled=None,
            icon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.chevron = chevron
            self.disabled = disabled
            self.icon = icon

    class Item(Component):
        Module = "mantine"
        JSXName = "Accordion.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "value"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
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
            self.value = value

    class Panel(Component):
        Module = "mantine"
        JSXName = "Accordion.Panel"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
