from render import Component, create_callback


class Affix(Component):
    Module = "antd"
    JSXName = "Affix"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = ["style", "className", "id", "offsetBottom", "offsetTop", "target"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        offsetBottom=None,
        offsetTop=None,
        onChange=None,
        target=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.offsetBottom = offsetBottom
        self.offsetTop = offsetTop
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.target = target
