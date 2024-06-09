from render import Component, create_callback


class Descriptions(Component):
    Module = "antd"
    JSXName = "Descriptions"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "bordered",
        "colon",
        "column",
        "contentStyle",
        "extra",
        "items",
        "labelStyle",
        "layout",
        "size",
        "title",
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
        bordered=None,
        colon=None,
        column=None,
        contentStyle=None,
        extra=None,
        items=None,
        labelStyle=None,
        layout=None,
        size=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.bordered = bordered
        self.colon = colon
        self.column = column
        self.contentStyle = contentStyle
        self.extra = extra
        self.items = items
        self.labelStyle = labelStyle
        self.layout = layout
        self.size = size
        self.title = title

    class Item(Component):
        Module = "antd"
        JSXName = "Descriptions.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "contentStyle",
            "label",
            "labelStyle",
            "span",
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
            contentStyle=None,
            label=None,
            labelStyle=None,
            span=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.contentStyle = contentStyle
            self.label = label
            self.labelStyle = labelStyle
            self.span = span
