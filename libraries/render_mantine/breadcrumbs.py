from render import Component, create_callback


class Breadcrumbs(Component):
    Module = "mantine"
    JSXName = "Breadcrumbs"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "separator", "separatorMargin"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        separator=None,
        separatorMargin=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.separator = separator
        self.separatorMargin = separatorMargin
