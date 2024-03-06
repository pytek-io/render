from render import Component, create_callback, Props


class Combobox(Component):
    Module = "mantine/core"
    JSXName = "Combobox"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onClose",
        "onOpen",
        "onOptionSubmit",
        "onPositionChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "arrowOffset",
        "arrowPosition",
        "arrowRadius",
        "arrowSize",
        "component",
        "disabled",
        "dropdownPadding",
        "floatingStrategy",
        "h",
        "href",
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
        "readOnly",
        "resetSelectionOnOptionHover",
        "returnFocus",
        "shadow",
        "size",
        "store",
        "sx",
        "ta",
        "target",
        "transitionProps",
        "variant",
        "width",
        "withArrow",
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
        component=None,
        disabled=None,
        dropdownPadding=None,
        floatingStrategy=None,
        h=None,
        href=None,
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
        onOptionSubmit=None,
        onPositionChange=None,
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
        readOnly=None,
        resetSelectionOnOptionHover=None,
        returnFocus=None,
        shadow=None,
        size=None,
        store=None,
        sx=None,
        ta=None,
        target=None,
        transitionProps=None,
        variant=None,
        width=None,
        withArrow=None,
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
        self.component = component
        self.disabled = disabled
        self.dropdownPadding = dropdownPadding
        self.floatingStrategy = floatingStrategy
        self.h = h
        self.href = href
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
        self.onOptionSubmit = create_callback(onOptionSubmit, "onOptionSubmit")
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
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
        self.readOnly = readOnly
        self.resetSelectionOnOptionHover = resetSelectionOnOptionHover
        self.returnFocus = returnFocus
        self.shadow = shadow
        self.size = size
        self.store = store
        self.sx = sx
        self.ta = ta
        self.target = target
        self.transitionProps = transitionProps
        self.variant = variant
        self.width = width
        self.withArrow = withArrow
        self.withinPortal = withinPortal
        self.zIndex = zIndex

    class Chevron(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Chevron"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "error",
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
            "size",
            "sx",
            "ta",
            "target",
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
            error=None,
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
            size=None,
            sx=None,
            ta=None,
            target=None,
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
            self.error = error
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
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant

    class Dropdown(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Dropdown"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "hidden",
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
            hidden=None,
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
            self.hidden = hidden
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
            self.variant = variant

    class Empty(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Empty"
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
            self.variant = variant

    class EventsTarget(Component):
        Module = "mantine/core"
        JSXName = "Combobox.EventsTarget"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoComplete",
            "component",
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
            "pr",
            "pt",
            "px",
            "py",
            "refProp",
            "sx",
            "ta",
            "target",
            "targetType",
            "variant",
            "withAriaAttributes",
            "withExpandedAttribute",
            "withKeyboardNavigation",
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
            autoComplete=None,
            component=None,
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
            pr=None,
            pt=None,
            px=None,
            py=None,
            refProp=None,
            sx=None,
            ta=None,
            target=None,
            targetType=None,
            variant=None,
            withAriaAttributes=None,
            withExpandedAttribute=None,
            withKeyboardNavigation=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.autoComplete = autoComplete
            self.component = component
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
            self.pr = pr
            self.pt = pt
            self.px = px
            self.py = py
            self.refProp = refProp
            self.sx = sx
            self.ta = ta
            self.target = target
            self.targetType = targetType
            self.variant = variant
            self.withAriaAttributes = withAriaAttributes
            self.withExpandedAttribute = withExpandedAttribute
            self.withKeyboardNavigation = withKeyboardNavigation

    class Footer(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Footer"
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
            self.variant = variant

    class Group(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Group"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "label",
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
            label=None,
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
            self.label = label
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
            self.variant = variant

    class Header(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Header"
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
            self.variant = variant

    class Option(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Option"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "active",
            "component",
            "disabled",
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
            "selected",
            "sx",
            "ta",
            "target",
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
            active=None,
            component=None,
            disabled=None,
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
            selected=None,
            sx=None,
            ta=None,
            target=None,
            value=None,
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
            self.active = active
            self.component = component
            self.disabled = disabled
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
            self.selected = selected
            self.sx = sx
            self.ta = ta
            self.target = target
            self.value = value
            self.variant = variant

    class Search(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Search"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "disabled",
            "error",
            "h",
            "href",
            "leftSection",
            "leftSectionPointerEvents",
            "leftSectionProps",
            "leftSectionWidth",
            "m",
            "mb",
            "me",
            "ml",
            "mr",
            "ms",
            "mt",
            "multiline",
            "mx",
            "my",
            "p",
            "pb",
            "pe",
            "pl",
            "pointer",
            "pr",
            "ps",
            "pt",
            "px",
            "py",
            "radius",
            "required",
            "rightSection",
            "rightSectionPointerEvents",
            "rightSectionProps",
            "rightSectionWidth",
            "size",
            "sx",
            "ta",
            "target",
            "variant",
            "withAria",
            "withAriaAttributes",
            "withErrorStyles",
            "withKeyboardNavigation",
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
            component=None,
            disabled=None,
            error=None,
            h=None,
            href=None,
            leftSection=None,
            leftSectionPointerEvents=None,
            leftSectionProps=None,
            leftSectionWidth=None,
            m=None,
            mb=None,
            me=None,
            ml=None,
            mr=None,
            ms=None,
            mt=None,
            multiline=None,
            mx=None,
            my=None,
            p=None,
            pb=None,
            pe=None,
            pl=None,
            pointer=None,
            pr=None,
            ps=None,
            pt=None,
            px=None,
            py=None,
            radius=None,
            required=None,
            rightSection=None,
            rightSectionPointerEvents=None,
            rightSectionProps=None,
            rightSectionWidth=None,
            size=None,
            sx=None,
            ta=None,
            target=None,
            variant=None,
            withAria=None,
            withAriaAttributes=None,
            withErrorStyles=None,
            withKeyboardNavigation=None,
            wrapperProps=None,
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
            self.disabled = disabled
            self.error = error
            self.h = h
            self.href = href
            self.leftSection = leftSection
            self.leftSectionPointerEvents = leftSectionPointerEvents
            self.leftSectionProps = leftSectionProps
            self.leftSectionWidth = leftSectionWidth
            self.m = m
            self.mb = mb
            self.me = me
            self.ml = ml
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.multiline = multiline
            self.mx = mx
            self.my = my
            self.p = p
            self.pb = pb
            self.pe = pe
            self.pl = pl
            self.pointer = pointer
            self.pr = pr
            self.ps = ps
            self.pt = pt
            self.px = px
            self.py = py
            self.radius = radius
            self.required = required
            self.rightSection = rightSection
            self.rightSectionPointerEvents = rightSectionPointerEvents
            self.rightSectionProps = rightSectionProps
            self.rightSectionWidth = rightSectionWidth
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant
            self.withAria = withAria
            self.withAriaAttributes = withAriaAttributes
            self.withErrorStyles = withErrorStyles
            self.withKeyboardNavigation = withKeyboardNavigation
            self.wrapperProps = wrapperProps

    class Target(Component):
        Module = "mantine/core"
        JSXName = "Combobox.Target"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoComplete",
            "component",
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
            "pr",
            "pt",
            "px",
            "py",
            "refProp",
            "sx",
            "ta",
            "target",
            "targetType",
            "variant",
            "withAriaAttributes",
            "withExpandedAttribute",
            "withKeyboardNavigation",
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
            autoComplete=None,
            component=None,
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
            pr=None,
            pt=None,
            px=None,
            py=None,
            refProp=None,
            sx=None,
            ta=None,
            target=None,
            targetType=None,
            variant=None,
            withAriaAttributes=None,
            withExpandedAttribute=None,
            withKeyboardNavigation=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.autoComplete = autoComplete
            self.component = component
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
            self.pr = pr
            self.pt = pt
            self.px = px
            self.py = py
            self.refProp = refProp
            self.sx = sx
            self.ta = ta
            self.target = target
            self.targetType = targetType
            self.variant = variant
            self.withAriaAttributes = withAriaAttributes
            self.withExpandedAttribute = withExpandedAttribute
            self.withKeyboardNavigation = withKeyboardNavigation
