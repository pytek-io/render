from render import Component, create_callback, InputComponent


class ColorPicker(InputComponent):
    Module = "antd"
    JSXName = "ColorPicker"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onChangeComplete",
        "onClear",
        "onFormatChange",
        "onOpenChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "arrow",
        "defaultFormat",
        "destroyTooltipOnHide",
        "disabled",
        "disabledAlpha",
        "format",
        "open",
        "panelRender",
        "placement",
        "presets",
        "showText",
        "size",
        "trigger",
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
        arrow=None,
        defaultFormat=None,
        destroyTooltipOnHide=None,
        disabled=None,
        disabledAlpha=None,
        format=None,
        onChangeComplete=None,
        onClear=None,
        onFormatChange=None,
        onOpenChange=None,
        open=None,
        panelRender=None,
        placement=None,
        presets=None,
        showText=None,
        size=None,
        trigger=None,
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
        self.arrow = arrow
        self.defaultFormat = defaultFormat
        self.destroyTooltipOnHide = destroyTooltipOnHide
        self.disabled = disabled
        self.disabledAlpha = disabledAlpha
        self.format = format
        self.onChangeComplete = create_callback(
            onChangeComplete, "onChangeComplete", [[0]]
        )
        self.onClear = create_callback(onClear, "onClear")
        self.onFormatChange = create_callback(onFormatChange, "onFormatChange", [[0]])
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.open = open
        self.panelRender = panelRender
        self.placement = placement
        self.presets = presets
        self.showText = showText
        self.size = size
        self.trigger = trigger
