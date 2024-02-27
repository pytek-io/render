from render import Component, create_callback


class Grid(Component):
    Module = "mantine"
    JSXName = "Grid"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "columns",
        "grow",
        "gutter",
        "justify",
        "overflow",
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
        columns=None,
        grow=None,
        gutter=None,
        justify=None,
        overflow=None,
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
        self.columns = columns
        self.grow = grow
        self.gutter = gutter
        self.justify = justify
        self.overflow = overflow

    class Col(Component):
        Module = "mantine"
        JSXName = "Grid.Col"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "offset", "order", "span"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            offset=None,
            order=None,
            span=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.offset = offset
            self.order = order
            self.span = span
