from render import Component, create_callback


class Col(Component):
    Module = "antd"
    JSXName = "Col"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "flex",
        "lg",
        "md",
        "offset",
        "order",
        "pull",
        "push",
        "sm",
        "span",
        "xl",
        "xs",
        "xxl",
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
        flex=None,
        lg=None,
        md=None,
        offset=None,
        order=None,
        pull=None,
        push=None,
        sm=None,
        span=None,
        xl=None,
        xs=None,
        xxl=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.flex = flex
        self.lg = lg
        self.md = md
        self.offset = offset
        self.order = order
        self.pull = pull
        self.push = push
        self.sm = sm
        self.span = span
        self.xl = xl
        self.xs = xs
        self.xxl = xxl


class Row(Component):
    Module = "antd"
    JSXName = "Row"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "align", "gutter", "justify", "wrap"]

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
        gutter=None,
        justify=None,
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
        self.gutter = gutter
        self.justify = justify
        self.wrap = wrap
