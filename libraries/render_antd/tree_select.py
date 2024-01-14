from render import Component, create_callback, InputComponent


class TreeSelect(InputComponent):
    Module = "ant"
    JSXName = "TreeSelect"
    InputName = "value"

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
        defaultValue=None,
        value=None,
        allowClear=None,
        autoClearSearchValue=None,
        bordered=None,
        disabled=None,
        dropdownRender=None,
        dropdownStyle=None,
        fieldNames=None,
        filterTreeNode=None,
        getPopupContainer=None,
        labelInValue=None,
        listHeight=None,
        loadData=None,
        maxTagCount=None,
        maxTagPlaceholder=None,
        maxTagTextLength=None,
        multiple=None,
        notFoundContent=None,
        onDropdownVisibleChange=None,
        onSearch=None,
        onSelect=None,
        onTreeExpand=None,
        placeholder=None,
        placement=None,
        popupClassName=None,
        popupMatchSelectWidth=None,
        searchValue=None,
        showCheckedStrategy=None,
        showSearch=None,
        size=None,
        status=None,
        suffixIcon=None,
        switcherIcon=None,
        tagRender=None,
        treeCheckStrictly=None,
        treeCheckable=None,
        treeData=None,
        treeDataSimpleMode=None,
        treeDefaultExpandAll=None,
        treeDefaultExpandedKeys=None,
        treeExpandAction=None,
        treeExpandedKeys=None,
        treeIcon=None,
        treeLine=None,
        treeLoadedKeys=None,
        treeNodeFilterProp=None,
        treeNodeLabelProp=None,
        virtual=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowClear = allowClear
        self.autoClearSearchValue = autoClearSearchValue
        self.bordered = bordered
        self.disabled = disabled
        self.dropdownRender = dropdownRender
        self.dropdownStyle = dropdownStyle
        self.fieldNames = fieldNames
        self.filterTreeNode = filterTreeNode
        self.getPopupContainer = getPopupContainer
        self.labelInValue = labelInValue
        self.listHeight = listHeight
        self.loadData = create_callback(
            loadData, "loadData", [[0, "key"]], is_promise=True
        )
        self.maxTagCount = maxTagCount
        self.maxTagPlaceholder = maxTagPlaceholder
        self.maxTagTextLength = maxTagTextLength
        self.multiple = multiple
        self.notFoundContent = notFoundContent
        self.onDropdownVisibleChange = create_callback(
            onDropdownVisibleChange, "onDropdownVisibleChange", []
        )
        self.onSearch = create_callback(onSearch, "onSearch", [])
        self.onSelect = create_callback(onSelect, "onSelect", [])
        self.onTreeExpand = create_callback(onTreeExpand, "onTreeExpand", [[0]])
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.popupMatchSelectWidth = popupMatchSelectWidth
        self.searchValue = searchValue
        self.showCheckedStrategy = showCheckedStrategy
        self.showSearch = showSearch
        self.size = size
        self.status = status
        self.suffixIcon = suffixIcon
        self.switcherIcon = switcherIcon
        self.tagRender = tagRender
        self.treeCheckStrictly = treeCheckStrictly
        self.treeCheckable = treeCheckable
        self.treeData = treeData
        self.treeDataSimpleMode = treeDataSimpleMode
        self.treeDefaultExpandAll = treeDefaultExpandAll
        self.treeDefaultExpandedKeys = treeDefaultExpandedKeys
        self.treeExpandAction = treeExpandAction
        self.treeExpandedKeys = treeExpandedKeys
        self.treeIcon = treeIcon
        self.treeLine = treeLine
        self.treeLoadedKeys = treeLoadedKeys
        self.treeNodeFilterProp = treeNodeFilterProp
        self.treeNodeLabelProp = treeNodeLabelProp
        self.virtual = virtual


class TreeSelectTreeNode(Component):
    Module = "ant"
    JSXName = "TreeSelect.TreeNode"

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
        isLeaf=None,
        selectable=None,
        title=None,
        value=None,
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
        self.isLeaf = isLeaf
        self.selectable = selectable
        self.title = title
        self.value = value
