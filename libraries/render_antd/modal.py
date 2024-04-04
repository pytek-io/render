from render import Component, create_callback, Props


class Modal(Component):
    Module = "antd"
    JSXName = "Modal"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "afterClose",
        "afterOpenChange",
        "onCancel",
        "onOk",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "cancelButtonProps",
        "cancelText",
        "centered",
        "classNames",
        "closeIcon",
        "confirmLoading",
        "destroyOnClose",
        "focusTriggerAfterClose",
        "footer",
        "forceRender",
        "getContainer",
        "keyboard",
        "mask",
        "maskClosable",
        "modalRender",
        "okButtonProps",
        "okText",
        "okType",
        "open",
        "styles",
        "title",
        "width",
        "wrapClassName",
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
        afterClose=None,
        afterOpenChange=None,
        cancelButtonProps=None,
        cancelText=None,
        centered=None,
        classNames=None,
        closeIcon=None,
        confirmLoading=None,
        destroyOnClose=None,
        focusTriggerAfterClose=None,
        footer=None,
        forceRender=None,
        getContainer=None,
        keyboard=None,
        mask=None,
        maskClosable=None,
        modalRender=None,
        okButtonProps=None,
        okText=None,
        okType=None,
        onCancel=None,
        onOk=None,
        open=None,
        styles=None,
        title=None,
        width=None,
        wrapClassName=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.afterClose = create_callback(afterClose, "afterClose")
        self.afterOpenChange = create_callback(
            afterOpenChange, "afterOpenChange", [[0]]
        )
        self.cancelButtonProps = cancelButtonProps
        self.cancelText = cancelText
        self.centered = centered
        self.classNames = classNames
        self.closeIcon = closeIcon
        self.confirmLoading = confirmLoading
        self.destroyOnClose = destroyOnClose
        self.focusTriggerAfterClose = focusTriggerAfterClose
        self.footer = footer
        self.forceRender = forceRender
        self.getContainer = getContainer
        self.keyboard = keyboard
        self.mask = mask
        self.maskClosable = maskClosable
        self.modalRender = modalRender
        self.okButtonProps = okButtonProps
        self.okText = okText
        self.okType = okType
        self.onCancel = create_callback(onCancel, "onCancel")
        self.onOk = create_callback(onOk, "onOk")
        self.open = open
        self.styles = styles
        self.title = title
        self.width = width
        self.wrapClassName = wrapClassName
        self.zIndex = zIndex
