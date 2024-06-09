from render import Component, create_callback, Props


class Popconfirm(Component):
    Module = "antd"
    JSXName = "Popconfirm"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onCancel",
        "onConfirm",
        "onOpenChange",
        "onPopupClick",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "arrow",
        "autoAdjustOverflow",
        "cancelButtonProps",
        "cancelText",
        "color",
        "defaultOpen",
        "description",
        "destroyTooltipOnHide",
        "disabled",
        "fresh",
        "getPopupContainer",
        "icon",
        "mouseEnterDelay",
        "mouseLeaveDelay",
        "okButtonProps",
        "okText",
        "okType",
        "open",
        "overlayClassName",
        "overlayInnerStyle",
        "overlayStyle",
        "placement",
        "showCancel",
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
        cancelButtonProps=None,
        cancelText=None,
        color=None,
        defaultOpen=None,
        description=None,
        destroyTooltipOnHide=None,
        disabled=None,
        fresh=None,
        getPopupContainer=None,
        icon=None,
        mouseEnterDelay=None,
        mouseLeaveDelay=None,
        okButtonProps=None,
        okText=None,
        okType=None,
        onCancel=None,
        onConfirm=None,
        onOpenChange=None,
        onPopupClick=None,
        open=None,
        overlayClassName=None,
        overlayInnerStyle=None,
        overlayStyle=None,
        placement=None,
        showCancel=None,
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
        self.cancelButtonProps = cancelButtonProps
        self.cancelText = cancelText
        self.color = color
        self.defaultOpen = defaultOpen
        self.description = description
        self.destroyTooltipOnHide = destroyTooltipOnHide
        self.disabled = disabled
        self.fresh = fresh
        self.getPopupContainer = getPopupContainer
        self.icon = icon
        self.mouseEnterDelay = mouseEnterDelay
        self.mouseLeaveDelay = mouseLeaveDelay
        self.okButtonProps = okButtonProps
        self.okText = okText
        self.okType = okType
        self.onCancel = create_callback(onCancel, "onCancel")
        self.onConfirm = create_callback(onConfirm, "onConfirm")
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.onPopupClick = create_callback(onPopupClick, "onPopupClick")
        self.open = open
        self.overlayClassName = overlayClassName
        self.overlayInnerStyle = overlayInnerStyle
        self.overlayStyle = overlayStyle
        self.placement = placement
        self.showCancel = showCancel
        self.title = title
        self.trigger = trigger
        self.zIndex = zIndex
