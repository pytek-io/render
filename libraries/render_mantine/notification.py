from render import create_callback, Component, InputComponent


class Notification(Component):
    Module = "mantine"
    JSXName = "Notification"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        closeButtonProps=None,
        color=None,
        disallowClose=None,
        icon=None,
        loading=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onClose=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        sx=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.closeButtonProps = closeButtonProps
        self.color = color
        self.disallowClose = disallowClose
        self.icon = icon
        self.loading = loading
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onClose = create_callback(onClose)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.sx = sx
        self.title = title
        assert id is None or isinstance(id, str)
