from render import create_callback, Component, InputComponent


class NativeSelect(InputComponent):
    Module = "mantine"
    JSXName = "NativeSelect"
    InputName = "value"
    NewValuePath = "currentTarget.value"

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
        data=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pl=None,
        placeholder=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        sx=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.data = data
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pl = pl
        self.placeholder = placeholder
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.sx = sx
        self.wrapperProps = wrapperProps
        assert id is None or isinstance(id, str)
