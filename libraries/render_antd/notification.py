from render import Component, create_callback


class Notification(Component):
    Module = "ant"
    JSXName = "Notification"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "bottom",
        "btn",
        "closeIcon",
        "description",
        "duration",
        "getContainer",
        "icon",
        "maxCount",
        "message",
        "placement",
        "props",
        "role",
        "rtl",
        "stack",
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
        bottom=None,
        btn=None,
        closeIcon=None,
        description=None,
        duration=None,
        getContainer=None,
        icon=None,
        maxCount=None,
        message=None,
        onClose=None,
        placement=None,
        props=None,
        role=None,
        rtl=None,
        stack=None,
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
        self.bottom = bottom
        self.btn = btn
        self.closeIcon = closeIcon
        self.description = description
        self.duration = duration
        self.getContainer = getContainer
        self.icon = icon
        self.maxCount = maxCount
        self.message = message
        self.onClose = create_callback(onClose, "onClose")
        self.placement = placement
        self.props = props
        self.role = role
        self.rtl = rtl
        self.stack = stack
        self.top = top
