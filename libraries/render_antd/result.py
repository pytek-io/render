from render import Component, create_callback


class Result(Component):
    Module = "ant"
    JSXName = "Result"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "extra",
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
        extra=None,
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
        self.extra = extra
        self.icon = icon
        self.status = status
        self.subTitle = subTitle
        self.title = title
