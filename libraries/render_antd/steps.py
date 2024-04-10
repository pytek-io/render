from render import Component, create_callback


class Steps(Component):
    Module = "antd"
    JSXName = "Steps"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "current",
        "direction",
        "initial",
        "items",
        "labelPlacement",
        "percent",
        "progressDot",
        "responsive",
        "size",
        "status",
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
        current=None,
        direction=None,
        initial=None,
        items=None,
        labelPlacement=None,
        onChange=None,
        percent=None,
        progressDot=None,
        responsive=None,
        size=None,
        status=None,
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
        self.current = current
        self.direction = direction
        self.initial = initial
        self.items = items
        self.labelPlacement = labelPlacement
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.percent = percent
        self.progressDot = progressDot
        self.responsive = responsive
        self.size = size
        self.status = status
        self.type = type

    class Item(Component):
        Module = "antd"
        JSXName = "Steps.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "description",
            "disabled",
            "icon",
            "status",
            "subTitle",
            "title",
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
            description=None,
            disabled=None,
            icon=None,
            status=None,
            subTitle=None,
            title=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.description = description
            self.disabled = disabled
            self.icon = icon
            self.status = status
            self.subTitle = subTitle
            self.title = title
