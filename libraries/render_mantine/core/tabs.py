from render import Component, create_callback, InputComponent


class Tabs(InputComponent):
    Module = "mantine/core"
    JSXName = "Tabs"
    InputCallback = "onTabChange"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "activateTabWithKeyboard",
        "allowTabDeactivation",
        "autoContrast",
        "color",
        "component",
        "h",
        "href",
        "inverted",
        "keepMounted",
        "loop",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "orientation",
        "p",
        "pb",
        "pe",
        "pl",
        "placement",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
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
        activateTabWithKeyboard=None,
        allowTabDeactivation=None,
        autoContrast=None,
        color=None,
        component=None,
        h=None,
        href=None,
        inverted=None,
        keepMounted=None,
        loop=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        orientation=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        placement=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.activateTabWithKeyboard = activateTabWithKeyboard
        self.allowTabDeactivation = allowTabDeactivation
        self.autoContrast = autoContrast
        self.color = color
        self.component = component
        self.h = h
        self.href = href
        self.inverted = inverted
        self.keepMounted = keepMounted
        self.loop = loop
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.placement = placement
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant

    class List(Component):
        Module = "mantine/core"
        JSXName = "Tabs.List"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "grow",
            "h",
            "href",
            "justify",
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
            component=None,
            grow=None,
            h=None,
            href=None,
            justify=None,
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
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.grow = grow
            self.h = h
            self.href = href
            self.justify = justify
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant

    class Panel(Component):
        Module = "mantine/core"
        JSXName = "Tabs.Panel"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "keepMounted",
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
            "sx",
            "ta",
            "target",
            "title",
            "value",
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
            component=None,
            h=None,
            href=None,
            keepMounted=None,
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
            sx=None,
            ta=None,
            target=None,
            title=None,
            value=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.keepMounted = keepMounted
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.value = value
            self.variant = variant

    class Tab(Component):
        Module = "mantine/core"
        JSXName = "Tabs.Tab"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "color",
            "component",
            "h",
            "href",
            "leftSection",
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
            "rightSection",
            "size",
            "sx",
            "ta",
            "target",
            "title",
            "value",
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
            color=None,
            component=None,
            h=None,
            href=None,
            leftSection=None,
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
            rightSection=None,
            size=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            value=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.color = color
            self.component = component
            self.h = h
            self.href = href
            self.leftSection = leftSection
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
            self.rightSection = rightSection
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.value = value
            self.variant = variant
