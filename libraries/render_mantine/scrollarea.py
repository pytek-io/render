from render import create_callback, Component, InputComponent


class ScrollArea(Component):
    Module = "mantine"
    JSXName = "ScrollArea"

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
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.dir = dir
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offsetScrollbars = offsetScrollbars
        self.onScrollPositionChange = create_callback(onScrollPositionChange)
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
        assert id is None or isinstance(id, str)


class ScrollAreaAutosize(Component):
    Module = "mantine"
    JSXName = "ScrollArea.Autosize"

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
        maxHeight=None,
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
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.dir = dir
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offsetScrollbars = offsetScrollbars
        self.onScrollPositionChange = create_callback(onScrollPositionChange)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.scrollHideDelay = scrollHideDelay
        self.scrollbarSize = scrollbarSize
        self.maxHeight = maxHeight
        self.sx = sx
        self.type = type
        self.viewportRef = viewportRef
        assert id is None or isinstance(id, str)
