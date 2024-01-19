from render import Component, create_callback


class Carousel(Component):
    Module = "ant"
    JSXName = "Carousel"
    CALLBACKS = ["onKeyPress", "onClick", "afterChange", "beforeChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoplay",
        "dotPosition",
        "dots",
        "easing",
        "effect",
        "waitForAnimate",
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
        afterChange=None,
        autoplay=None,
        beforeChange=None,
        dotPosition=None,
        dots=None,
        easing=None,
        effect=None,
        waitForAnimate=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.afterChange = create_callback(afterChange, "afterChange", [[0]])
        self.autoplay = autoplay
        self.beforeChange = create_callback(beforeChange, "beforeChange", [[0], [1]])
        self.dotPosition = dotPosition
        self.dots = dots
        self.easing = easing
        self.effect = effect
        self.waitForAnimate = waitForAnimate
