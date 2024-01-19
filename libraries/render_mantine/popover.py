from render import Component, create_callback, InputComponent


class Popover(InputComponent):
    Module = "mantine"
    JSXName = "Popover"
    InputName = "opened"
    CALLBACKS = ["onKeyPress", "onClick", "onClose", "onOpen", "onPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "__staticSelector",
        "arrowOffset",
        "arrowSize",
        "classNames",
        "clickOutsideEvents",
        "closeOnClickOutside",
        "closeOnEscape",
        "disabled",
        "exitTransitionDuration",
        "m",
        "mb",
        "middlewares",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "offset",
        "p",
        "pb",
        "pl",
        "position",
        "positionDependencies",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "shadow",
        "styles",
        "sx",
        "transition",
        "transitionDuration",
        "trapFocus",
        "unstyled",
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
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
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
        self.onClose = create_callback(onClose, "onClose")
        self.onOpen = create_callback(onOpen, "onOpen")
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
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


class PopoverDropdown(Component):
    Module = "mantine"
    JSXName = "Popover.Dropdown"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
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
        "pr",
        "pt",
        "px",
        "py",
        "sx",
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
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
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


class PopoverTarget(Component):
    Module = "mantine"
    JSXName = "Popover.Target"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
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
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
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
