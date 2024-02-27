from render import Component, create_callback


class Group(Component):
    Module = "mantine"
    JSXName = "Group"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "gap",
        "grow",
        "justify",
        "preventGrowOverflow",
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
        gap=None,
        grow=None,
        justify=None,
        preventGrowOverflow=None,
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
        self.gap = gap
        self.grow = grow
        self.justify = justify
        self.preventGrowOverflow = preventGrowOverflow
        self.wrap = wrap
