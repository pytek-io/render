from render import Component, create_callback, Props


class Drawer(Component):
    Module = "mantine/core"
    JSXName = "Drawer"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeButtonProps",
        "closeOnClickOutside",
        "closeOnEscape",
        "component",
        "h",
        "href",
        "keepMounted",
        "lockScroll",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "offset",
        "opened",
        "overlayProps",
        "p",
        "padding",
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
        "radius",
        "removeScrollProps",
        "returnFocus",
        "scrollAreaComponent",
        "shadow",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "transitionProps",
        "trapFocus",
        "variant",
        "withCloseButton",
        "withOverlay",
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
        closeButtonProps=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        component=None,
        h=None,
        href=None,
        keepMounted=None,
        lockScroll=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        offset=None,
        onClose=None,
        opened=None,
        overlayProps=None,
        p=None,
        padding=None,
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
        radius=None,
        removeScrollProps=None,
        returnFocus=None,
        scrollAreaComponent=None,
        shadow=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        transitionProps=None,
        trapFocus=None,
        variant=None,
        withCloseButton=None,
        withOverlay=None,
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
        self.closeButtonProps = closeButtonProps
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.component = component
        self.h = h
        self.href = href
        self.keepMounted = keepMounted
        self.lockScroll = lockScroll
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.onClose = create_callback(onClose, "onClose")
        self.opened = opened
        self.overlayProps = overlayProps
        self.p = p
        self.padding = padding
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
        self.radius = radius
        self.removeScrollProps = removeScrollProps
        self.returnFocus = returnFocus
        self.scrollAreaComponent = scrollAreaComponent
        self.shadow = shadow
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.transitionProps = transitionProps
        self.trapFocus = trapFocus
        self.variant = variant
        self.withCloseButton = withCloseButton
        self.withOverlay = withOverlay
        self.withinPortal = withinPortal
        self.zIndex = zIndex
