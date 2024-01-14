from render import create_callback, Component, InputComponent


class PasswordInput(InputComponent):
    Module = "mantine"
    JSXName = "PasswordInput"
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
        defaultVisible=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onVisibilityChange=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        toggleTabIndex=None,
        visibilityToggleIcon=None,
        visibilityToggleLabel=None,
        visible=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.defaultVisible = defaultVisible
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onVisibilityChange = create_callback(onVisibilityChange)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.toggleTabIndex = toggleTabIndex
        self.visibilityToggleIcon = visibilityToggleIcon
        self.visibilityToggleLabel = visibilityToggleLabel
        self.visible = visible
        assert id is None or isinstance(id, str)
