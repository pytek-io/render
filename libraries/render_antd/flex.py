from render import Component, create_callback


class Flex(Component):
    Module = "ant"
    JSXName = "Flex"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "component",
        "flex",
        "gap",
        "justify",
        "vertical",
        "wrap",
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
        align=None,
        component=None,
        flex=None,
        gap=None,
        justify=None,
        vertical=None,
        wrap=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.component = component
        self.flex = flex
        self.gap = gap
        self.justify = justify
        self.vertical = vertical
        self.wrap = wrap
