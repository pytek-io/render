from render import Component, create_callback, Props


class Drawer(Component):
    Module = "mantine"
    JSXName = "Drawer"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeButtonProps",
        "closeOnClickOutside",
        "closeOnEscape",
        "keepMounted",
        "lockScroll",
        "offset",
        "opened",
        "overlayProps",
        "padding",
        "portalProps",
        "position",
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
        closeButtonProps=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        keepMounted=None,
        lockScroll=None,
        offset=None,
        onClose=None,
        opened=None,
        overlayProps=None,
        padding=None,
        portalProps=None,
        position=None,
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
        self.closeButtonProps = closeButtonProps
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.keepMounted = keepMounted
        self.lockScroll = lockScroll
        self.offset = offset
        self.onClose = create_callback(onClose, "onClose")
        self.opened = opened
        self.overlayProps = overlayProps
        self.padding = padding
        self.portalProps = portalProps
        self.position = position
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
        self.zIndex = zIndex
