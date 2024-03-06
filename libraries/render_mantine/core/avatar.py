from render import Component, create_callback, add_data_namespace, Props


class Avatar(Component):
    Module = "mantine/core"
    JSXName = "Avatar"
    CALLBACKS = ["onKeyPress", "onClick"]
    DATA = ["src"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alt",
        "autoContrast",
        "color",
        "component",
        "gradient",
        "h",
        "href",
        "imageProps",
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
        "size",
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
        alt=None,
        autoContrast=None,
        color=None,
        component=None,
        gradient=None,
        h=None,
        href=None,
        imageProps=None,
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
        size=None,
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
        self.alt = alt
        self.autoContrast = autoContrast
        self.color = color
        self.component = component
        self.gradient = gradient
        self.h = h
        self.href = href
        self.imageProps = imageProps
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
        self.size = size
        self.src = add_data_namespace(src)
        self.sx = sx
        self.ta = ta
        self.target = target
        self.variant = variant
