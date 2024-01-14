from render import Component, create_callback


class Alert(Component):
    Module = "ant"
    JSXName = "Alert"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        action=None,
        afterClose=None,
        banner=None,
        closeIcon=None,
        description=None,
        icon=None,
        message=None,
        onClose=None,
        showIcon=None,
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
        self.action = action
        self.afterClose = create_callback(afterClose, "afterClose", [])
        self.banner = banner
        self.closeIcon = closeIcon
        self.description = description
        self.icon = icon
        self.message = message
        self.onClose = create_callback(onClose, "onClose", [])
        self.showIcon = showIcon
        self.type = type


class AlertErrorBoundary(Component):
    Module = "ant"
    JSXName = "Alert.ErrorBoundary"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        description=None,
        message=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.description = description
        self.message = message
