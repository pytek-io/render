from render import Component, create_callback


class DatesProvider(Component):
    Module = "mantine/dates"
    JSXName = "DatesProvider"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "h",
        "href",
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
        "pr",
        "pt",
        "px",
        "py",
        "settings",
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
        component=None,
        h=None,
        href=None,
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
        pr=None,
        pt=None,
        px=None,
        py=None,
        settings=None,
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
        self.component = component
        self.h = h
        self.href = href
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
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.settings = settings
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
