from render import Component, create_callback


class Tour(Component):
    Module = "antd"
    JSXName = "Tour"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "arrow",
        "closeIcon",
        "current",
        "indicatorsRender",
        "mask",
        "open",
        "placement",
        "scrollIntoViewOptions",
        "type",
        "zIndex",
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
        arrow=None,
        closeIcon=None,
        current=None,
        indicatorsRender=None,
        mask=None,
        onChange=None,
        onClose=None,
        open=None,
        placement=None,
        scrollIntoViewOptions=None,
        type=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.arrow = arrow
        self.closeIcon = closeIcon
        self.current = current
        self.indicatorsRender = indicatorsRender
        self.mask = mask
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onClose = create_callback(onClose, "onClose")
        self.open = open
        self.placement = placement
        self.scrollIntoViewOptions = scrollIntoViewOptions
        self.type = type
        self.zIndex = zIndex
