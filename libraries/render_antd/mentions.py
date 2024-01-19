from render import Component, create_callback


class Mention(Component):
    Module = "ant"
    JSXName = "Mention"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onBlur",
        "onChange",
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
        "autoFocus",
        "autoSize",
        "defaultValue",
        "filterOption",
        "getPopupContainer",
        "notFoundContent",
        "options",
        "placement",
        "prefix",
        "split",
        "status",
        "value",
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
        autoFocus=None,
        autoSize=None,
        defaultValue=None,
        filterOption=None,
        getPopupContainer=None,
        notFoundContent=None,
        onBlur=None,
        onChange=None,
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
        self.autoFocus = autoFocus
        self.autoSize = autoSize
        self.defaultValue = defaultValue
        self.filterOption = filterOption
        self.getPopupContainer = getPopupContainer
        self.notFoundContent = notFoundContent
        self.onBlur = create_callback(onBlur, "onBlur")
        self.onChange = create_callback(onChange, "onChange", [[0]])
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
        self.value = value


class MentionsOption(Component):
    Module = "ant"
    JSXName = "Mentions.Option"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "disabled", "label"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        disabled=None,
        label=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.disabled = disabled
        self.label = label
