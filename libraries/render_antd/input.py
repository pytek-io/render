from render import Component, create_callback, InputComponent


class Input(InputComponent):
    Module = "antd"
    JSXName = "Input"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onPressEnter"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "addonAfter",
        "addonBefore",
        "allowClear",
        "bordered",
        "classNames",
        "count",
        "disabled",
        "maxLength",
        "placeholder",
        "prefix",
        "showCount",
        "size",
        "status",
        "styles",
        "suffix",
        "type",
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
        addonAfter=None,
        addonBefore=None,
        allowClear=None,
        bordered=None,
        classNames=None,
        count=None,
        disabled=None,
        maxLength=None,
        onPressEnter=None,
        placeholder=None,
        prefix=None,
        showCount=None,
        size=None,
        status=None,
        styles=None,
        suffix=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.addonAfter = addonAfter
        self.addonBefore = addonBefore
        self.allowClear = allowClear
        self.bordered = bordered
        self.classNames = classNames
        self.count = count
        self.disabled = disabled
        self.maxLength = maxLength
        self.onPressEnter = create_callback(onPressEnter, "onPressEnter")
        self.placeholder = placeholder
        self.prefix = prefix
        self.showCount = showCount
        self.size = size
        self.status = status
        self.styles = styles
        self.suffix = suffix
        self.type = type


class Group(Component):
    Module = "antd"
    JSXName = "Input.Group"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "compact", "size"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        compact=None,
        size=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.compact = compact
        self.size = size


class Password(Component):
    Module = "antd"
    JSXName = "Input.Password"
    CALLBACKS = ["onKeyPress", "onClick", "onVisibleChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "blur",
        "focus",
        "iconRender",
        "visibilityToggle",
        "visible",
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
        blur=None,
        focus=None,
        iconRender=None,
        onVisibleChange=None,
        visibilityToggle=None,
        visible=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.blur = blur
        self.focus = focus
        self.iconRender = iconRender
        self.onVisibleChange = create_callback(onVisibleChange, "onVisibleChange")
        self.visibilityToggle = visibilityToggle
        self.visible = visible


class Search(Component):
    Module = "antd"
    JSXName = "Input.Search"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onPressEnter", "onSearch"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "addonAfter",
        "addonBefore",
        "allowClear",
        "bordered",
        "classNames",
        "count",
        "defaultValue",
        "disabled",
        "enterButton",
        "loading",
        "maxLength",
        "placeholder",
        "prefix",
        "showCount",
        "size",
        "status",
        "styles",
        "suffix",
        "type",
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
        addonAfter=None,
        addonBefore=None,
        allowClear=None,
        bordered=None,
        classNames=None,
        count=None,
        defaultValue=None,
        disabled=None,
        enterButton=None,
        loading=None,
        maxLength=None,
        onChange=None,
        onPressEnter=None,
        onSearch=None,
        placeholder=None,
        prefix=None,
        showCount=None,
        size=None,
        status=None,
        styles=None,
        suffix=None,
        type=None,
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
        self.addonAfter = addonAfter
        self.addonBefore = addonBefore
        self.allowClear = allowClear
        self.bordered = bordered
        self.classNames = classNames
        self.count = count
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.enterButton = enterButton
        self.loading = loading
        self.maxLength = maxLength
        self.onChange = create_callback(onChange, "onChange")
        self.onPressEnter = create_callback(onPressEnter, "onPressEnter")
        self.onSearch = create_callback(onSearch, "onSearch", [[0]])
        self.placeholder = placeholder
        self.prefix = prefix
        self.showCount = showCount
        self.size = size
        self.status = status
        self.styles = styles
        self.suffix = suffix
        self.type = type
        self.value = value


class TextArea(InputComponent):
    Module = "antd"
    JSXName = "Input.TextArea"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onPressEnter", "onResize"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "addonAfter",
        "addonBefore",
        "allowClear",
        "autoSize",
        "bordered",
        "classNames",
        "cols",
        "count",
        "disabled",
        "maxLength",
        "placeholder",
        "prefix",
        "rows",
        "showCount",
        "size",
        "status",
        "styles",
        "suffix",
        "type",
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
        addonAfter=None,
        addonBefore=None,
        allowClear=None,
        autoSize=None,
        bordered=None,
        classNames=None,
        cols=None,
        count=None,
        disabled=None,
        maxLength=None,
        onPressEnter=None,
        onResize=None,
        placeholder=None,
        prefix=None,
        rows=None,
        showCount=None,
        size=None,
        status=None,
        styles=None,
        suffix=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.addonAfter = addonAfter
        self.addonBefore = addonBefore
        self.allowClear = allowClear
        self.autoSize = autoSize
        self.bordered = bordered
        self.classNames = classNames
        self.cols = cols
        self.count = count
        self.disabled = disabled
        self.maxLength = maxLength
        self.onPressEnter = create_callback(onPressEnter, "onPressEnter")
        self.onResize = create_callback(
            onResize, "onResize", [[0, "width"], [0, "height"]]
        )
        self.placeholder = placeholder
        self.prefix = prefix
        self.rows = rows
        self.showCount = showCount
        self.size = size
        self.status = status
        self.styles = styles
        self.suffix = suffix
        self.type = type
