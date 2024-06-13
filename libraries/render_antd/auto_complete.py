from render import Component, create_callback, InputComponent


class AutoComplete(InputComponent):
    Module = "antd"
    JSXName = "AutoComplete"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onBlur",
        "onClear",
        "onDropdownVisibleChange",
        "onFocus",
        "onSearch",
        "onSelect",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoFocus",
        "backfill",
        "defaultActiveFirstOption",
        "defaultOpen",
        "disabled",
        "dropdownMatchSelectWidth",
        "filterOption",
        "notFoundContent",
        "open",
        "options",
        "placeholder",
        "popupClassName",
        "status",
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
        allowClear=None,
        autoFocus=None,
        backfill=None,
        defaultActiveFirstOption=None,
        defaultOpen=None,
        disabled=None,
        dropdownMatchSelectWidth=None,
        filterOption=None,
        notFoundContent=None,
        onBlur=None,
        onClear=None,
        onDropdownVisibleChange=None,
        onFocus=None,
        onSearch=None,
        onSelect=None,
        open=None,
        options=None,
        placeholder=None,
        popupClassName=None,
        status=None,
        variant=None,
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
        self.autoFocus = autoFocus
        self.backfill = backfill
        self.defaultActiveFirstOption = defaultActiveFirstOption
        self.defaultOpen = defaultOpen
        self.disabled = disabled
        self.dropdownMatchSelectWidth = dropdownMatchSelectWidth
        self.filterOption = filterOption
        self.notFoundContent = notFoundContent
        self.onBlur = create_callback(onBlur, "onBlur")
        self.onClear = create_callback(onClear, "onClear")
        self.onDropdownVisibleChange = create_callback(
            onDropdownVisibleChange, "onDropdownVisibleChange"
        )
        self.onFocus = create_callback(onFocus, "onFocus")
        self.onSearch = create_callback(onSearch, "onSearch", [[0]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0]])
        self.open = open
        self.options = options
        self.placeholder = placeholder
        self.popupClassName = popupClassName
        self.status = status
        self.variant = variant
