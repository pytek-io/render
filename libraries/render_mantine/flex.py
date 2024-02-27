from render import Component, create_callback


class Flex(Component):
    Module = "mantine"
    JSXName = "Flex"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "columnGap",
        "direction",
        "gap",
        "justify",
        "rowGap",
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
        columnGap=None,
        direction=None,
        gap=None,
        justify=None,
        rowGap=None,
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
        self.columnGap = columnGap
        self.direction = direction
        self.gap = gap
        self.justify = justify
        self.rowGap = rowGap
        self.wrap = wrap
