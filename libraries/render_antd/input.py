from render import Component, create_callback, InputComponent


class Input(InputComponent):
    Module = "antd"
    JSXName = "Input"
    InputName = "value"
    NewValuePath = "target.value"
    CALLBACKS = ["onKeyPress", "onClick", "onPressEnter"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "addonAfter",
        "addonBefore",
        "allowClear",
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
        addonAfter=None,
        addonBefore=None,
        allowClear=None,
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
        self.addonAfter = addonAfter
        self.addonBefore = addonBefore
        self.allowClear = allowClear
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
        self.variant = variant

    class Group(InputComponent):
        Module = "antd"
        JSXName = "Input.Group"
        InputName = "value"
        NewValuePath = "target.value"
        CALLBACKS = ["onKeyPress", "onClick", "onPressEnter"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "addonAfter",
            "addonBefore",
            "allowClear",
            "classNames",
            "compact",
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
            addonAfter=None,
            addonBefore=None,
            allowClear=None,
            classNames=None,
            compact=None,
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
            self.addonAfter = addonAfter
            self.addonBefore = addonBefore
            self.allowClear = allowClear
            self.classNames = classNames
            self.compact = compact
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
            self.variant = variant

    class Password(InputComponent):
        Module = "antd"
        JSXName = "Input.Password"
        InputName = "value"
        NewValuePath = "target.value"
        CALLBACKS = ["onKeyPress", "onClick", "onPressEnter"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "addonAfter",
            "addonBefore",
            "allowClear",
            "classNames",
            "count",
            "disabled",
            "iconRender",
            "maxLength",
            "placeholder",
            "prefix",
            "showCount",
            "size",
            "status",
            "styles",
            "suffix",
            "type",
            "variant",
            "visibilityToggle",
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
            classNames=None,
            count=None,
            disabled=None,
            iconRender=None,
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
            variant=None,
            visibilityToggle=None,
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
            self.addonAfter = addonAfter
            self.addonBefore = addonBefore
            self.allowClear = allowClear
            self.classNames = classNames
            self.count = count
            self.disabled = disabled
            self.iconRender = iconRender
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
            self.variant = variant
            self.visibilityToggle = visibilityToggle

    class Search(InputComponent):
        Module = "antd"
        JSXName = "Input.Search"
        InputName = "value"
        NewValuePath = "target.value"
        CALLBACKS = ["onKeyPress", "onClick", "onPressEnter", "onSearch"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "addonAfter",
            "addonBefore",
            "allowClear",
            "classNames",
            "count",
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
            addonAfter=None,
            addonBefore=None,
            allowClear=None,
            classNames=None,
            count=None,
            disabled=None,
            enterButton=None,
            loading=None,
            maxLength=None,
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
            self.addonAfter = addonAfter
            self.addonBefore = addonBefore
            self.allowClear = allowClear
            self.classNames = classNames
            self.count = count
            self.disabled = disabled
            self.enterButton = enterButton
            self.loading = loading
            self.maxLength = maxLength
            self.onPressEnter = create_callback(onPressEnter, "onPressEnter")
            self.onSearch = create_callback(onSearch, "onSearch", [[0], [2, "source"]])
            self.placeholder = placeholder
            self.prefix = prefix
            self.showCount = showCount
            self.size = size
            self.status = status
            self.styles = styles
            self.suffix = suffix
            self.type = type
            self.variant = variant

    class TextArea(InputComponent):
        Module = "antd"
        JSXName = "Input.TextArea"
        InputName = "value"
        NewValuePath = "target.value"
        CALLBACKS = ["onKeyPress", "onClick", "onPressEnter"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "addonAfter",
            "addonBefore",
            "allowClear",
            "autoSize",
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
            addonAfter=None,
            addonBefore=None,
            allowClear=None,
            autoSize=None,
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
            self.addonAfter = addonAfter
            self.addonBefore = addonBefore
            self.allowClear = allowClear
            self.autoSize = autoSize
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
            self.variant = variant
