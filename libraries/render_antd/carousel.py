from render import Component, create_callback


class Carousel(Component):
    Module = "antd"
    JSXName = "Carousel"
    CALLBACKS = ["onKeyPress", "onClick", "afterChange", "beforeChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoplay",
        "autoplaySpeed",
        "dotPosition",
        "dots",
        "easing",
        "effect",
        "fade",
        "infinite",
        "speed",
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
        autoplaySpeed=None,
        beforeChange=None,
        dotPosition=None,
        dots=None,
        easing=None,
        effect=None,
        fade=None,
        infinite=None,
        speed=None,
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
        self.autoplaySpeed = autoplaySpeed
        self.beforeChange = create_callback(beforeChange, "beforeChange", [[0], [1]])
        self.dotPosition = dotPosition
        self.dots = dots
        self.easing = easing
        self.effect = effect
        self.fade = fade
        self.infinite = infinite
        self.speed = speed
        self.waitForAnimate = waitForAnimate
