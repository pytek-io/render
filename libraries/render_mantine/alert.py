from render import Component, create_callback


class Alert(Component):
    Module = "mantine"
    JSXName = "Alert"
    CALLBACKS = ["onKeyPress", "onClick", "onClose"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "closeButtonLabel",
        "color",
        "icon",
        "radius",
        "title",
        "withCloseButton",
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
        autoContrast=None,
        closeButtonLabel=None,
        color=None,
        icon=None,
        onClose=None,
        radius=None,
        title=None,
        withCloseButton=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.closeButtonLabel = closeButtonLabel
        self.color = color
        self.icon = icon
        self.onClose = create_callback(onClose, "onClose")
        self.radius = radius
        self.title = title
        self.withCloseButton = withCloseButton
