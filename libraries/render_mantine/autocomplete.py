from render import create_callback, Component, InputComponent


class Autocomplete(InputComponent):
    Module = "mantine"
    JSXName = "Autocomplete"
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
        dropdownComponent=None,
        m=None,
        maxDropdownHeight=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onItemSubmit=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.dropdownComponent = dropdownComponent
        self.m = m
        self.maxDropdownHeight = maxDropdownHeight
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onItemSubmit = create_callback(onItemSubmit)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        assert id is None or isinstance(id, str)
