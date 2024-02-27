from render import Component, create_callback


class AppShell(Component):
    Module = "mantine"
    JSXName = "AppShell"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "aside",
        "disabled",
        "footer",
        "header",
        "layout",
        "navbar",
        "offsetScrollbars",
        "padding",
        "transitionDuration",
        "transitionTimingFunction",
        "withBorder",
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
        aside=None,
        disabled=None,
        footer=None,
        header=None,
        layout=None,
        navbar=None,
        offsetScrollbars=None,
        padding=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        withBorder=None,
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
        self.aside = aside
        self.disabled = disabled
        self.footer = footer
        self.header = header
        self.layout = layout
        self.navbar = navbar
        self.offsetScrollbars = offsetScrollbars
        self.padding = padding
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        self.withBorder = withBorder
        self.zIndex = zIndex

    class Aside(Component):
        Module = "mantine"
        JSXName = "AppShell.Aside"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "withBorder", "zIndex"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            withBorder=None,
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
            self.withBorder = withBorder
            self.zIndex = zIndex

    class Footer(Component):
        Module = "mantine"
        JSXName = "AppShell.Footer"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "withBorder", "zIndex"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            withBorder=None,
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
            self.withBorder = withBorder
            self.zIndex = zIndex

    class Header(Component):
        Module = "mantine"
        JSXName = "AppShell.Header"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "withBorder", "zIndex"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            withBorder=None,
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
            self.withBorder = withBorder
            self.zIndex = zIndex

    class Navbar(Component):
        Module = "mantine"
        JSXName = "AppShell.Navbar"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "withBorder", "zIndex"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            withBorder=None,
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
            self.withBorder = withBorder
            self.zIndex = zIndex

    class Section(Component):
        Module = "mantine"
        JSXName = "AppShell.Section"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "grow"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            grow=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.grow = grow
