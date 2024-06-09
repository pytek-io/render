from render import Component, create_callback, Props


class Notification(Component):
    Module = "mantine/core"
    JSXName = "Notification"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeButtonProps",
        "color",
        "component",
        "h",
        "href",
        "icon",
        "loading",
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
        "withBorder",
        "withCloseButton",
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
        closeButtonProps=None,
        color=None,
        component=None,
        h=None,
        href=None,
        icon=None,
        loading=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        onClose=None,
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
        withBorder=None,
        withCloseButton=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.closeButtonProps = closeButtonProps
        self.color = color
        self.component = component
        self.h = h
        self.href = href
        self.icon = icon
        self.loading = loading
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onClose = create_callback(onClose, "onClose")
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
        self.withBorder = withBorder
        self.withCloseButton = withCloseButton

    class s(Component):
        Module = "mantine/core"
        JSXName = "Notification.s"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoClose",
            "component",
            "containerWidth",
            "h",
            "href",
            "limit",
            "m",
            "mb",
            "me",
            "ml",
            "mr",
            "ms",
            "mt",
            "mx",
            "my",
            "notificationMaxHeight",
            "p",
            "pb",
            "pe",
            "pl",
            "portalProps",
            "position",
            "pr",
            "ps",
            "pt",
            "px",
            "py",
            "store",
            "sx",
            "ta",
            "target",
            "title",
            "transitionDuration",
            "variant",
            "withinPortal",
            "zIndex",
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
            autoClose=None,
            component=None,
            containerWidth=None,
            h=None,
            href=None,
            limit=None,
            m=None,
            mb=None,
            me=None,
            ml=None,
            mr=None,
            ms=None,
            mt=None,
            mx=None,
            my=None,
            notificationMaxHeight=None,
            p=None,
            pb=None,
            pe=None,
            pl=None,
            portalProps=None,
            position=None,
            pr=None,
            ps=None,
            pt=None,
            px=None,
            py=None,
            store=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            transitionDuration=None,
            variant=None,
            withinPortal=None,
            zIndex=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.autoClose = autoClose
            self.component = component
            self.containerWidth = containerWidth
            self.h = h
            self.href = href
            self.limit = limit
            self.m = m
            self.mb = mb
            self.me = me
            self.ml = ml
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.mx = mx
            self.my = my
            self.notificationMaxHeight = notificationMaxHeight
            self.p = p
            self.pb = pb
            self.pe = pe
            self.pl = pl
            self.portalProps = portalProps
            self.position = position
            self.pr = pr
            self.ps = ps
            self.pt = pt
            self.px = px
            self.py = py
            self.store = store
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.transitionDuration = transitionDuration
            self.variant = variant
            self.withinPortal = withinPortal
            self.zIndex = zIndex
