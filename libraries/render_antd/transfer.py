from render import Component, create_callback, InputComponent


class Transfer(InputComponent):
    Module = "ant"
    JSXName = "Transfer"
    InputName = "targetKeys"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onItemSelect",
        "onItemSelectAll",
        "onScroll",
        "onSearch",
        "onSelectChange",
        "oneWay",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "dataSource",
        "direction",
        "disabled",
        "filterOption",
        "filteredItems",
        "footer",
        "listStyle",
        "locale",
        "operationStyle",
        "operations",
        "pagination",
        "render",
        "selectAllLabels",
        "selectedKeys",
        "selectionsIcon",
        "showSearch",
        "showSelectAll",
        "status",
        "titles",
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
        onChange=None,
        defaultTargetkeys=None,
        targetKeys=None,
        dataSource=None,
        direction=None,
        disabled=None,
        filterOption=None,
        filteredItems=None,
        footer=None,
        listStyle=None,
        locale=None,
        onItemSelect=None,
        onItemSelectAll=None,
        onScroll=None,
        onSearch=None,
        onSelectChange=None,
        oneWay=None,
        operationStyle=None,
        operations=None,
        pagination=None,
        render=None,
        selectAllLabels=None,
        selectedKeys=None,
        selectionsIcon=None,
        showSearch=None,
        showSelectAll=None,
        status=None,
        titles=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, targetKeys, defaultTargetkeys)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.dataSource = dataSource
        self.direction = direction
        self.disabled = disabled
        self.filterOption = filterOption
        self.filteredItems = filteredItems
        self.footer = footer
        self.listStyle = listStyle
        self.locale = locale
        self.onItemSelect = create_callback(onItemSelect, "onItemSelect", [[0], [1]])
        self.onItemSelectAll = create_callback(
            onItemSelectAll, "onItemSelectAll", [[0], [1]]
        )
        self.onScroll = create_callback(onScroll, "onScroll", [[0]])
        self.onSearch = create_callback(onSearch, "onSearch", [[0], [1]])
        self.onSelectChange = create_callback(
            onSelectChange, "onSelectChange", [[0], [1]]
        )
        self.oneWay = create_callback(oneWay, "oneWay")
        self.operationStyle = operationStyle
        self.operations = operations
        self.pagination = pagination
        self.render = render
        self.selectAllLabels = selectAllLabels
        self.selectedKeys = selectedKeys
        self.selectionsIcon = selectionsIcon
        self.showSearch = showSearch
        self.showSelectAll = showSelectAll
        self.status = status
        self.titles = titles
