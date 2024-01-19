from render import Component, create_callback


class Message(Component):
    Module = "ant"
    JSXName = "Message"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "content",
        "duration",
        "getContainer",
        "icon",
        "maxCount",
        "prefixCls",
        "rtl",
        "top",
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
        content=None,
        duration=None,
        getContainer=None,
        icon=None,
        maxCount=None,
        onClose=None,
        prefixCls=None,
        rtl=None,
        top=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.content = content
        self.duration = duration
        self.getContainer = getContainer
        self.icon = icon
        self.maxCount = maxCount
        self.onClose = create_callback(onClose, "onClose")
        self.prefixCls = prefixCls
        self.rtl = rtl
        self.top = top
