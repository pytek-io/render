from render import Component, create_callback, Props


class Breadcrumb(Component):
    Module = "ant"
    JSXName = "Breadcrumb"

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


class RouteItemType(Component):
    Module = "ant"
    JSXName = "RouteItemType"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        dropdownProps=None,
        href=None,
        menu=None,
        path=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick", [])
        self.dropdownProps = dropdownProps
        self.href = href
        self.menu = menu
        self.path = path
        self.title = title


class SeparatorType(Component):
    Module = "ant"
    JSXName = "SeparatorType"

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
        self.separator = separator
        self.type = type
