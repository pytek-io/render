from render import Component, create_callback


class Tag(Component):
    Module = "antd"
    JSXName = "Tag"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = ["style", "className", "id", "bordered", "closeIcon", "color", "icon"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        bordered=None,
        closeIcon=None,
        color=None,
        icon=None,
        onClose=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.bordered = bordered
        self.closeIcon = closeIcon
        self.color = color
        self.icon = icon
        self.onClose = create_callback(onClose, "onClose")


class CheckableTag(Component):
    Module = "antd"
    JSXName = "Tag.CheckableTag"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = ["style", "className", "id", "checked"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        checked=None,
        onChange=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.checked = checked
        self.onChange = create_callback(onChange, "onChange", [[0]])
