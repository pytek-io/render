from render import create_callback, Component, InputComponent


class Modal(Component):
    Module = "mantine"
    JSXName = "Modal"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        centered=None,
        closeButtonLabel=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        fullScreen=None,
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
        overflow=None,
        overlayBlur=None,
        overlayColor=None,
        overlayOpacity=None,
        p=None,
        padding=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
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
        withinPortal=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.centered = centered
        self.closeButtonLabel = closeButtonLabel
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.fullScreen = fullScreen
        self.lockScroll = lockScroll
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onClose = create_callback(onClose)
        self.opened = opened
        self.overflow = overflow
        self.overlayBlur = overlayBlur
        self.overlayColor = overlayColor
        self.overlayOpacity = overlayOpacity
        self.p = p
        self.padding = padding
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
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
        self.withinPortal = withinPortal
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)
