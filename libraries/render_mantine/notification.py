from render import Component, create_callback, Props


class Notification(Component):
    Module = "mantine"
    JSXName = "Notification"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeButtonProps",
        "color",
        "icon",
        "loading",
        "radius",
        "title",
        "withBorder",
        "withCloseButton",
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
        color=None,
        icon=None,
        loading=None,
        onClose=None,
        radius=None,
        title=None,
        withBorder=None,
        withCloseButton=None,
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
        self.color = color
        self.icon = icon
        self.loading = loading
        self.onClose = create_callback(onClose, "onClose")
        self.radius = radius
        self.title = title
        self.withBorder = withBorder
        self.withCloseButton = withCloseButton

    class s(Component):
        Module = "mantine"
        JSXName = "Notification.s"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoClose",
            "containerWidth",
            "limit",
            "notificationMaxHeight",
            "portalProps",
            "position",
            "store",
            "transitionDuration",
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
            autoClose=None,
            containerWidth=None,
            limit=None,
            notificationMaxHeight=None,
            portalProps=None,
            position=None,
            store=None,
            transitionDuration=None,
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
            self.autoClose = autoClose
            self.containerWidth = containerWidth
            self.limit = limit
            self.notificationMaxHeight = notificationMaxHeight
            self.portalProps = portalProps
            self.position = position
            self.store = store
            self.transitionDuration = transitionDuration
            self.withinPortal = withinPortal
            self.zIndex = zIndex
