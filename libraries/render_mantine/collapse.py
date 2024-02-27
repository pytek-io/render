from render import Component, create_callback


class Collapse(Component):
    Module = "mantine"
    JSXName = "Collapse"
    CALLBACKS = ["onKeyPress", "onClick", "onTransitionEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "_in",
        "animateOpacity",
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
        _in=None,
        animateOpacity=None,
        onTransitionEnd=None,
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
        self._in = _in
        self.animateOpacity = animateOpacity
        self.onTransitionEnd = create_callback(onTransitionEnd, "onTransitionEnd")
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
