from render import Component, create_callback


class Popover(Component):
    Module = "antd"
    JSXName = "Popover"
    CALLBACKS = ["onKeyPress", "onClick", "onOpenChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "arrow",
        "autoAdjustOverflow",
        "color",
        "content",
        "defaultOpen",
        "destroyTooltipOnHide",
        "fresh",
        "getPopupContainer",
        "mouseEnterDelay",
        "mouseLeaveDelay",
        "open",
        "overlayClassName",
        "overlayInnerStyle",
        "overlayStyle",
        "placement",
        "title",
        "trigger",
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
        align=None,
        arrow=None,
        autoAdjustOverflow=None,
        color=None,
        content=None,
        defaultOpen=None,
        destroyTooltipOnHide=None,
        fresh=None,
        getPopupContainer=None,
        mouseEnterDelay=None,
        mouseLeaveDelay=None,
        onOpenChange=None,
        open=None,
        overlayClassName=None,
        overlayInnerStyle=None,
        overlayStyle=None,
        placement=None,
        title=None,
        trigger=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.arrow = arrow
        self.autoAdjustOverflow = autoAdjustOverflow
        self.color = color
        self.content = content
        self.defaultOpen = defaultOpen
        self.destroyTooltipOnHide = destroyTooltipOnHide
        self.fresh = fresh
        self.getPopupContainer = getPopupContainer
        self.mouseEnterDelay = mouseEnterDelay
        self.mouseLeaveDelay = mouseLeaveDelay
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.open = open
        self.overlayClassName = overlayClassName
        self.overlayInnerStyle = overlayInnerStyle
        self.overlayStyle = overlayStyle
        self.placement = placement
        self.title = title
        self.trigger = trigger
        self.zIndex = zIndex
