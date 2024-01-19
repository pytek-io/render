from render import Component, create_callback


class FloatButton(Component):
    Module = "antd"
    JSXName = "FloatButton"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "badge",
        "description",
        "href",
        "icon",
        "shape",
        "target",
        "tooltip",
        "type",
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
        badge=None,
        description=None,
        href=None,
        icon=None,
        shape=None,
        target=None,
        tooltip=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.badge = badge
        self.description = description
        self.href = href
        self.icon = icon
        self.shape = shape
        self.target = target
        self.tooltip = tooltip
        self.type = type


class BackTop(Component):
    Module = "antd"
    JSXName = "FloatButton.BackTop"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "badge",
        "description",
        "duration",
        "href",
        "icon",
        "shape",
        "target",
        "tooltip",
        "type",
        "visibilityHeight",
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
        badge=None,
        description=None,
        duration=None,
        href=None,
        icon=None,
        shape=None,
        target=None,
        tooltip=None,
        type=None,
        visibilityHeight=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.badge = badge
        self.description = description
        self.duration = duration
        self.href = href
        self.icon = icon
        self.shape = shape
        self.target = target
        self.tooltip = tooltip
        self.type = type
        self.visibilityHeight = visibilityHeight


class Group(Component):
    Module = "antd"
    JSXName = "FloatButton.Group"
    CALLBACKS = ["onKeyPress", "onClick", "onOpenChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "badge",
        "description",
        "href",
        "icon",
        "open",
        "shape",
        "target",
        "tooltip",
        "trigger",
        "type",
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
        badge=None,
        description=None,
        href=None,
        icon=None,
        onOpenChange=None,
        open=None,
        shape=None,
        target=None,
        tooltip=None,
        trigger=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.badge = badge
        self.description = description
        self.href = href
        self.icon = icon
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.open = open
        self.shape = shape
        self.target = target
        self.tooltip = tooltip
        self.trigger = trigger
        self.type = type
