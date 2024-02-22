from render import Component, create_callback, InputComponent, Props


class TextInput(InputComponent):
    Module = "mantine"
    JSXName = "TextInput"
    InputName = "value"
    NewValuePath = "currentTarget.value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "size",
        "sx",
        "type",
        "wrapperProps",
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
        onChange=None,
        defaultValue="",
        value=None,
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
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        sx=None,
        type=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
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
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.sx = sx
        self.type = type
        self.wrapperProps = wrapperProps
