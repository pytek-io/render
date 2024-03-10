from render import Component, create_callback, Props


class Dialog(Component):
    Module = "mantine/core"
    JSXName = "Dialog"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "h",
        "href",
        "keepMounted",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "opened",
        "p",
        "pb",
        "pe",
        "pl",
        "portalProps",
        "position",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "shadow",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "transitionProps",
        "variant",
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
        component=None,
        h=None,
        href=None,
        keepMounted=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        onClose=None,
        opened=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        portalProps=None,
        position=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        shadow=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        transitionProps=None,
        variant=None,
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
        self.component = component
        self.h = h
        self.href = href
        self.keepMounted = keepMounted
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onClose = create_callback(onClose, "onClose")
        self.opened = opened
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.portalProps = portalProps
        self.position = position
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.shadow = shadow
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.transitionProps = transitionProps
        self.variant = variant
        self.withBorder = withBorder
        self.withCloseButton = withCloseButton
        self.withinPortal = withinPortal
        self.zIndex = zIndex
