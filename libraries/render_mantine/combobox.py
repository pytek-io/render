from render import Component, create_callback, Props


class Combobox(Component):
    Module = "mantine"
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
        "disabled",
        "dropdownPadding",
        "keepMounted",
        "middlewares",
        "offset",
        "portalProps",
        "position",
        "positionDependencies",
        "radius",
        "readOnly",
        "resetSelectionOnOptionHover",
        "returnFocus",
        "shadow",
        "size",
        "store",
        "transitionProps",
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
        disabled=None,
        dropdownPadding=None,
        keepMounted=None,
        middlewares=None,
        offset=None,
        onClose=None,
        onOpen=None,
        onOptionSubmit=None,
        onPositionChange=None,
        portalProps=None,
        position=None,
        positionDependencies=None,
        radius=None,
        readOnly=None,
        resetSelectionOnOptionHover=None,
        returnFocus=None,
        shadow=None,
        size=None,
        store=None,
        transitionProps=None,
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
        self.disabled = disabled
        self.dropdownPadding = dropdownPadding
        self.keepMounted = keepMounted
        self.middlewares = middlewares
        self.offset = offset
        self.onClose = create_callback(onClose, "onClose")
        self.onOpen = create_callback(onOpen, "onOpen")
        self.onOptionSubmit = create_callback(onOptionSubmit, "onOptionSubmit")
        self.onPositionChange = create_callback(onPositionChange, "onPositionChange")
        self.portalProps = portalProps
        self.position = position
        self.positionDependencies = positionDependencies
        self.radius = radius
        self.readOnly = readOnly
        self.resetSelectionOnOptionHover = resetSelectionOnOptionHover
        self.returnFocus = returnFocus
        self.shadow = shadow
        self.size = size
        self.store = store
        self.transitionProps = transitionProps
        self.width = width
        self.withArrow = withArrow
        self.withinPortal = withinPortal
        self.zIndex = zIndex

    class Chevron(Component):
        Module = "mantine"
        JSXName = "Combobox.Chevron"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "error", "size"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            error=None,
            size=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.error = error
            self.size = size

    class Dropdown(Component):
        Module = "mantine"
        JSXName = "Combobox.Dropdown"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "hidden"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            hidden=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.hidden = hidden

    class Empty(Component):
        Module = "mantine"
        JSXName = "Combobox.Empty"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")

    class EventsTarget(Component):
        Module = "mantine"
        JSXName = "Combobox.EventsTarget"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "refProp",
            "targetType",
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
            refProp=None,
            targetType=None,
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
            self.refProp = refProp
            self.targetType = targetType
            self.withAriaAttributes = withAriaAttributes
            self.withExpandedAttribute = withExpandedAttribute
            self.withKeyboardNavigation = withKeyboardNavigation

    class Footer(Component):
        Module = "mantine"
        JSXName = "Combobox.Footer"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")

    class Group(Component):
        Module = "mantine"
        JSXName = "Combobox.Group"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "label"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            label=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.label = label

    class Header(Component):
        Module = "mantine"
        JSXName = "Combobox.Header"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")

    class Option(Component):
        Module = "mantine"
        JSXName = "Combobox.Option"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "active",
            "disabled",
            "selected",
            "value",
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
            disabled=None,
            selected=None,
            value=None,
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
            self.disabled = disabled
            self.selected = selected
            self.value = value

    class Search(Component):
        Module = "mantine"
        JSXName = "Combobox.Search"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "disabled",
            "error",
            "leftSection",
            "leftSectionPointerEvents",
            "leftSectionProps",
            "leftSectionWidth",
            "multiline",
            "pointer",
            "radius",
            "required",
            "rightSection",
            "rightSectionPointerEvents",
            "rightSectionProps",
            "rightSectionWidth",
            "size",
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
            disabled=None,
            error=None,
            leftSection=None,
            leftSectionPointerEvents=None,
            leftSectionProps=None,
            leftSectionWidth=None,
            multiline=None,
            pointer=None,
            radius=None,
            required=None,
            rightSection=None,
            rightSectionPointerEvents=None,
            rightSectionProps=None,
            rightSectionWidth=None,
            size=None,
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
            self.disabled = disabled
            self.error = error
            self.leftSection = leftSection
            self.leftSectionPointerEvents = leftSectionPointerEvents
            self.leftSectionProps = leftSectionProps
            self.leftSectionWidth = leftSectionWidth
            self.multiline = multiline
            self.pointer = pointer
            self.radius = radius
            self.required = required
            self.rightSection = rightSection
            self.rightSectionPointerEvents = rightSectionPointerEvents
            self.rightSectionProps = rightSectionProps
            self.rightSectionWidth = rightSectionWidth
            self.size = size
            self.withAria = withAria
            self.withAriaAttributes = withAriaAttributes
            self.withErrorStyles = withErrorStyles
            self.withKeyboardNavigation = withKeyboardNavigation
            self.wrapperProps = wrapperProps

    class Target(Component):
        Module = "mantine"
        JSXName = "Combobox.Target"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "refProp",
            "targetType",
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
            refProp=None,
            targetType=None,
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
            self.refProp = refProp
            self.targetType = targetType
            self.withAriaAttributes = withAriaAttributes
            self.withExpandedAttribute = withExpandedAttribute
            self.withKeyboardNavigation = withKeyboardNavigation
