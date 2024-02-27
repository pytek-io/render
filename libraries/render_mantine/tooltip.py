from render import Component, create_callback, InputComponent, Props


class Tooltip(InputComponent):
    Module = "mantine"
    JSXName = "Tooltip"
    InputName = "opened"
    CALLBACKS = ["onKeyPress", "onClick", "onPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "arrowOffset",
        "arrowPosition",
        "arrowRadius",
        "arrowSize",
        "closeDelay",
        "color",
        "disabled",
        "events",
        "inline",
        "keepMounted",
        "label",
        "multiline",
        "offset",
        "openDelay",
        "portalProps",
        "position",
        "positionDependencies",
        "radius",
        "refProp",
        "transitionProps",
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
        closeDelay=None,
        color=None,
        disabled=None,
        events=None,
        inline=None,
        keepMounted=None,
        label=None,
        multiline=None,
        offset=None,
        onPositionChange=None,
        openDelay=None,
        portalProps=None,
        position=None,
        positionDependencies=None,
        radius=None,
        refProp=None,
        transitionProps=None,
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
        self.closeDelay = closeDelay
        self.color = color
        self.disabled = disabled
        self.events = events
        self.inline = inline
        self.keepMounted = keepMounted
        self.label = label
        self.multiline = multiline
        self.offset = offset
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.openDelay = openDelay
        self.portalProps = portalProps
        self.position = position
        self.positionDependencies = positionDependencies
        self.radius = radius
        self.refProp = refProp
        self.transitionProps = transitionProps
        self.withArrow = withArrow
        self.withinPortal = withinPortal
        self.zIndex = zIndex
