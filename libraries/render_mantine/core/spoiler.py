from render import Component, create_callback


class Spoiler(Component):
    Module = "mantine/core"
    JSXName = "Spoiler"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "controlRef",
        "h",
        "hideLabel",
        "href",
        "initialState",
        "m",
        "maxHeight",
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
        "showLabel",
        "sx",
        "ta",
        "target",
        "title",
        "transitionDuration",
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
        controlRef=None,
        h=None,
        hideLabel=None,
        href=None,
        initialState=None,
        m=None,
        maxHeight=None,
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
        showLabel=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        transitionDuration=None,
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
        self.controlRef = controlRef
        self.h = h
        self.hideLabel = hideLabel
        self.href = href
        self.initialState = initialState
        self.m = m
        self.maxHeight = maxHeight
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
        self.showLabel = showLabel
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.transitionDuration = transitionDuration
        self.variant = variant
