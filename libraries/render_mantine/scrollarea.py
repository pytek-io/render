from render import Component, create_callback


class ScrollArea(Component):
    Module = "mantine"
    JSXName = "ScrollArea"
    CALLBACKS = ["onKeyPress", "onClick", "onScrollPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "dir",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "offsetScrollbars",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "scrollHideDelay",
        "scrollbarSize",
        "sx",
        "type",
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
        dir=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        offsetScrollbars=None,
        onScrollPositionChange=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        scrollHideDelay=None,
        scrollbarSize=None,
        sx=None,
        type=None,
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
        self.dir = dir
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offsetScrollbars = offsetScrollbars
        self.onScrollPositionChange = create_callback(
            onScrollPositionChange, "onScrollPositionChange"
        )
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.scrollHideDelay = scrollHideDelay
        self.scrollbarSize = scrollbarSize
        self.sx = sx
        self.type = type
        self.viewportRef = viewportRef
