from render import Component, create_callback, InputComponent, Props


class Tooltip(InputComponent):
    Module = "mantine/core"
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
        "component",
        "disabled",
        "events",
        "floatingStrategy",
        "h",
        "href",
        "inline",
        "keepMounted",
        "label",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "multiline",
        "mx",
        "my",
        "offset",
        "openDelay",
        "p",
        "pb",
        "pe",
        "pl",
        "portalProps",
        "position",
        "positionDependencies",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "refProp",
        "sx",
        "ta",
        "target",
        "title",
        "transitionProps",
        "variant",
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
        arrowOffset=None,
        arrowPosition=None,
        arrowRadius=None,
        arrowSize=None,
        closeDelay=None,
        color=None,
        component=None,
        disabled=None,
        events=None,
        floatingStrategy=None,
        h=None,
        href=None,
        inline=None,
        keepMounted=None,
        label=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        multiline=None,
        mx=None,
        my=None,
        offset=None,
        onPositionChange=None,
        openDelay=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        portalProps=None,
        position=None,
        positionDependencies=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        refProp=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        transitionProps=None,
        variant=None,
        withArrow=None,
        withinPortal=None,
        zIndex=None,
        controller=None,
        onChange=None,
        opened=None,
        defaultOpened=None,
    ):
        super().__init__(key, controller, children, onChange, opened, defaultOpened)
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
        self.component = component
        self.disabled = disabled
        self.events = events
        self.floatingStrategy = floatingStrategy
        self.h = h
        self.href = href
        self.inline = inline
        self.keepMounted = keepMounted
        self.label = label
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.multiline = multiline
        self.mx = mx
        self.my = my
        self.offset = offset
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.openDelay = openDelay
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.portalProps = portalProps
        self.position = position
        self.positionDependencies = positionDependencies
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.refProp = refProp
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.transitionProps = transitionProps
        self.variant = variant
        self.withArrow = withArrow
        self.withinPortal = withinPortal
        self.zIndex = zIndex
