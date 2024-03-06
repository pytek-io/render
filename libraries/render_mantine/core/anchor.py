from render import Component, create_callback


class Anchor(Component):
    Module = "mantine/core"
    JSXName = "Anchor"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "component",
        "gradient",
        "h",
        "href",
        "inherit",
        "inline",
        "lineClamp",
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
        "size",
        "sx",
        "ta",
        "target",
        "truncate",
        "underline",
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
        color=None,
        component=None,
        gradient=None,
        h=None,
        href=None,
        inherit=None,
        inline=None,
        lineClamp=None,
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
        size=None,
        sx=None,
        ta=None,
        target=None,
        truncate=None,
        underline=None,
        variant=None,
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
        self.gradient = gradient
        self.h = h
        self.href = href
        self.inherit = inherit
        self.inline = inline
        self.lineClamp = lineClamp
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
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.truncate = truncate
        self.underline = underline
        self.variant = variant
