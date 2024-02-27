from render import Component, create_callback, Props


class Dialog(Component):
    Module = "mantine"
    JSXName = "Dialog"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "keepMounted",
        "opened",
        "portalProps",
        "position",
        "radius",
        "shadow",
        "size",
        "transitionProps",
        "withBorder",
        "withCloseButton",
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
        keepMounted=None,
        onClose=None,
        opened=None,
        portalProps=None,
        position=None,
        radius=None,
        shadow=None,
        size=None,
        transitionProps=None,
        withBorder=None,
        withCloseButton=None,
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
        self.keepMounted = keepMounted
        self.onClose = create_callback(onClose, "onClose")
        self.opened = opened
        self.portalProps = portalProps
        self.position = position
        self.radius = radius
        self.shadow = shadow
        self.size = size
        self.transitionProps = transitionProps
        self.withBorder = withBorder
        self.withCloseButton = withCloseButton
        self.withinPortal = withinPortal
        self.zIndex = zIndex
