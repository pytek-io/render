from render import Component, create_callback


class Indicator(Component):
    Module = "mantine"
    JSXName = "Indicator"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "disabled",
        "dot",
        "inline",
        "label",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "offset",
        "overflowCount",
        "p",
        "pb",
        "pl",
        "position",
        "pr",
        "processing",
        "pt",
        "px",
        "py",
        "radius",
        "showZero",
        "size",
        "sx",
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
        color=None,
        disabled=None,
        dot=None,
        inline=None,
        label=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        offset=None,
        overflowCount=None,
        p=None,
        pb=None,
        pl=None,
        position=None,
        pr=None,
        processing=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        showZero=None,
        size=None,
        sx=None,
        withBorder=None,
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
        self.dot = dot
        self.inline = inline
        self.label = label
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.overflowCount = overflowCount
        self.p = p
        self.pb = pb
        self.pl = pl
        self.position = position
        self.pr = pr
        self.processing = processing
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.showZero = showZero
        self.size = size
        self.sx = sx
        self.withBorder = withBorder
        self.zIndex = zIndex
