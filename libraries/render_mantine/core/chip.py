from render import Component, create_callback, InputComponent, Props


class Chip(InputComponent):
    Module = "mantine/core"
    JSXName = "Chip"
    InputName = "checked"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "component",
        "h",
        "href",
        "icon",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "rootRef",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "type",
        "variant",
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
        defaultChecked=None,
        checked=None,
        autoContrast=None,
        color=None,
        component=None,
        h=None,
        href=None,
        icon=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        rootRef=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        type=None,
        variant=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.component = component
        self.h = h
        self.href = href
        self.icon = icon
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.rootRef = rootRef
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.type = type
        self.variant = variant
        self.wrapperProps = wrapperProps

    class Group(InputComponent):
        Module = "mantine/core"
        JSXName = "Chip.Group"
        InputName = "value"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "m",
            "mb",
            "ml",
            "mr",
            "mt",
            "multiple",
            "mx",
            "my",
            "p",
            "pb",
            "pl",
            "pr",
            "pt",
            "px",
            "py",
            "sx",
            "ta",
            "target",
            "title",
            "variant",
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
            defaultValue=None,
            value=None,
            component=None,
            h=None,
            href=None,
            m=None,
            mb=None,
            ml=None,
            mr=None,
            mt=None,
            multiple=None,
            mx=None,
            my=None,
            p=None,
            pb=None,
            pl=None,
            pr=None,
            pt=None,
            px=None,
            py=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, onChange, value, defaultValue)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.m = m
            self.mb = mb
            self.ml = ml
            self.mr = mr
            self.mt = mt
            self.multiple = multiple
            self.mx = mx
            self.my = my
            self.p = p
            self.pb = pb
            self.pl = pl
            self.pr = pr
            self.pt = pt
            self.px = px
            self.py = py
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant
