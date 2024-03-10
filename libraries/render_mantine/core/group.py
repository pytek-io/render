from render import Component, create_callback


class Group(Component):
    Module = "mantine/core"
    JSXName = "Group"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "component",
        "gap",
        "grow",
        "h",
        "href",
        "justify",
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
        "preventGrowOverflow",
        "ps",
        "pt",
        "px",
        "py",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "wrap",
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
        align=None,
        component=None,
        gap=None,
        grow=None,
        h=None,
        href=None,
        justify=None,
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
        preventGrowOverflow=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        wrap=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.component = component
        self.gap = gap
        self.grow = grow
        self.h = h
        self.href = href
        self.justify = justify
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
        self.preventGrowOverflow = preventGrowOverflow
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.wrap = wrap
