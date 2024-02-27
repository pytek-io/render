from render import Component, create_callback


class Indicator(Component):
    Module = "mantine"
    JSXName = "Indicator"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "disabled",
        "inline",
        "label",
        "offset",
        "position",
        "processing",
        "radius",
        "size",
        "withBorder",
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
        autoContrast=None,
        color=None,
        disabled=None,
        inline=None,
        label=None,
        offset=None,
        position=None,
        processing=None,
        radius=None,
        size=None,
        withBorder=None,
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
        self.autoContrast = autoContrast
        self.color = color
        self.disabled = disabled
        self.inline = inline
        self.label = label
        self.offset = offset
        self.position = position
        self.processing = processing
        self.radius = radius
        self.size = size
        self.withBorder = withBorder
        self.zIndex = zIndex
