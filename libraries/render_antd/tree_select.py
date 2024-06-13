from render import Component, create_callback, InputComponent


class TreeSelect(InputComponent):
    Module = "antd"
    JSXName = "TreeSelect"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "loadData",
        "onDropdownVisibleChange",
        "onSearch",
        "onSelect",
        "onTreeExpand",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoClearSearchValue",
        "checkable",
        "disableCheckbox",
        "disabled",
        "dropdownRender",
        "dropdownStyle",
        "fieldNames",
        "filterTreeNode",
        "getPopupContainer",
        "isLeaf",
        "labelInValue",
        "listHeight",
        "maxTagCount",
        "maxTagPlaceholder",
        "maxTagTextLength",
        "multiple",
        "notFoundContent",
        "placeholder",
        "placement",
        "popupClassName",
        "popupMatchSelectWidth",
        "searchValue",
        "selectable",
        "showCheckedStrategy",
        "showSearch",
        "size",
        "status",
        "suffixIcon",
        "switcherIcon",
        "tagRender",
        "title",
        "treeCheckStrictly",
        "treeCheckable",
        "treeData",
        "treeDataSimpleMode",
        "treeDefaultExpandAll",
        "treeDefaultExpandedKeys",
        "treeExpandAction",
        "treeExpandedKeys",
        "treeIcon",
        "treeLine",
        "treeLoadedKeys",
        "treeNodeFilterProp",
        "treeNodeLabelProp",
        "variant",
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
        allowClear=None,
        autoClearSearchValue=None,
        checkable=None,
        disableCheckbox=None,
        disabled=None,
        dropdownRender=None,
        dropdownStyle=None,
        fieldNames=None,
        filterTreeNode=None,
        getPopupContainer=None,
        isLeaf=None,
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
        selectable=None,
        showCheckedStrategy=None,
        showSearch=None,
        size=None,
        status=None,
        suffixIcon=None,
        switcherIcon=None,
        tagRender=None,
        title=None,
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
        variant=None,
        virtual=None,
        controller=None,
        onChange=None,
        value=None,
        defaultValue=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowClear = allowClear
        self.autoClearSearchValue = autoClearSearchValue
        self.checkable = checkable
        self.disableCheckbox = disableCheckbox
        self.disabled = disabled
        self.dropdownRender = dropdownRender
        self.dropdownStyle = dropdownStyle
        self.fieldNames = fieldNames
        self.filterTreeNode = filterTreeNode
        self.getPopupContainer = getPopupContainer
        self.isLeaf = isLeaf
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
            onDropdownVisibleChange, "onDropdownVisibleChange"
        )
        self.onSearch = create_callback(onSearch, "onSearch")
        self.onSelect = create_callback(onSelect, "onSelect")
        self.onTreeExpand = create_callback(onTreeExpand, "onTreeExpand", [[0]])
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.popupMatchSelectWidth = popupMatchSelectWidth
        self.searchValue = searchValue
        self.selectable = selectable
        self.showCheckedStrategy = showCheckedStrategy
        self.showSearch = showSearch
        self.size = size
        self.status = status
        self.suffixIcon = suffixIcon
        self.switcherIcon = switcherIcon
        self.tagRender = tagRender
        self.title = title
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
        self.variant = variant
        self.virtual = virtual
