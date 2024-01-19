from render import Component, create_callback


class Tree(Component):
    Module = "antd"
    JSXName = "Tree"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "loadData",
        "onCheck",
        "onDragEnd",
        "onDragEnter",
        "onDragLeave",
        "onDragOver",
        "onDragStart",
        "onDrop",
        "onExpand",
        "onLoad",
        "onRightClick",
        "onSelect",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowDrop",
        "autoExpandParent",
        "blockNode",
        "checkStrictly",
        "checkable",
        "checkedKeys",
        "defaultCheckedKeys",
        "defaultExpandAll",
        "defaultExpandParent",
        "defaultExpandedKeys",
        "defaultSelectedKeys",
        "disabled",
        "draggable",
        "expandedKeys",
        "fieldNames",
        "filterTreeNode",
        "height",
        "icon",
        "loadedKeys",
        "multiple",
        "rootStyle",
        "selectable",
        "selectedKeys",
        "showIcon",
        "showLine",
        "switcherIcon",
        "titleRender",
        "treeData",
        "virtual",
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
        allowDrop=None,
        autoExpandParent=None,
        blockNode=None,
        checkStrictly=None,
        checkable=None,
        checkedKeys=None,
        defaultCheckedKeys=None,
        defaultExpandAll=None,
        defaultExpandParent=None,
        defaultExpandedKeys=None,
        defaultSelectedKeys=None,
        disabled=None,
        draggable=None,
        expandedKeys=None,
        fieldNames=None,
        filterTreeNode=None,
        height=None,
        icon=None,
        loadData=None,
        loadedKeys=None,
        multiple=None,
        onCheck=None,
        onDragEnd=None,
        onDragEnter=None,
        onDragLeave=None,
        onDragOver=None,
        onDragStart=None,
        onDrop=None,
        onExpand=None,
        onLoad=None,
        onRightClick=None,
        onSelect=None,
        rootStyle=None,
        selectable=None,
        selectedKeys=None,
        showIcon=None,
        showLine=None,
        switcherIcon=None,
        titleRender=None,
        treeData=None,
        virtual=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowDrop = allowDrop
        self.autoExpandParent = autoExpandParent
        self.blockNode = blockNode
        self.checkStrictly = checkStrictly
        self.checkable = checkable
        self.checkedKeys = checkedKeys
        self.defaultCheckedKeys = defaultCheckedKeys
        self.defaultExpandAll = defaultExpandAll
        self.defaultExpandParent = defaultExpandParent
        self.defaultExpandedKeys = defaultExpandedKeys
        self.defaultSelectedKeys = defaultSelectedKeys
        self.disabled = disabled
        self.draggable = draggable
        self.expandedKeys = expandedKeys
        self.fieldNames = fieldNames
        self.filterTreeNode = filterTreeNode
        self.height = height
        self.icon = icon
        self.loadData = create_callback(
            loadData, "loadData", [[0, "key"]], is_promise=True
        )
        self.loadedKeys = loadedKeys
        self.multiple = multiple
        self.onCheck = create_callback(onCheck, "onCheck", [[1, "node", "key"]])
        self.onDragEnd = create_callback(onDragEnd, "onDragEnd", [[0, "node", "key"]])
        self.onDragEnter = create_callback(
            onDragEnter, "onDragEnter", [[0, "node", "key"]]
        )
        self.onDragLeave = create_callback(
            onDragLeave, "onDragLeave", [[0, "node", "key"]]
        )
        self.onDragOver = create_callback(
            onDragOver, "onDragOver", [[0, "node", "key"]]
        )
        self.onDragStart = create_callback(
            onDragStart, "onDragStart", [[0, "node", "key"]]
        )
        self.onDrop = create_callback(onDrop, "onDrop", [[0, "node", "key"]])
        self.onExpand = create_callback(onExpand, "onExpand", [[1, "node", "key"]])
        self.onLoad = create_callback(onLoad, "onLoad", [[1, "node", "key"]])
        self.onRightClick = create_callback(
            onRightClick, "onRightClick", [[0, "node", "key"]]
        )
        self.onSelect = create_callback(onSelect, "onSelect", [[0]])
        self.rootStyle = rootStyle
        self.selectable = selectable
        self.selectedKeys = selectedKeys
        self.showIcon = showIcon
        self.showLine = showLine
        self.switcherIcon = switcherIcon
        self.titleRender = titleRender
        self.treeData = treeData
        self.virtual = virtual


class TreeNode(Component):
    Module = "antd"
    JSXName = "Tree.TreeNode"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "checkable",
        "disableCheckbox",
        "disabled",
        "icon",
        "isLeaf",
        "selectable",
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
        checkable=None,
        disableCheckbox=None,
        disabled=None,
        icon=None,
        isLeaf=None,
        selectable=None,
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
        self.checkable = checkable
        self.disableCheckbox = disableCheckbox
        self.disabled = disabled
        self.icon = icon
        self.isLeaf = isLeaf
        self.selectable = selectable
        self.title = title
