from render import create_callback, Component, InputComponent


class Collapse(Component):
    Module = "mantine"
    JSXName = "Collapse"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        animateOpacity=None,
        in_=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onTransitionEnd=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.animateOpacity = animateOpacity
        self.in_ = in_
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onTransitionEnd = create_callback(onTransitionEnd)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        assert id is None or isinstance(id, str)
