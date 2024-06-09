from render import Component, create_callback, Props


class Icon(Component):
    Module = "ant-icons"
    JSXName = "Icon"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "extraCommonProps",
        "fill",
        "height",
        "rotate",
        "scriptUrl",
        "spin",
        "twoToneColor",
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
        component=None,
        extraCommonProps=None,
        fill=None,
        height=None,
        rotate=None,
        scriptUrl=None,
        spin=None,
        twoToneColor=None,
        width=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.component = component
        self.extraCommonProps = extraCommonProps
        self.fill = fill
        self.height = height
        self.rotate = rotate
        self.scriptUrl = scriptUrl
        self.spin = spin
        self.twoToneColor = twoToneColor
        self.width = width
