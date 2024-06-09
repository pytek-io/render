from render import Component, create_callback, InputComponent


class Cascader(InputComponent):
    Module = "antd"
    JSXName = "Cascader"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "loadData",
        "onDropdownVisibleChange",
        "onSearch",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoClearSearchValue",
        "autoFocus",
        "changeOnSelect",
        "disabled",
        "displayRender",
        "dropdownMenuColumnStyle",
        "dropdownRender",
        "expandIcon",
        "expandTrigger",
        "fieldNames",
        "filter",
        "getPopupContainer",
        "limit",
        "loadingIcon",
        "matchInputWidth",
        "maxTagCount",
        "maxTagPlaceholder",
        "maxTagTextLength",
        "multiple",
        "notFoundContent",
        "open",
        "options",
        "placeholder",
        "placement",
        "popupClassName",
        "removeIcon",
        "render",
        "searchValue",
        "showCheckedStrategy",
        "showSearch",
        "size",
        "sort",
        "status",
        "suffixIcon",
        "tagRender",
        "variant",
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
        changeOnSelect=None,
        disabled=None,
        displayRender=None,
        dropdownMenuColumnStyle=None,
        dropdownRender=None,
        expandIcon=None,
        expandTrigger=None,
        fieldNames=None,
        filter=None,
        getPopupContainer=None,
        limit=None,
        loadData=None,
        loadingIcon=None,
        matchInputWidth=None,
        maxTagCount=None,
        maxTagPlaceholder=None,
        maxTagTextLength=None,
        multiple=None,
        notFoundContent=None,
        onDropdownVisibleChange=None,
        onSearch=None,
        open=None,
        options=None,
        placeholder=None,
        placement=None,
        popupClassName=None,
        removeIcon=None,
        render=None,
        searchValue=None,
        showCheckedStrategy=None,
        showSearch=None,
        size=None,
        sort=None,
        status=None,
        suffixIcon=None,
        tagRender=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowClear = allowClear
        self.autoClearSearchValue = autoClearSearchValue
        self.autoFocus = autoFocus
        self.changeOnSelect = changeOnSelect
        self.disabled = disabled
        self.displayRender = displayRender
        self.dropdownMenuColumnStyle = dropdownMenuColumnStyle
        self.dropdownRender = dropdownRender
        self.expandIcon = expandIcon
        self.expandTrigger = expandTrigger
        self.fieldNames = fieldNames
        self.filter = filter
        self.getPopupContainer = getPopupContainer
        self.limit = limit
        self.loadData = create_callback(loadData, "loadData", [[0]], is_promise=True)
        self.loadingIcon = loadingIcon
        self.matchInputWidth = matchInputWidth
        self.maxTagCount = maxTagCount
        self.maxTagPlaceholder = maxTagPlaceholder
        self.maxTagTextLength = maxTagTextLength
        self.multiple = multiple
        self.notFoundContent = notFoundContent
        self.onDropdownVisibleChange = create_callback(
            onDropdownVisibleChange, "onDropdownVisibleChange"
        )
        self.onSearch = create_callback(onSearch, "onSearch", [[0]])
        self.open = open
        self.options = options
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.removeIcon = removeIcon
        self.render = render
        self.searchValue = searchValue
        self.showCheckedStrategy = showCheckedStrategy
        self.showSearch = showSearch
        self.size = size
        self.sort = sort
        self.status = status
        self.suffixIcon = suffixIcon
        self.tagRender = tagRender
        self.variant = variant
