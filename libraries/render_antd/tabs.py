from render import Component, create_callback


class TabItemType(Component):
    Module = "ant"
    JSXName = "TabItemType"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        closeIcon=None,
        destroyInactiveTabPane=None,
        disabled=None,
        forceRender=None,
        label=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.closeIcon = closeIcon
        self.destroyInactiveTabPane = destroyInactiveTabPane
        self.disabled = disabled
        self.forceRender = forceRender
        self.label = label


class Tabs(Component):
    Module = "ant"
    JSXName = "Tabs"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        activeKey=None,
        addIcon=None,
        animated=None,
        centered=None,
        defaultActiveKey=None,
        destroyInactiveTabPane=None,
        hideAdd=None,
        indicatorSize=None,
        items=None,
        moreIcon=None,
        onChange=None,
        onEdit=None,
        onTabClick=None,
        onTabScroll=None,
        popupClassName=None,
        renderTabBar=None,
        size=None,
        tabBarExtraContent=None,
        tabBarGutter=None,
        tabBarStyle=None,
        tabPosition=None,
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
        self.activeKey = activeKey
        self.addIcon = addIcon
        self.animated = animated
        self.centered = centered
        self.defaultActiveKey = defaultActiveKey
        self.destroyInactiveTabPane = destroyInactiveTabPane
        self.hideAdd = hideAdd
        self.indicatorSize = indicatorSize
        self.items = items
        self.moreIcon = moreIcon
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onEdit = create_callback(onEdit, "onEdit", [[1]])
        self.onTabClick = create_callback(onTabClick, "onTabClick", [[0]])
        self.onTabScroll = create_callback(
            onTabScroll, "onTabScroll", [[0, "direction"]]
        )
        self.popupClassName = popupClassName
        self.renderTabBar = renderTabBar
        self.size = size
        self.tabBarExtraContent = tabBarExtraContent
        self.tabBarGutter = tabBarGutter
        self.tabBarStyle = tabBarStyle
        self.tabPosition = tabPosition
        self.type = type
