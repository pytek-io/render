from render import Component, create_callback


class Overlay(Component):
    Module = "mantine/core"
    JSXName = "Overlay"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "backgroundOpacity",
        "blur",
        "center",
        "color",
        "component",
        "fixed",
        "gradient",
        "h",
        "href",
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
        "sx",
        "ta",
        "target",
        "title",
        "variant",
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
        backgroundOpacity=None,
        blur=None,
        center=None,
        color=None,
        component=None,
        fixed=None,
        gradient=None,
        h=None,
        href=None,
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
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.backgroundOpacity = backgroundOpacity
        self.blur = blur
        self.center = center
        self.color = color
        self.component = component
        self.fixed = fixed
        self.gradient = gradient
        self.h = h
        self.href = href
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
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.zIndex = zIndex
