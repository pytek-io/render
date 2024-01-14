from render import create_callback, Component, InputComponent


class Popover(InputComponent):
    Module = "mantine"
    JSXName = "Popover"
    InputName = "opened"

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
        defaultOpened=None,
        opened=None,
        __staticSelector=None,
        arrowOffset=None,
        arrowSize=None,
        classNames=None,
        clickOutsideEvents=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        disabled=None,
        exitTransitionDuration=None,
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
        p=None,
        pb=None,
        pl=None,
        position=None,
        positionDependencies=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        shadow=None,
        styles=None,
        sx=None,
        transition=None,
        transitionDuration=None,
        trapFocus=None,
        unstyled=None,
        width=None,
        withArrow=None,
        withRoles=None,
        withinPortal=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, opened, defaultOpened)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.__staticSelector = __staticSelector
        self.arrowOffset = arrowOffset
        self.arrowSize = arrowSize
        self.classNames = classNames
        self.clickOutsideEvents = clickOutsideEvents
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.disabled = disabled
        self.exitTransitionDuration = exitTransitionDuration
        self.m = m
        self.mb = mb
        self.middlewares = middlewares
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.onClose = create_callback(onClose)
        self.onOpen = create_callback(onOpen)
        self.onPositionChange = create_callback(onPositionChange)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.position = position
        self.positionDependencies = positionDependencies
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.shadow = shadow
        self.styles = styles
        self.sx = sx
        self.transition = transition
        self.transitionDuration = transitionDuration
        self.trapFocus = trapFocus
        self.unstyled = unstyled
        self.width = width
        self.withArrow = withArrow
        self.withRoles = withRoles
        self.withinPortal = withinPortal
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)


class PopoverDropdown(Component):
    Module = "mantine"
    JSXName = "Popover.Dropdown"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
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
        self.sx = sx
        assert id is None or isinstance(id, str)


class PopoverTarget(Component):
    Module = "mantine"
    JSXName = "Popover.Target"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
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
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
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
        assert id is None or isinstance(id, str)
