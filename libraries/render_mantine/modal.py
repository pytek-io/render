from render import Component, create_callback, Props


class Modal(Component):
    Module = "mantine"
    JSXName = "Modal"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "centered",
        "closeButtonProps",
        "closeOnClickOutside",
        "closeOnEscape",
        "fullScreen",
        "keepMounted",
        "lockScroll",
        "opened",
        "overlayProps",
        "padding",
        "portalProps",
        "radius",
        "removeScrollProps",
        "returnFocus",
        "scrollAreaComponent",
        "shadow",
        "size",
        "title",
        "transitionProps",
        "trapFocus",
        "withCloseButton",
        "withOverlay",
        "withinPortal",
        "xOffset",
        "yOffset",
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
        centered=None,
        closeButtonProps=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        fullScreen=None,
        keepMounted=None,
        lockScroll=None,
        onClose=None,
        opened=None,
        overlayProps=None,
        padding=None,
        portalProps=None,
        radius=None,
        removeScrollProps=None,
        returnFocus=None,
        scrollAreaComponent=None,
        shadow=None,
        size=None,
        title=None,
        transitionProps=None,
        trapFocus=None,
        withCloseButton=None,
        withOverlay=None,
        withinPortal=None,
        xOffset=None,
        yOffset=None,
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
        self.centered = centered
        self.closeButtonProps = closeButtonProps
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.fullScreen = fullScreen
        self.keepMounted = keepMounted
        self.lockScroll = lockScroll
        self.onClose = create_callback(onClose, "onClose")
        self.opened = opened
        self.overlayProps = overlayProps
        self.padding = padding
        self.portalProps = portalProps
        self.radius = radius
        self.removeScrollProps = removeScrollProps
        self.returnFocus = returnFocus
        self.scrollAreaComponent = scrollAreaComponent
        self.shadow = shadow
        self.size = size
        self.title = title
        self.transitionProps = transitionProps
        self.trapFocus = trapFocus
        self.withCloseButton = withCloseButton
        self.withOverlay = withOverlay
        self.withinPortal = withinPortal
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.zIndex = zIndex

    class sProvider(Component):
        Module = "mantine"
        JSXName = "Modal.sProvider"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "labels", "modalProps", "modals"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            labels=None,
            modalProps=None,
            modals=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.labels = labels
            self.modalProps = modalProps
            self.modals = modals
