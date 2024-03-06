from render import Component, create_callback, Props


class NavigationProgress(Component):
    Module = "mantine/nprogress"
    JSXName = "NavigationProgress"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "component",
        "h",
        "href",
        "initialProgress",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "portalProps",
        "pr",
        "pt",
        "px",
        "py",
        "size",
        "stepInterval",
        "store",
        "sx",
        "ta",
        "target",
        "variant",
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
        component=None,
        h=None,
        href=None,
        initialProgress=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pl=None,
        portalProps=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        stepInterval=None,
        store=None,
        sx=None,
        ta=None,
        target=None,
        variant=None,
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
        self.component = component
        self.h = h
        self.href = href
        self.initialProgress = initialProgress
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pl = pl
        self.portalProps = portalProps
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.stepInterval = stepInterval
        self.store = store
        self.sx = sx
        self.ta = ta
        self.target = target
        self.variant = variant
        self.withinPortal = withinPortal
        self.zIndex = zIndex
