from render import Component, create_callback, InputComponent


class SegmentedControl(InputComponent):
    Module = "mantine/core"
    JSXName = "SegmentedControl"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "component",
        "data",
        "disabled",
        "fullWidth",
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
        "name",
        "orientation",
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
        "readOnly",
        "size",
        "sx",
        "ta",
        "target",
        "transitionDuration",
        "transitionTimingFunction",
        "variant",
        "withItemsBorders",
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
        onChange=None,
        defaultValue=None,
        value=None,
        autoContrast=None,
        color=None,
        component=None,
        data=None,
        disabled=None,
        fullWidth=None,
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
        name=None,
        orientation=None,
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
        readOnly=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        variant=None,
        withItemsBorders=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.component = component
        self.data = data
        self.disabled = disabled
        self.fullWidth = fullWidth
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
        self.name = name
        self.orientation = orientation
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
        self.readOnly = readOnly
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        self.variant = variant
        self.withItemsBorders = withItemsBorders
