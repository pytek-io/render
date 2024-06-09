from render import Component, create_callback


class Timeline(Component):
    Module = "mantine/core"
    JSXName = "Timeline"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "align",
        "autoContrast",
        "bulletSize",
        "color",
        "component",
        "h",
        "href",
        "lineWidth",
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
        "reverseActive",
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
        active=None,
        align=None,
        autoContrast=None,
        bulletSize=None,
        color=None,
        component=None,
        h=None,
        href=None,
        lineWidth=None,
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
        reverseActive=None,
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
        self.active = active
        self.align = align
        self.autoContrast = autoContrast
        self.bulletSize = bulletSize
        self.color = color
        self.component = component
        self.h = h
        self.href = href
        self.lineWidth = lineWidth
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
        self.reverseActive = reverseActive
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant

    class Item(Component):
        Module = "mantine/core"
        JSXName = "Timeline.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "bullet",
            "color",
            "component",
            "h",
            "href",
            "lineVariant",
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
            bullet=None,
            color=None,
            component=None,
            h=None,
            href=None,
            lineVariant=None,
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
            self.bullet = bullet
            self.color = color
            self.component = component
            self.h = h
            self.href = href
            self.lineVariant = lineVariant
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant
