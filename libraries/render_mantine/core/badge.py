from render import Component, create_callback


class Badge(Component):
    Module = "mantine/core"
    JSXName = "Badge"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "circle",
        "color",
        "component",
        "fullWidth",
        "gradient",
        "h",
        "href",
        "leftSection",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "rightSection",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
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
        autoContrast=None,
        circle=None,
        color=None,
        component=None,
        fullWidth=None,
        gradient=None,
        h=None,
        href=None,
        leftSection=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        rightSection=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.circle = circle
        self.color = color
        self.component = component
        self.fullWidth = fullWidth
        self.gradient = gradient
        self.h = h
        self.href = href
        self.leftSection = leftSection
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.rightSection = rightSection
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
