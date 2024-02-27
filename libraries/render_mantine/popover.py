from render import Component, create_callback, InputComponent, Props


class Popover(InputComponent):
    Module = "mantine"
    JSXName = "Popover"
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
        "closeOnClickOutside",
        "closeOnEscape",
        "disabled",
        "keepMounted",
        "middlewares",
        "offset",
        "portalProps",
        "position",
        "positionDependencies",
        "radius",
        "returnFocus",
        "shadow",
        "transitionProps",
        "trapFocus",
        "width",
        "withArrow",
        "withRoles",
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
        closeOnClickOutside=None,
        closeOnEscape=None,
        disabled=None,
        keepMounted=None,
        middlewares=None,
        offset=None,
        onClose=None,
        onOpen=None,
        onPositionChange=None,
        portalProps=None,
        position=None,
        positionDependencies=None,
        radius=None,
        returnFocus=None,
        shadow=None,
        transitionProps=None,
        trapFocus=None,
        width=None,
        withArrow=None,
        withRoles=None,
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
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.disabled = disabled
        self.keepMounted = keepMounted
        self.middlewares = middlewares
        self.offset = offset
        self.onClose = create_callback(onClose, "onClose")
        self.onOpen = create_callback(onOpen, "onOpen")
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.portalProps = portalProps
        self.position = position
        self.positionDependencies = positionDependencies
        self.radius = radius
        self.returnFocus = returnFocus
        self.shadow = shadow
        self.transitionProps = transitionProps
        self.trapFocus = trapFocus
        self.width = width
        self.withArrow = withArrow
        self.withRoles = withRoles
        self.withinPortal = withinPortal
        self.zIndex = zIndex

    class Dropdown(Component):
        Module = "mantine"
        JSXName = "Popover.Dropdown"
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
        JSXName = "Popover.Target"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "popupType", "refProp"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            popupType=None,
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
            self.popupType = popupType
            self.refProp = refProp
