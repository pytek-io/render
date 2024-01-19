from render import Component, create_callback


class QRCode(Component):
    Module = "antd"
    JSXName = "QRCode"
    CALLBACKS = ["onKeyPress", "onClick", "onRefresh"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "bgColor",
        "bordered",
        "color",
        "errorLevel",
        "icon",
        "iconSize",
        "size",
        "status",
        "type",
        "value",
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
        bgColor=None,
        bordered=None,
        color=None,
        errorLevel=None,
        icon=None,
        iconSize=None,
        onRefresh=None,
        size=None,
        status=None,
        type=None,
        value=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.bgColor = bgColor
        self.bordered = bordered
        self.color = color
        self.errorLevel = errorLevel
        self.icon = icon
        self.iconSize = iconSize
        self.onRefresh = create_callback(onRefresh, "onRefresh")
        self.size = size
        self.status = status
        self.type = type
        self.value = value
