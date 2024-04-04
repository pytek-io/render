from render import Component, create_callback


class Space(Component):
    Module = "antd"
    JSXName = "Space"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "classNames",
        "direction",
        "size",
        "split",
        "styles",
        "wrap",
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
        align=None,
        classNames=None,
        direction=None,
        size=None,
        split=None,
        styles=None,
        wrap=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.classNames = classNames
        self.direction = direction
        self.size = size
        self.split = split
        self.styles = styles
        self.wrap = wrap
