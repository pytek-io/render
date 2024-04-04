from render import Component, create_callback


class Button(Component):
    Module = "antd"
    JSXName = "Button"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "block",
        "classNames",
        "danger",
        "disabled",
        "ghost",
        "href",
        "htmlType",
        "icon",
        "loading",
        "shape",
        "size",
        "styles",
        "target",
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
        block=None,
        classNames=None,
        danger=None,
        disabled=None,
        ghost=None,
        href=None,
        htmlType=None,
        icon=None,
        loading=None,
        shape=None,
        size=None,
        styles=None,
        target=None,
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
        self.block = block
        self.classNames = classNames
        self.danger = danger
        self.disabled = disabled
        self.ghost = ghost
        self.href = href
        self.htmlType = htmlType
        self.icon = icon
        self.loading = loading
        self.shape = shape
        self.size = size
        self.styles = styles
        self.target = target
        self.type = type

    class Group(Component):
        Module = "antd"
        JSXName = "Button.Group"
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
