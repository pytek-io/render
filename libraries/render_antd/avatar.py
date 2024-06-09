from render import Component, create_callback


class Avatar(Component):
    Module = "antd"
    JSXName = "Avatar"
    CALLBACKS = ["onKeyPress", "onClick", "onError"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alt",
        "crossOrigin",
        "draggable",
        "gap",
        "icon",
        "shape",
        "size",
        "src",
        "srcSet",
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
        alt=None,
        crossOrigin=None,
        draggable=None,
        gap=None,
        icon=None,
        onError=None,
        shape=None,
        size=None,
        src=None,
        srcSet=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alt = alt
        self.crossOrigin = crossOrigin
        self.draggable = draggable
        self.gap = gap
        self.icon = icon
        self.onError = create_callback(onError, "onError")
        self.shape = shape
        self.size = size
        self.src = src
        self.srcSet = srcSet

    class Group(Component):
        Module = "antd"
        JSXName = "Avatar.Group"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "maxCount",
            "maxPopoverPlacement",
            "maxPopoverTrigger",
            "maxStyle",
            "shape",
            "size",
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
            maxCount=None,
            maxPopoverPlacement=None,
            maxPopoverTrigger=None,
            maxStyle=None,
            shape=None,
            size=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.maxCount = maxCount
            self.maxPopoverPlacement = maxPopoverPlacement
            self.maxPopoverTrigger = maxPopoverTrigger
            self.maxStyle = maxStyle
            self.shape = shape
            self.size = size
