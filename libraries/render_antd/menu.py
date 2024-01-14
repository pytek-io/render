from render import Component, create_callback, Props


class Menu(Component):
    Module = "ant"
    JSXName = "Menu"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        danger=None,
        dashed=None,
        defaultOpenKeys=None,
        defaultSelectedKeys=None,
        disabled=None,
        expandIcon=None,
        forceSubMenuRender=None,
        icon=None,
        inlineCollapsed=None,
        inlineIndent=None,
        items=None,
        label=None,
        mode=None,
        multiple=None,
        onDeselect=None,
        onOpenChange=None,
        onSelect=None,
        onTitleClick=None,
        openKeys=None,
        overflowedIndicator=None,
        popupClassName=None,
        popupOffset=None,
        selectable=None,
        selectedKeys=None,
        subMenuCloseDelay=None,
        subMenuOpenDelay=None,
        theme=None,
        title=None,
        triggerSubMenuAction=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick", [[0, "key"]])
        self.danger = danger
        self.dashed = dashed
        self.defaultOpenKeys = defaultOpenKeys
        self.defaultSelectedKeys = defaultSelectedKeys
        self.disabled = disabled
        self.expandIcon = expandIcon
        self.forceSubMenuRender = forceSubMenuRender
        self.icon = icon
        self.inlineCollapsed = inlineCollapsed
        self.inlineIndent = inlineIndent
        self.items = items
        self.label = label
        self.mode = mode
        self.multiple = multiple
        self.onDeselect = create_callback(onDeselect, "onDeselect", [[0, "key"]])
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [])
        self.onSelect = create_callback(onSelect, "onSelect", [[0, "key"]])
        self.onTitleClick = create_callback(onTitleClick, "onTitleClick", [[0, "key"]])
        self.openKeys = openKeys
        self.overflowedIndicator = overflowedIndicator
        self.popupClassName = popupClassName
        self.popupOffset = popupOffset
        self.selectable = selectable
        self.selectedKeys = selectedKeys
        self.subMenuCloseDelay = subMenuCloseDelay
        self.subMenuOpenDelay = subMenuOpenDelay
        self.theme = theme
        self.title = title
        self.triggerSubMenuAction = triggerSubMenuAction


class MenuProps(Props):
    def __init__(
        self,
        children=None,
        danger=None,
        dashed=None,
        defaultOpenKeys=None,
        defaultSelectedKeys=None,
        disabled=None,
        expandIcon=None,
        forceSubMenuRender=None,
        icon=None,
        inlineCollapsed=None,
        inlineIndent=None,
        items=None,
        key=None,
        label=None,
        mode=None,
        multiple=None,
        onClick=None,
        onDeselect=None,
        onOpenChange=None,
        onSelect=None,
        onTitleClick=None,
        openKeys=None,
        overflowedIndicator=None,
        popupClassName=None,
        popupOffset=None,
        selectable=None,
        selectedKeys=None,
        style=None,
        subMenuCloseDelay=None,
        subMenuOpenDelay=None,
        theme=None,
        title=None,
        triggerSubMenuAction=None,
    ):
        self.children = children
        self.danger = danger
        self.dashed = dashed
        self.defaultOpenKeys = defaultOpenKeys
        self.defaultSelectedKeys = defaultSelectedKeys
        self.disabled = disabled
        self.expandIcon = expandIcon
        self.forceSubMenuRender = forceSubMenuRender
        self.icon = icon
        self.inlineCollapsed = inlineCollapsed
        self.inlineIndent = inlineIndent
        self.items = items
        self.key = key
        self.label = label
        self.mode = mode
        self.multiple = multiple
        self.onClick = create_callback(onClick, "onClick", [[0, "key"]])
        self.onDeselect = create_callback(onDeselect, "onDeselect", [[0, "key"]])
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [])
        self.onSelect = create_callback(onSelect, "onSelect", [[0, "key"]])
        self.onTitleClick = create_callback(onTitleClick, "onTitleClick", [[0, "key"]])
        self.openKeys = openKeys
        self.overflowedIndicator = overflowedIndicator
        self.popupClassName = popupClassName
        self.popupOffset = popupOffset
        self.selectable = selectable
        self.selectedKeys = selectedKeys
        self.style = style
        self.subMenuCloseDelay = subMenuCloseDelay
        self.subMenuOpenDelay = subMenuOpenDelay
        self.theme = theme
        self.title = title
        self.triggerSubMenuAction = triggerSubMenuAction
