from render import Component, create_callback, Props


class Popconfirm(Component):
    Module = "ant"
    JSXName = "Popconfirm"
    CALLBACKS = ["onKeyPress", "onClick", "onCancel", "onConfirm", "onPopupClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "cancelButtonProps",
        "cancelText",
        "description",
        "disabled",
        "icon",
        "okButtonProps",
        "okText",
        "okType",
        "showCancel",
        "title",
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
        cancelButtonProps=None,
        cancelText=None,
        description=None,
        disabled=None,
        icon=None,
        okButtonProps=None,
        okText=None,
        okType=None,
        onCancel=None,
        onConfirm=None,
        onPopupClick=None,
        showCancel=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.cancelButtonProps = cancelButtonProps
        self.cancelText = cancelText
        self.description = description
        self.disabled = disabled
        self.icon = icon
        self.okButtonProps = okButtonProps
        self.okText = okText
        self.okType = okType
        self.onCancel = create_callback(onCancel, "onCancel")
        self.onConfirm = create_callback(onConfirm, "onConfirm")
        self.onPopupClick = create_callback(onPopupClick, "onPopupClick")
        self.showCancel = showCancel
        self.title = title
