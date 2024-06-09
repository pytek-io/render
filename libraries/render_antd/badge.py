from render import Component, create_callback


class Badge(Component):
    Module = "antd"
    JSXName = "Badge"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "classNames",
        "color",
        "count",
        "dot",
        "offset",
        "overflowCount",
        "showZero",
        "size",
        "status",
        "styles",
        "text",
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
        classNames=None,
        color=None,
        count=None,
        dot=None,
        offset=None,
        overflowCount=None,
        showZero=None,
        size=None,
        status=None,
        styles=None,
        text=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.classNames = classNames
        self.color = color
        self.count = count
        self.dot = dot
        self.offset = offset
        self.overflowCount = overflowCount
        self.showZero = showZero
        self.size = size
        self.status = status
        self.styles = styles
        self.text = text
        self.title = title

    class Ribbon(Component):
        Module = "antd"
        JSXName = "Badge.Ribbon"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "color", "placement", "text"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            color=None,
            placement=None,
            text=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.color = color
            self.placement = placement
            self.text = text
