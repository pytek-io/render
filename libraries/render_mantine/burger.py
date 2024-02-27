from render import Component, create_callback


class Burger(Component):
    Module = "mantine"
    JSXName = "Burger"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "opened",
        "size",
        "transitionDuration",
        "transitionTimingFunction",
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
        color=None,
        opened=None,
        size=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.opened = opened
        self.size = size
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
