from render import Component, create_callback


class Spin(Component):
    Module = "antd"
    JSXName = "Spin"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "delay",
        "fullscreen",
        "indicator",
        "size",
        "spinning",
        "tip",
        "wrapperClassName",
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
        delay=None,
        fullscreen=None,
        indicator=None,
        size=None,
        spinning=None,
        tip=None,
        wrapperClassName=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.delay = delay
        self.fullscreen = fullscreen
        self.indicator = indicator
        self.size = size
        self.spinning = spinning
        self.tip = tip
        self.wrapperClassName = wrapperClassName
