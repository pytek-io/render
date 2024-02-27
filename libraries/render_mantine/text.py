from render import Component, create_callback


class Text(Component):
    Module = "mantine"
    JSXName = "Text"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "gradient",
        "inherit",
        "inline",
        "lineClamp",
        "size",
        "span",
        "truncate",
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
        gradient=None,
        inherit=None,
        inline=None,
        lineClamp=None,
        size=None,
        span=None,
        truncate=None,
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
        self.gradient = gradient
        self.inherit = inherit
        self.inline = inline
        self.lineClamp = lineClamp
        self.size = size
        self.span = span
        self.truncate = truncate
