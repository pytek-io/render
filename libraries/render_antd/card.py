from render import Component, create_callback, Props


class Card(Component):
    Module = "antd"
    JSXName = "Card"
    CALLBACKS = ["onKeyPress", "onClick", "onTabChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "actions",
        "activeTabKey",
        "bodyStyle",
        "bordered",
        "cover",
        "defaultActiveTabKey",
        "extra",
        "headStyle",
        "hoverable",
        "loading",
        "size",
        "tabBarExtraContent",
        "tabList",
        "tabProps",
        "title",
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
        actions=None,
        activeTabKey=None,
        bodyStyle=None,
        bordered=None,
        cover=None,
        defaultActiveTabKey=None,
        extra=None,
        headStyle=None,
        hoverable=None,
        loading=None,
        onTabChange=None,
        size=None,
        tabBarExtraContent=None,
        tabList=None,
        tabProps=None,
        title=None,
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
        self.actions = actions
        self.activeTabKey = activeTabKey
        self.bodyStyle = bodyStyle
        self.bordered = bordered
        self.cover = cover
        self.defaultActiveTabKey = defaultActiveTabKey
        self.extra = extra
        self.headStyle = headStyle
        self.hoverable = hoverable
        self.loading = loading
        self.onTabChange = create_callback(onTabChange, "onTabChange", [[0]])
        self.size = size
        self.tabBarExtraContent = tabBarExtraContent
        self.tabList = tabList
        self.tabProps = tabProps
        self.title = title
        self.type = type


class Grid(Component):
    Module = "antd"
    JSXName = "Card.Grid"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "hoverable"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        hoverable=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.hoverable = hoverable


class Meta(Component):
    Module = "antd"
    JSXName = "Card.Meta"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "avatar", "description", "title"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        avatar=None,
        description=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.avatar = avatar
        self.description = description
        self.title = title
