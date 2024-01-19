from render import Component, create_callback


class Drawer(Component):
    Module = "mantine"
    JSXName = "Drawer"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeButtonLabel",
        "closeOnClickOutside",
        "closeOnEscape",
        "lockScroll",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "opened",
        "overlayBlur",
        "overlayColor",
        "overlayOpacity",
        "p",
        "padding",
        "pb",
        "pl",
        "position",
        "pr",
        "pt",
        "px",
        "py",
        "shadow",
        "size",
        "sx",
        "target",
        "title",
        "transition",
        "transitionDuration",
        "transitionTimingFunction",
        "trapFocus",
        "withCloseButton",
        "withFocusReturn",
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
        closeButtonLabel=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        lockScroll=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onClose=None,
        opened=None,
        overlayBlur=None,
        overlayColor=None,
        overlayOpacity=None,
        p=None,
        padding=None,
        pb=None,
        pl=None,
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        shadow=None,
        size=None,
        sx=None,
        target=None,
        title=None,
        transition=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        trapFocus=None,
        withCloseButton=None,
        withFocusReturn=None,
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
        self.closeButtonLabel = closeButtonLabel
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.lockScroll = lockScroll
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onClose = create_callback(onClose, "onClose")
        self.opened = opened
        self.overlayBlur = overlayBlur
        self.overlayColor = overlayColor
        self.overlayOpacity = overlayOpacity
        self.p = p
        self.padding = padding
        self.pb = pb
        self.pl = pl
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.shadow = shadow
        self.size = size
        self.sx = sx
        self.target = target
        self.title = title
        self.transition = transition
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        self.trapFocus = trapFocus
        self.withCloseButton = withCloseButton
        self.withFocusReturn = withFocusReturn
        self.withOverlay = withOverlay
        self.withinPortal = withinPortal
        self.zIndex = zIndex
