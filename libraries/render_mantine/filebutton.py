from render import create_callback, Component, InputComponent


class FileButton(Component):
    Module = "mantine"
    JSXName = "FileButton"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        accept=None,
        form=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        multiple=None,
        mx=None,
        my=None,
        name=None,
        onChange=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        resetRef=None,
        sx=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.accept = accept
        self.form = form
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.multiple = multiple
        self.mx = mx
        self.my = my
        self.name = name
        self.onChange = create_callback(onChange)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.resetRef = create_callback(resetRef)
        self.sx = sx
        assert id is None or isinstance(id, str)
