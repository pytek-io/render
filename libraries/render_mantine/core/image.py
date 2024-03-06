from render import Component, create_callback, add_data_namespace


class Image(Component):
    Module = "mantine/core"
    JSXName = "Image"
    CALLBACKS = ["onKeyPress", "onClick", "onError"]
    DATA = ["src"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "fallbackSrc",
        "fit",
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
        fallbackSrc=None,
        fit=None,
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
        onError=None,
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
        src=None,
        sx=None,
        ta=None,
        target=None,
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
        self.component = component
        self.fallbackSrc = fallbackSrc
        self.fit = fit
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
        self.onError = create_callback(onError, "onError")
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
        self.src = add_data_namespace(src)
        self.sx = sx
        self.ta = ta
        self.target = target
        self.variant = variant
