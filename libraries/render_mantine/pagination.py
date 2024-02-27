from render import Component, create_callback, InputComponent, Props


class Pagination(InputComponent):
    Module = "mantine"
    JSXName = "Pagination"
    InputName = "page"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onFirstPage",
        "onLastPage",
        "onNextPage",
        "onPreviousPage",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "boundaries",
        "color",
        "defaultValue",
        "disabled",
        "dotsIcon",
        "firstIcon",
        "gap",
        "getControlProps",
        "getItemProps",
        "lastIcon",
        "nextIcon",
        "previousIcon",
        "radius",
        "siblings",
        "size",
        "total",
        "value",
        "withControls",
        "withEdges",
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
        defaultPage=None,
        page=None,
        autoContrast=None,
        boundaries=None,
        color=None,
        defaultValue=None,
        disabled=None,
        dotsIcon=None,
        firstIcon=None,
        gap=None,
        getControlProps=None,
        getItemProps=None,
        lastIcon=None,
        nextIcon=None,
        onFirstPage=None,
        onLastPage=None,
        onNextPage=None,
        onPreviousPage=None,
        previousIcon=None,
        radius=None,
        siblings=None,
        size=None,
        total=None,
        value=None,
        withControls=None,
        withEdges=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, page, defaultPage)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.boundaries = boundaries
        self.color = color
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.dotsIcon = dotsIcon
        self.firstIcon = firstIcon
        self.gap = gap
        self.getControlProps = getControlProps
        self.getItemProps = getItemProps
        self.lastIcon = lastIcon
        self.nextIcon = nextIcon
        self.onFirstPage = create_callback(onFirstPage, "onFirstPage")
        self.onLastPage = create_callback(onLastPage, "onLastPage")
        self.onNextPage = create_callback(onNextPage, "onNextPage")
        self.onPreviousPage = create_callback(onPreviousPage, "onPreviousPage")
        self.previousIcon = previousIcon
        self.radius = radius
        self.siblings = siblings
        self.size = size
        self.total = total
        self.value = value
        self.withControls = withControls
        self.withEdges = withEdges

    class Control(Component):
        Module = "mantine"
        JSXName = "Pagination.Control"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "active", "withPadding"]

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
            withPadding=None,
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
            self.withPadding = withPadding

    class Dots(Component):
        Module = "mantine"
        JSXName = "Pagination.Dots"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "icon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            icon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.icon = icon

    class First(Component):
        Module = "mantine"
        JSXName = "Pagination.First"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "icon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            icon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.icon = icon

    class Items(Component):
        Module = "mantine"
        JSXName = "Pagination.Items"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "dotsIcon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            dotsIcon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.dotsIcon = dotsIcon

    class Last(Component):
        Module = "mantine"
        JSXName = "Pagination.Last"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "icon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            icon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.icon = icon

    class Next(Component):
        Module = "mantine"
        JSXName = "Pagination.Next"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "icon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            icon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.icon = icon

    class Previous(Component):
        Module = "mantine"
        JSXName = "Pagination.Previous"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "icon"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            icon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.icon = icon

    class Root(Component):
        Module = "mantine"
        JSXName = "Pagination.Root"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onChange",
            "onFirstPage",
            "onLastPage",
            "onNextPage",
            "onPreviousPage",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoContrast",
            "boundaries",
            "color",
            "defaultValue",
            "disabled",
            "getItemProps",
            "radius",
            "siblings",
            "size",
            "total",
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
            autoContrast=None,
            boundaries=None,
            color=None,
            defaultValue=None,
            disabled=None,
            getItemProps=None,
            onChange=None,
            onFirstPage=None,
            onLastPage=None,
            onNextPage=None,
            onPreviousPage=None,
            radius=None,
            siblings=None,
            size=None,
            total=None,
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
            self.autoContrast = autoContrast
            self.boundaries = boundaries
            self.color = color
            self.defaultValue = defaultValue
            self.disabled = disabled
            self.getItemProps = getItemProps
            self.onChange = create_callback(onChange, "onChange")
            self.onFirstPage = create_callback(onFirstPage, "onFirstPage")
            self.onLastPage = create_callback(onLastPage, "onLastPage")
            self.onNextPage = create_callback(onNextPage, "onNextPage")
            self.onPreviousPage = create_callback(onPreviousPage, "onPreviousPage")
            self.radius = radius
            self.siblings = siblings
            self.size = size
            self.total = total
            self.value = value
