from render import Component, create_callback, InputComponent


class TimePicker(InputComponent):
    Module = "antd"
    JSXName = "TimePicker"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onOpenChange", "onSelect"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoFocus",
        "bordered",
        "cellRender",
        "changeOnBlur",
        "disabled",
        "disabledTime",
        "format",
        "getPopupContainer",
        "hideDisabledOptions",
        "hourStep",
        "inputReadOnly",
        "minuteStep",
        "open",
        "placeholder",
        "placement",
        "popupClassName",
        "popupStyle",
        "renderExtraFooter",
        "secondStep",
        "showNow",
        "size",
        "status",
        "suffixIcon",
        "use12Hours",
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
        bordered=None,
        cellRender=None,
        changeOnBlur=None,
        disabled=None,
        disabledTime=None,
        format=None,
        getPopupContainer=None,
        hideDisabledOptions=None,
        hourStep=None,
        inputReadOnly=None,
        minuteStep=None,
        onOpenChange=None,
        onSelect=None,
        open=None,
        placeholder=None,
        placement=None,
        popupClassName=None,
        popupStyle=None,
        renderExtraFooter=None,
        secondStep=None,
        showNow=None,
        size=None,
        status=None,
        suffixIcon=None,
        use12Hours=None,
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
        self.bordered = bordered
        self.cellRender = cellRender
        self.changeOnBlur = changeOnBlur
        self.disabled = disabled
        self.disabledTime = disabledTime
        self.format = format
        self.getPopupContainer = getPopupContainer
        self.hideDisabledOptions = hideDisabledOptions
        self.hourStep = hourStep
        self.inputReadOnly = inputReadOnly
        self.minuteStep = minuteStep
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0]])
        self.open = open
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.popupStyle = popupStyle
        self.renderExtraFooter = renderExtraFooter
        self.secondStep = secondStep
        self.showNow = showNow
        self.size = size
        self.status = status
        self.suffixIcon = suffixIcon
        self.use12Hours = use12Hours


class RangePicker(Component):
    Module = "antd"
    JSXName = "TimePicker.RangePicker"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onOpenChange", "onSelect"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoFocus",
        "bordered",
        "cellRender",
        "changeOnBlur",
        "defaultValue",
        "disabled",
        "disabledTime",
        "format",
        "getPopupContainer",
        "hideDisabledOptions",
        "hourStep",
        "inputReadOnly",
        "minuteStep",
        "open",
        "placeholder",
        "placement",
        "popupClassName",
        "popupStyle",
        "renderExtraFooter",
        "secondStep",
        "showNow",
        "size",
        "status",
        "suffixIcon",
        "use12Hours",
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
        allowClear=None,
        autoFocus=None,
        bordered=None,
        cellRender=None,
        changeOnBlur=None,
        defaultValue=None,
        disabled=None,
        disabledTime=None,
        format=None,
        getPopupContainer=None,
        hideDisabledOptions=None,
        hourStep=None,
        inputReadOnly=None,
        minuteStep=None,
        onChange=None,
        onOpenChange=None,
        onSelect=None,
        open=None,
        placeholder=None,
        placement=None,
        popupClassName=None,
        popupStyle=None,
        renderExtraFooter=None,
        secondStep=None,
        showNow=None,
        size=None,
        status=None,
        suffixIcon=None,
        use12Hours=None,
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
        self.allowClear = allowClear
        self.autoFocus = autoFocus
        self.bordered = bordered
        self.cellRender = cellRender
        self.changeOnBlur = changeOnBlur
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.disabledTime = disabledTime
        self.format = format
        self.getPopupContainer = getPopupContainer
        self.hideDisabledOptions = hideDisabledOptions
        self.hourStep = hourStep
        self.inputReadOnly = inputReadOnly
        self.minuteStep = minuteStep
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0]])
        self.open = open
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.popupStyle = popupStyle
        self.renderExtraFooter = renderExtraFooter
        self.secondStep = secondStep
        self.showNow = showNow
        self.size = size
        self.status = status
        self.suffixIcon = suffixIcon
        self.use12Hours = use12Hours
        self.value = value
