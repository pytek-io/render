from render import Component, create_callback, InputComponent


class Select(InputComponent):
    Module = "antd"
    JSXName = "Select"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onBlur",
        "onClear",
        "onDeselect",
        "onDropdownVisibleChange",
        "onFocus",
        "onInputKeyDown",
        "onMouseEnter",
        "onMouseLeave",
        "onPopupScroll",
        "onSearch",
        "onSelect",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoClearSearchValue",
        "autoFocus",
        "defaultActiveFirstOption",
        "defaultOpen",
        "disabled",
        "dropdownRender",
        "dropdownStyle",
        "fieldNames",
        "filterOption",
        "filterSort",
        "getPopupContainer",
        "labelInValue",
        "listHeight",
        "loading",
        "maxCount",
        "maxTagCount",
        "maxTagPlaceholder",
        "maxTagTextLength",
        "menuItemSelectedIcon",
        "mode",
        "notFoundContent",
        "open",
        "optionFilterProp",
        "optionLabelProp",
        "optionRender",
        "options",
        "placeholder",
        "placement",
        "popupClassName",
        "popupMatchSelectWidth",
        "removeIcon",
        "searchValue",
        "showSearch",
        "size",
        "status",
        "suffixIcon",
        "tagRender",
        "tokenSeparators",
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
        onChange=None,
        defaultValue=None,
        value=None,
        allowClear=None,
        autoClearSearchValue=None,
        autoFocus=None,
        defaultActiveFirstOption=None,
        defaultOpen=None,
        disabled=None,
        dropdownRender=None,
        dropdownStyle=None,
        fieldNames=None,
        filterOption=None,
        filterSort=None,
        getPopupContainer=None,
        labelInValue=None,
        listHeight=None,
        loading=None,
        maxCount=None,
        maxTagCount=None,
        maxTagPlaceholder=None,
        maxTagTextLength=None,
        menuItemSelectedIcon=None,
        mode=None,
        notFoundContent=None,
        onBlur=None,
        onClear=None,
        onDeselect=None,
        onDropdownVisibleChange=None,
        onFocus=None,
        onInputKeyDown=None,
        onMouseEnter=None,
        onMouseLeave=None,
        onPopupScroll=None,
        onSearch=None,
        onSelect=None,
        open=None,
        optionFilterProp=None,
        optionLabelProp=None,
        optionRender=None,
        options=None,
        placeholder=None,
        placement=None,
        popupClassName=None,
        popupMatchSelectWidth=None,
        removeIcon=None,
        searchValue=None,
        showSearch=None,
        size=None,
        status=None,
        suffixIcon=None,
        tagRender=None,
        tokenSeparators=None,
        variant=None,
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
        self.autoFocus = autoFocus
        self.defaultActiveFirstOption = defaultActiveFirstOption
        self.defaultOpen = defaultOpen
        self.disabled = disabled
        self.dropdownRender = dropdownRender
        self.dropdownStyle = dropdownStyle
        self.fieldNames = fieldNames
        self.filterOption = filterOption
        self.filterSort = filterSort
        self.getPopupContainer = getPopupContainer
        self.labelInValue = labelInValue
        self.listHeight = listHeight
        self.loading = loading
        self.maxCount = maxCount
        self.maxTagCount = maxTagCount
        self.maxTagPlaceholder = maxTagPlaceholder
        self.maxTagTextLength = maxTagTextLength
        self.menuItemSelectedIcon = menuItemSelectedIcon
        self.mode = mode
        self.notFoundContent = notFoundContent
        self.onBlur = create_callback(onBlur, "onBlur")
        self.onClear = create_callback(onClear, "onClear")
        self.onDeselect = create_callback(onDeselect, "onDeselect", [[0]])
        self.onDropdownVisibleChange = create_callback(
            onDropdownVisibleChange, "onDropdownVisibleChange", [[0]]
        )
        self.onFocus = create_callback(onFocus, "onFocus")
        self.onInputKeyDown = create_callback(onInputKeyDown, "onInputKeyDown")
        self.onMouseEnter = create_callback(onMouseEnter, "onMouseEnter")
        self.onMouseLeave = create_callback(onMouseLeave, "onMouseLeave")
        self.onPopupScroll = create_callback(onPopupScroll, "onPopupScroll")
        self.onSearch = create_callback(onSearch, "onSearch", [[0]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0]])
        self.open = open
        self.optionFilterProp = optionFilterProp
        self.optionLabelProp = optionLabelProp
        self.optionRender = optionRender
        self.options = options
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.popupMatchSelectWidth = popupMatchSelectWidth
        self.removeIcon = removeIcon
        self.searchValue = searchValue
        self.showSearch = showSearch
        self.size = size
        self.status = status
        self.suffixIcon = suffixIcon
        self.tagRender = tagRender
        self.tokenSeparators = tokenSeparators
        self.variant = variant
        self.virtual = virtual
