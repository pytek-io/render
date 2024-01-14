from render import create_callback, Component, InputComponent


class SegmentedControl(InputComponent):
    Module = "mantine"
    JSXName = "SegmentedControl"
    InputName = "value"

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
        color=None,
        data=None,
        disabled=None,
        fullWidth=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        name=None,
        orientation=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        size=None,
        sx=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.color = color
        self.data = data
        self.disabled = disabled
        self.fullWidth = fullWidth
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.name = name
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.size = size
        self.sx = sx
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        assert id is None or isinstance(id, str)
