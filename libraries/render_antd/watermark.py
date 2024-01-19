from render import Component, create_callback


class Font(Component):
    Module = "ant"
    JSXName = "Font"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "fontFamily",
        "fontSize",
        "fontStyle",
        "fontWeight",
        "textAlign",
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
        color=None,
        fontFamily=None,
        fontSize=None,
        fontStyle=None,
        fontWeight=None,
        textAlign=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontStyle = fontStyle
        self.fontWeight = fontWeight
        self.textAlign = textAlign


class Watermark(Component):
    Module = "ant"
    JSXName = "Watermark"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "content",
        "font",
        "gap",
        "height",
        "image",
        "inherit",
        "offset",
        "rotate",
        "width",
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
        content=None,
        font=None,
        gap=None,
        height=None,
        image=None,
        inherit=None,
        offset=None,
        rotate=None,
        width=None,
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
        self.content = content
        self.font = font
        self.gap = gap
        self.height = height
        self.image = image
        self.inherit = inherit
        self.offset = offset
        self.rotate = rotate
        self.width = width
        self.zIndex = zIndex
