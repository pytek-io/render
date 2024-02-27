from render import Component, create_callback


class Title(Component):
    Module = "mantine"
    JSXName = "Title"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "lineClamp", "order", "size", "textWrap"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        lineClamp=None,
        order=None,
        size=None,
        textWrap=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.lineClamp = lineClamp
        self.order = order
        self.size = size
        self.textWrap = textWrap
