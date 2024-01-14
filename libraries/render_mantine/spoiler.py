from render import create_callback, Component, InputComponent


class Spoiler(Component):
    Module = "mantine"
    JSXName = "Spoiler"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        controlRef=None,
        hideLabel=None,
        initialState=None,
        m=None,
        maxHeight=None,
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
        showLabel=None,
        sx=None,
        transitionDuration=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.controlRef = controlRef
        self.hideLabel = hideLabel
        self.initialState = initialState
        self.m = m
        self.maxHeight = maxHeight
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
        self.showLabel = showLabel
        self.sx = sx
        self.transitionDuration = transitionDuration
        assert id is None or isinstance(id, str)
