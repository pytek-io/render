from render import Component, create_callback, Props


class ScrollArea(Component):
    Module = "mantine"
    JSXName = "ScrollArea"
    CALLBACKS = ["onKeyPress", "onClick", "onScrollPositionChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "offsetScrollbars",
        "scrollHideDelay",
        "scrollbarSize",
        "scrollbars",
        "type",
        "viewportProps",
        "viewportRef",
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
        offsetScrollbars=None,
        onScrollPositionChange=None,
        scrollHideDelay=None,
        scrollbarSize=None,
        scrollbars=None,
        type=None,
        viewportProps=None,
        viewportRef=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.offsetScrollbars = offsetScrollbars
        self.onScrollPositionChange = create_callback(
            onScrollPositionChange, "onScrollPositionChange"
        )
        self.scrollHideDelay = scrollHideDelay
        self.scrollbarSize = scrollbarSize
        self.scrollbars = scrollbars
        self.type = type
        self.viewportProps = viewportProps
        self.viewportRef = viewportRef
