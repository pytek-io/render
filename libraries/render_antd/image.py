from render import Component, create_callback, add_data_namespace


class Image(Component):
    Module = "antd"
    JSXName = "Image"
    CALLBACKS = ["onKeyPress", "onClick", "onError", "onVisibleChange"]
    DATA = ["src"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alt",
        "closeIcon",
        "fallback",
        "forceRender",
        "getContainer",
        "height",
        "imageRender",
        "mask",
        "maskClassName",
        "maxScale",
        "minScale",
        "movable",
        "placeholder",
        "preview",
        "rootClassName",
        "scaleStep",
        "toolbarRender",
        "visible",
        "width",
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
        alt=None,
        closeIcon=None,
        fallback=None,
        forceRender=None,
        getContainer=None,
        height=None,
        imageRender=None,
        mask=None,
        maskClassName=None,
        maxScale=None,
        minScale=None,
        movable=None,
        onError=None,
        onVisibleChange=None,
        placeholder=None,
        preview=None,
        rootClassName=None,
        scaleStep=None,
        src=None,
        toolbarRender=None,
        visible=None,
        width=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alt = alt
        self.closeIcon = closeIcon
        self.fallback = fallback
        self.forceRender = forceRender
        self.getContainer = getContainer
        self.height = height
        self.imageRender = imageRender
        self.mask = mask
        self.maskClassName = maskClassName
        self.maxScale = maxScale
        self.minScale = minScale
        self.movable = movable
        self.onError = create_callback(onError, "onError")
        self.onVisibleChange = create_callback(
            onVisibleChange, "onVisibleChange", [[0], [1]]
        )
        self.placeholder = placeholder
        self.preview = preview
        self.rootClassName = rootClassName
        self.scaleStep = scaleStep
        self.src = add_data_namespace(src)
        self.toolbarRender = toolbarRender
        self.visible = visible
        self.width = width
