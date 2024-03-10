from render import Component, create_callback, Props


class ScrollArea(Component):
    Module = "mantine/core"
    JSXName = "ScrollArea"
    CALLBACKS = ["onKeyPress", "onClick", "onScrollPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
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
        "offsetScrollbars",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "scrollHideDelay",
        "scrollbarSize",
        "scrollbars",
        "sx",
        "ta",
        "target",
        "title",
        "type",
        "variant",
        "viewportProps",
        "viewportRef",
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
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        offsetScrollbars=None,
        onScrollPositionChange=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        scrollHideDelay=None,
        scrollbarSize=None,
        scrollbars=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        type=None,
        variant=None,
        viewportProps=None,
        viewportRef=None,
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
        self.offsetScrollbars = offsetScrollbars
        self.onScrollPositionChange = create_callback(
            onScrollPositionChange, "onScrollPositionChange"
        )
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.scrollHideDelay = scrollHideDelay
        self.scrollbarSize = scrollbarSize
        self.scrollbars = scrollbars
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.type = type
        self.variant = variant
        self.viewportProps = viewportProps
        self.viewportRef = viewportRef
