from render import Component, create_callback, Props


class LoadingOverlay(Component):
    Module = "mantine"
    JSXName = "LoadingOverlay"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "loaderProps",
        "overlayProps",
        "transitionProps",
        "visible",
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
        loaderProps=None,
        overlayProps=None,
        transitionProps=None,
        visible=None,
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
        self.loaderProps = loaderProps
        self.overlayProps = overlayProps
        self.transitionProps = transitionProps
        self.visible = visible
        self.zIndex = zIndex
