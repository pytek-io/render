from render import Component, create_callback, InputComponent


class DatePicker(InputComponent):
    Module = "antd"
    JSXName = "DatePicker"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onOk", "onOpenChange", "onPanelChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowClear",
        "autoFocus",
        "bordered",
        "cellRender",
        "changeOnBlur",
        "dateRender",
        "disabled",
        "disabledDate",
        "disabledTime",
        "format",
        "getPopupContainer",
        "inputReadOnly",
        "locale",
        "mode",
        "nextIcon",
        "open",
        "panelRender",
        "picker",
        "placeholder",
        "placement",
        "popupClassName",
        "popupStyle",
        "presets",
        "prevIcon",
        "renderExtraFooter",
        "showNow",
        "showTime",
        "showTime_defaultValue",
        "showToday",
        "size",
        "status",
        "suffixIcon",
        "superNextIcon",
        "superPrevIcon",
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
        dateRender=None,
        disabled=None,
        disabledDate=None,
        disabledTime=None,
        format=None,
        getPopupContainer=None,
        inputReadOnly=None,
        locale=None,
        mode=None,
        nextIcon=None,
        onOk=None,
        onOpenChange=None,
        onPanelChange=None,
        open=None,
        panelRender=None,
        picker=None,
        placeholder=None,
        placement=None,
        popupClassName=None,
        popupStyle=None,
        presets=None,
        prevIcon=None,
        renderExtraFooter=None,
        showNow=None,
        showTime=None,
        showTime_defaultValue=None,
        showToday=None,
        size=None,
        status=None,
        suffixIcon=None,
        superNextIcon=None,
        superPrevIcon=None,
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
        self.dateRender = dateRender
        self.disabled = disabled
        self.disabledDate = disabledDate
        self.disabledTime = disabledTime
        self.format = format
        self.getPopupContainer = getPopupContainer
        self.inputReadOnly = inputReadOnly
        self.locale = locale
        self.mode = mode
        self.nextIcon = nextIcon
        self.onOk = create_callback(onOk, "onOk")
        self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
        self.onPanelChange = create_callback(onPanelChange, "onPanelChange", [[0], [1]])
        self.open = open
        self.panelRender = panelRender
        self.picker = picker
        self.placeholder = placeholder
        self.placement = placement
        self.popupClassName = popupClassName
        self.popupStyle = popupStyle
        self.presets = presets
        self.prevIcon = prevIcon
        self.renderExtraFooter = renderExtraFooter
        self.showNow = showNow
        self.showTime = showTime
        self.showTime_defaultValue = showTime_defaultValue
        self.showToday = showToday
        self.size = size
        self.status = status
        self.suffixIcon = suffixIcon
        self.superNextIcon = superNextIcon
        self.superPrevIcon = superPrevIcon


class RangePicker(InputComponent):
    Module = "antd"
    JSXName = "DatePicker.RangePicker"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onCalendarChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowEmpty",
        "cellRender",
        "dateRender",
        "disabled",
        "disabledTime",
        "format",
        "presets",
        "renderExtraFooter",
        "separator",
        "showTime",
        "showTime_defaultValue",
        "picker",
        "bordered",
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
        allowEmpty=None,
        cellRender=None,
        dateRender=None,
        disabled=None,
        disabledTime=None,
        format=None,
        onCalendarChange=None,
        presets=None,
        renderExtraFooter=None,
        separator=None,
        showTime=None,
        showTime_defaultValue=None,
        picker=None,
        bordered=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowEmpty = allowEmpty
        self.cellRender = cellRender
        self.dateRender = dateRender
        self.disabled = disabled
        self.disabledTime = disabledTime
        self.format = format
        self.onCalendarChange = create_callback(
            onCalendarChange, "onCalendarChange", [[], [], [2, "range"]]
        )
        self.presets = presets
        self.renderExtraFooter = renderExtraFooter
        self.separator = separator
        self.showTime = showTime
        self.showTime_defaultValue = showTime_defaultValue
        self.picker = picker
        self.bordered = bordered
