from render import create_callback, Component, InputComponent


class Overlay(Component):
    Module = "mantine"
    JSXName = "Overlay"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        blur=None,
        color=None,
        component=None,
        gradient=None,
        href=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        opacity=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        sx=None,
        target=None,
        title=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.blur = blur
        self.color = color
        self.component = component
        self.gradient = gradient
        self.href = href
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.opacity = opacity
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.sx = sx
        self.target = target
        self.title = title
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)
