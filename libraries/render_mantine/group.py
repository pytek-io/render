from render import Component, create_callback


class Group(Component):
    Module = "mantine"
    JSXName = "Group"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "grow",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "noWrap",
        "p",
        "pb",
        "pl",
        "position",
        "pr",
        "pt",
        "px",
        "py",
        "spacing",
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
        align=None,
        grow=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        noWrap=None,
        p=None,
        pb=None,
        pl=None,
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        spacing=None,
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
        self.align = align
        self.grow = grow
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.noWrap = noWrap
        self.p = p
        self.pb = pb
        self.pl = pl
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.spacing = spacing
        self.sx = sx
