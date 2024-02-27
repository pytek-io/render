from render import Component, create_callback


class Anchor(Component):
    Module = "mantine"
    JSXName = "Anchor"
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
        "truncate",
        "underline",
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
        truncate=None,
        underline=None,
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
        self.truncate = truncate
        self.underline = underline
