from render import Component, create_callback, InputComponent


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
        "arrowSize",
        "closeDelay",
        "color",
        "disabled",
        "events",
        "inline",
        "label",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "multiline",
        "mx",
        "my",
        "offset",
        "openDelay",
        "p",
        "pb",
        "pl",
        "position",
        "positionDependencies",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "refProp",
        "sx",
        "transition",
        "transitionDuration",
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
        arrowSize=None,
        closeDelay=None,
        color=None,
        disabled=None,
        events=None,
        inline=None,
        label=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        multiline=None,
        mx=None,
        my=None,
        offset=None,
        onPositionChange=None,
        openDelay=None,
        p=None,
        pb=None,
        pl=None,
        position=None,
        positionDependencies=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        refProp=None,
        sx=None,
        transition=None,
        transitionDuration=None,
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
        self.arrowSize = arrowSize
        self.closeDelay = closeDelay
        self.color = color
        self.disabled = disabled
        self.events = events
        self.inline = inline
        self.label = label
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.multiline = multiline
        self.mx = mx
        self.my = my
        self.offset = offset
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.openDelay = openDelay
        self.p = p
        self.pb = pb
        self.pl = pl
        self.position = position
        self.positionDependencies = positionDependencies
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.refProp = refProp
        self.sx = sx
        self.transition = transition
        self.transitionDuration = transitionDuration
        self.width = width
        self.withArrow = withArrow
        self.withinPortal = withinPortal
        self.zIndex = zIndex


class TooltipFloating(Component):
    Module = "mantine"
    JSXName = "Tooltip.Floating"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "disabled",
        "label",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "multiline",
        "mx",
        "my",
        "offset",
        "p",
        "pb",
        "pl",
        "position",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "refProp",
        "sx",
        "width",
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
        color=None,
        disabled=None,
        label=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        multiline=None,
        mx=None,
        my=None,
        offset=None,
        p=None,
        pb=None,
        pl=None,
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        refProp=None,
        sx=None,
        width=None,
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
        self.color = color
        self.disabled = disabled
        self.label = label
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.multiline = multiline
        self.mx = mx
        self.my = my
        self.offset = offset
        self.p = p
        self.pb = pb
        self.pl = pl
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.refProp = refProp
        self.sx = sx
        self.width = width
        self.withinPortal = withinPortal
        self.zIndex = zIndex


class TooltipGroup(Component):
    Module = "mantine"
    JSXName = "Tooltip.Group"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeDelay",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "openDelay",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "sx",
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
        closeDelay=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        openDelay=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.closeDelay = closeDelay
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.openDelay = openDelay
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
