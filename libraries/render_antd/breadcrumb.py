from render import Component, create_callback


class Breadcrumb(Component):
    Module = "antd"
    JSXName = "Breadcrumb"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "itemRender",
        "items",
        "params",
        "separator",
        "type",
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
        itemRender=None,
        items=None,
        params=None,
        separator=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.itemRender = itemRender
        self.items = items
        self.params = params
        self.separator = separator
        self.type = type
