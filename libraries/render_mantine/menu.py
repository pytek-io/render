from render import Component, create_callback, InputComponent, Props


class Menu(InputComponent):
    Module = "mantine"
    JSXName = "Menu"
    InputName = "opened"
    CALLBACKS = ["onKeyPress", "onClick", "onClose", "onOpen", "onPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "arrowOffset",
        "arrowPosition",
        "arrowRadius",
        "arrowSize",
        "clickOutsideEvents",
        "closeDelay",
        "closeOnClickOutside",
        "closeOnEscape",
        "closeOnItemClick",
        "disabled",
        "keepMounted",
        "loop",
        "menuItemTabIndex",
        "middlewares",
        "offset",
        "openDelay",
        "portalProps",
        "position",
        "positionDependencies",
        "radius",
        "returnFocus",
        "shadow",
        "transitionProps",
        "trapFocus",
        "trigger",
        "width",
        "withArrow",
        "withinPortal",
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
        onChange=None,
        defaultOpened=None,
        opened=None,
        arrowOffset=None,
        arrowPosition=None,
        arrowRadius=None,
        arrowSize=None,
        clickOutsideEvents=None,
        closeDelay=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        closeOnItemClick=None,
        disabled=None,
        keepMounted=None,
        loop=None,
        menuItemTabIndex=None,
        middlewares=None,
        offset=None,
        onClose=None,
        onOpen=None,
        onPositionChange=None,
        openDelay=None,
        portalProps=None,
        position=None,
        positionDependencies=None,
        radius=None,
        returnFocus=None,
        shadow=None,
        transitionProps=None,
        trapFocus=None,
        trigger=None,
        width=None,
        withArrow=None,
        withinPortal=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, opened, defaultOpened)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.arrowOffset = arrowOffset
        self.arrowPosition = arrowPosition
        self.arrowRadius = arrowRadius
        self.arrowSize = arrowSize
        self.clickOutsideEvents = clickOutsideEvents
        self.closeDelay = closeDelay
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.closeOnItemClick = closeOnItemClick
        self.disabled = disabled
        self.keepMounted = keepMounted
        self.loop = loop
        self.menuItemTabIndex = menuItemTabIndex
        self.middlewares = middlewares
        self.offset = offset
        self.onClose = create_callback(onClose, "onClose")
        self.onOpen = create_callback(onOpen, "onOpen")
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.openDelay = openDelay
        self.portalProps = portalProps
        self.position = position
        self.positionDependencies = positionDependencies
        self.radius = radius
        self.returnFocus = returnFocus
        self.shadow = shadow
        self.transitionProps = transitionProps
        self.trapFocus = trapFocus
        self.trigger = trigger
        self.width = width
        self.withArrow = withArrow
        self.withinPortal = withinPortal
        self.zIndex = zIndex

    class Divider(Component):
        Module = "mantine"
        JSXName = "Menu.Divider"
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

    class Dropdown(Component):
        Module = "mantine"
        JSXName = "Menu.Dropdown"
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

    class Item(Component):
        Module = "mantine"
        JSXName = "Menu.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "closeMenuOnClick",
            "color",
            "disabled",
            "leftSection",
            "rightSection",
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
            closeMenuOnClick=None,
            color=None,
            disabled=None,
            leftSection=None,
            rightSection=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.closeMenuOnClick = closeMenuOnClick
            self.color = color
            self.disabled = disabled
            self.leftSection = leftSection
            self.rightSection = rightSection

    class Label(Component):
        Module = "mantine"
        JSXName = "Menu.Label"
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

    class Target(Component):
        Module = "mantine"
        JSXName = "Menu.Target"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "refProp"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            refProp=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.refProp = refProp
