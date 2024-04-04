from render import Component, create_callback, InputComponent


class Mentions(InputComponent):
    Module = "antd"
    JSXName = "Mentions"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onBlur",
        "onFocus",
        "onResize",
        "onSearch",
        "onSelect",
        "validateSearch",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoFocus",
        "autoSize",
        "filterOption",
        "getPopupContainer",
        "loading",
        "notFoundContent",
        "options",
        "placement",
        "prefix",
        "split",
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
        onChange=None,
        defaultValue=None,
        value=None,
        allowClear=None,
        autoFocus=None,
        autoSize=None,
        filterOption=None,
        getPopupContainer=None,
        loading=None,
        notFoundContent=None,
        onBlur=None,
        onFocus=None,
        onResize=None,
        onSearch=None,
        onSelect=None,
        options=None,
        placement=None,
        prefix=None,
        split=None,
        status=None,
        validateSearch=None,
        variant=None,
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
        self.autoFocus = autoFocus
        self.autoSize = autoSize
        self.filterOption = filterOption
        self.getPopupContainer = getPopupContainer
        self.loading = loading
        self.notFoundContent = notFoundContent
        self.onBlur = create_callback(onBlur, "onBlur")
        self.onFocus = create_callback(onFocus, "onFocus")
        self.onResize = create_callback(
            onResize, "onResize", [[0, "width"], [0, "height"]]
        )
        self.onSearch = create_callback(onSearch, "onSearch", [[0], [1]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0], [1]])
        self.options = options
        self.placement = placement
        self.prefix = prefix
        self.split = split
        self.status = status
        self.validateSearch = create_callback(validateSearch, "validateSearch")
        self.variant = variant
