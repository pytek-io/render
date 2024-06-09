from render import Component, create_callback


class Drawer(Component):
    Module = "antd"
    JSXName = "Drawer"
    CALLBACKS = ["onKeyPress", "onClick", "afterOpenChange", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoFocus",
        "classNames",
        "closeIcon",
        "destroyOnClose",
        "extra",
        "footer",
        "forceRender",
        "getContainer",
        "headerStyle",
        "height",
        "keyboard",
        "mask",
        "maskClosable",
        "open",
        "placement",
        "push",
        "rootStyle",
        "size",
        "styles",
        "title",
        "width",
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
        afterOpenChange=None,
        autoFocus=None,
        classNames=None,
        closeIcon=None,
        destroyOnClose=None,
        extra=None,
        footer=None,
        forceRender=None,
        getContainer=None,
        headerStyle=None,
        height=None,
        keyboard=None,
        mask=None,
        maskClosable=None,
        onClose=None,
        open=None,
        placement=None,
        push=None,
        rootStyle=None,
        size=None,
        styles=None,
        title=None,
        width=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.afterOpenChange = create_callback(
            afterOpenChange, "afterOpenChange", [[0]]
        )
        self.autoFocus = autoFocus
        self.classNames = classNames
        self.closeIcon = closeIcon
        self.destroyOnClose = destroyOnClose
        self.extra = extra
        self.footer = footer
        self.forceRender = forceRender
        self.getContainer = getContainer
        self.headerStyle = headerStyle
        self.height = height
        self.keyboard = keyboard
        self.mask = mask
        self.maskClosable = maskClosable
        self.onClose = create_callback(onClose, "onClose")
        self.open = open
        self.placement = placement
        self.push = push
        self.rootStyle = rootStyle
        self.size = size
        self.styles = styles
        self.title = title
        self.width = width
        self.zIndex = zIndex
