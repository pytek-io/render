from render import Component, create_callback


class Layout(Component):
    Module = "antd"
    JSXName = "Layout"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "hasSider"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        hasSider=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.hasSider = hasSider

    class Content(Component):
        Module = "antd"
        JSXName = "Layout.Content"
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

    class Footer(Component):
        Module = "antd"
        JSXName = "Layout.Footer"
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

    class Header(Component):
        Module = "antd"
        JSXName = "Layout.Header"
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

    class Sider(Component):
        Module = "antd"
        JSXName = "Layout.Sider"
        CALLBACKS = ["onKeyPress", "onClick", "onBreakpoint", "onCollapse"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "breakpoint",
            "collapsed",
            "collapsedWidth",
            "collapsible",
            "defaultCollapsed",
            "reverseArrow",
            "theme",
            "trigger",
            "width",
            "zeroWidthTriggerStyle",
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
            breakpoint=None,
            collapsed=None,
            collapsedWidth=None,
            collapsible=None,
            defaultCollapsed=None,
            onBreakpoint=None,
            onCollapse=None,
            reverseArrow=None,
            theme=None,
            trigger=None,
            width=None,
            zeroWidthTriggerStyle=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.breakpoint = breakpoint
            self.collapsed = collapsed
            self.collapsedWidth = collapsedWidth
            self.collapsible = collapsible
            self.defaultCollapsed = defaultCollapsed
            self.onBreakpoint = create_callback(onBreakpoint, "onBreakpoint", [[0]])
            self.onCollapse = create_callback(onCollapse, "onCollapse", [[0], [1]])
            self.reverseArrow = reverseArrow
            self.theme = theme
            self.trigger = trigger
            self.width = width
            self.zeroWidthTriggerStyle = zeroWidthTriggerStyle
