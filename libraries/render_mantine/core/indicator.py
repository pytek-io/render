from render import Component, create_callback


class Indicator(Component):
    Module = "mantine/core"
    JSXName = "Indicator"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "component",
        "disabled",
        "h",
        "href",
        "inline",
        "label",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "offset",
        "p",
        "pb",
        "pe",
        "pl",
        "position",
        "pr",
        "processing",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "withBorder",
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
        autoContrast=None,
        color=None,
        component=None,
        disabled=None,
        h=None,
        href=None,
        inline=None,
        label=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        offset=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        position=None,
        pr=None,
        processing=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        withBorder=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.component = component
        self.disabled = disabled
        self.h = h
        self.href = href
        self.inline = inline
        self.label = label
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.position = position
        self.pr = pr
        self.processing = processing
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withBorder = withBorder
        self.zIndex = zIndex
