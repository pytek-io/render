from render import create_callback, Component, InputComponent


class Button(Component):
    Module = "mantine"
    JSXName = "Button"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        color=None,
        compact=None,
        component=None,
        disabled=None,
        fullWidth=None,
        gradient=None,
        href=None,
        leftIcon=None,
        loaderPosition=None,
        loaderProps=None,
        loading=None,
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
        radius=None,
        rightIcon=None,
        size=None,
        sx=None,
        target=None,
        title=None,
        type=None,
        uppercase=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.color = color
        self.compact = compact
        self.component = component
        self.disabled = disabled
        self.fullWidth = fullWidth
        self.gradient = gradient
        self.href = href
        self.leftIcon = leftIcon
        self.loaderPosition = loaderPosition
        self.loaderProps = loaderProps
        self.loading = loading
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
        self.radius = radius
        self.rightIcon = rightIcon
        self.size = size
        self.sx = sx
        self.target = target
        self.title = title
        self.type = type
        self.uppercase = uppercase
        self.variant = variant
        assert id is None or isinstance(id, str)


class ButtonGroup(Component):
    Module = "mantine"
    JSXName = "ButtonGroup"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        buttonBorderWidth=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        orientation=None,
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
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.buttonBorderWidth = buttonBorderWidth
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        assert id is None or isinstance(id, str)
