from render import Component, create_callback, Props


class HoverCard(Component):
    Module = "mantine/core"
    JSXName = "HoverCard"
    CALLBACKS = ["onKeyPress", "onClick", "onClose", "onOpen", "onPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "arrowOffset",
        "arrowPosition",
        "arrowRadius",
        "arrowSize",
        "clickOutsideEvents",
        "closeDelay",
        "closeOnClickOutside",
        "closeOnEscape",
        "component",
        "defaultOpened",
        "disabled",
        "floatingStrategy",
        "h",
        "href",
        "initiallyOpened",
        "keepMounted",
        "m",
        "mb",
        "middlewares",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "offset",
        "openDelay",
        "p",
        "pb",
        "pl",
        "portalProps",
        "position",
        "positionDependencies",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "returnFocus",
        "shadow",
        "sx",
        "ta",
        "target",
        "title",
        "transitionProps",
        "trapFocus",
        "variant",
        "width",
        "withArrow",
        "withRoles",
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
        arrowOffset=None,
        arrowPosition=None,
        arrowRadius=None,
        arrowSize=None,
        clickOutsideEvents=None,
        closeDelay=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        component=None,
        defaultOpened=None,
        disabled=None,
        floatingStrategy=None,
        h=None,
        href=None,
        initiallyOpened=None,
        keepMounted=None,
        m=None,
        mb=None,
        middlewares=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        offset=None,
        onClose=None,
        onOpen=None,
        onPositionChange=None,
        openDelay=None,
        p=None,
        pb=None,
        pl=None,
        portalProps=None,
        position=None,
        positionDependencies=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        returnFocus=None,
        shadow=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        transitionProps=None,
        trapFocus=None,
        variant=None,
        width=None,
        withArrow=None,
        withRoles=None,
        withinPortal=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.arrowOffset = arrowOffset
        self.arrowPosition = arrowPosition
        self.arrowRadius = arrowRadius
        self.arrowSize = arrowSize
        self.clickOutsideEvents = clickOutsideEvents
        self.closeDelay = closeDelay
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.component = component
        self.defaultOpened = defaultOpened
        self.disabled = disabled
        self.floatingStrategy = floatingStrategy
        self.h = h
        self.href = href
        self.initiallyOpened = initiallyOpened
        self.keepMounted = keepMounted
        self.m = m
        self.mb = mb
        self.middlewares = middlewares
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.onClose = create_callback(onClose, "onClose")
        self.onOpen = create_callback(onOpen, "onOpen")
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.openDelay = openDelay
        self.p = p
        self.pb = pb
        self.pl = pl
        self.portalProps = portalProps
        self.position = position
        self.positionDependencies = positionDependencies
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.returnFocus = returnFocus
        self.shadow = shadow
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.transitionProps = transitionProps
        self.trapFocus = trapFocus
        self.variant = variant
        self.width = width
        self.withArrow = withArrow
        self.withRoles = withRoles
        self.withinPortal = withinPortal
        self.zIndex = zIndex

    class Dropdown(Component):
        Module = "mantine/core"
        JSXName = "HoverCard.Dropdown"
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
            h=None,
            href=None,
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
            super().__init__(key, controller)
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

    class Target(Component):
        Module = "mantine/core"
        JSXName = "HoverCard.Target"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "eventPropsWrapperName",
            "h",
            "href",
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
            "popupType",
            "pr",
            "pt",
            "px",
            "py",
            "refProp",
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
            eventPropsWrapperName=None,
            h=None,
            href=None,
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
            popupType=None,
            pr=None,
            pt=None,
            px=None,
            py=None,
            refProp=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.eventPropsWrapperName = eventPropsWrapperName
            self.h = h
            self.href = href
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
            self.popupType = popupType
            self.pr = pr
            self.pt = pt
            self.px = px
            self.py = py
            self.refProp = refProp
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant
