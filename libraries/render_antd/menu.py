from render import Component, create_callback


class Menu(Component):
    Module = "antd"
    JSXName = "Menu"
    CALLBACKS = ["onKeyPress", "onClick", "onDeselect", "onOpenChange", "onSelect"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "defaultOpenKeys",
        "defaultSelectedKeys",
        "expandIcon",
        "forceSubMenuRender",
        "inlineCollapsed",
        "inlineIndent",
        "items",
        "mode",
        "multiple",
        "openKeys",
        "overflowedIndicator",
        "selectable",
        "selectedKeys",
        "subMenuCloseDelay",
        "subMenuOpenDelay",
        "theme",
        "triggerSubMenuAction",
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
        defaultOpenKeys=None,
        defaultSelectedKeys=None,
        expandIcon=None,
        forceSubMenuRender=None,
        inlineCollapsed=None,
        inlineIndent=None,
        items=None,
        mode=None,
        multiple=None,
        onDeselect=None,
        onOpenChange=None,
        onSelect=None,
        openKeys=None,
        overflowedIndicator=None,
        selectable=None,
        selectedKeys=None,
        subMenuCloseDelay=None,
        subMenuOpenDelay=None,
        theme=None,
        triggerSubMenuAction=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick", [[0, "key"]])
        self.defaultOpenKeys = defaultOpenKeys
        self.defaultSelectedKeys = defaultSelectedKeys
        self.expandIcon = expandIcon
        self.forceSubMenuRender = forceSubMenuRender
        self.inlineCollapsed = inlineCollapsed
        self.inlineIndent = inlineIndent
        self.items = items
        self.mode = mode
        self.multiple = multiple
        self.onDeselect = create_callback(onDeselect, "onDeselect", [[0, "key"]])
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange")
        self.onSelect = create_callback(onSelect, "onSelect", [[0, "key"]])
        self.openKeys = openKeys
        self.overflowedIndicator = overflowedIndicator
        self.selectable = selectable
        self.selectedKeys = selectedKeys
        self.subMenuCloseDelay = subMenuCloseDelay
        self.subMenuOpenDelay = subMenuOpenDelay
        self.theme = theme
        self.triggerSubMenuAction = triggerSubMenuAction
