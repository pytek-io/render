from render import Component, create_callback, Props


class Tour(Component):
    Module = "ant"
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


class TourStep(Component):
    Module = "ant"
    JSXName = "TourStep"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "arrow",
        "closeIcon",
        "cover",
        "description",
        "mask",
        "nextButtonProps",
        "placement",
        "prevButtonProps",
        "scrollIntoViewOptions",
        "target",
        "title",
        "type",
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
        cover=None,
        description=None,
        mask=None,
        nextButtonProps=None,
        onClose=None,
        placement=None,
        prevButtonProps=None,
        scrollIntoViewOptions=None,
        target=None,
        title=None,
        type=None,
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
        self.cover = cover
        self.description = description
        self.mask = mask
        self.nextButtonProps = nextButtonProps
        self.onClose = create_callback(onClose, "onClose")
        self.placement = placement
        self.prevButtonProps = prevButtonProps
        self.scrollIntoViewOptions = scrollIntoViewOptions
        self.target = target
        self.title = title
        self.type = type
