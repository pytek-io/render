from render import Component, create_callback, InputComponent


class DatePicker(InputComponent):
    Module = "antd"
    JSXName = "DatePicker"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onOk", "onPanelChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "defaultPickerValue",
        "disabledTime",
        "format",
        "multiple",
        "pickerValue",
        "renderExtraFooter",
        "showNow",
        "showTime",
        "showTime_defaultValue",
        "showWeek",
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
        defaultPickerValue=None,
        disabledTime=None,
        format=None,
        multiple=None,
        onOk=None,
        onPanelChange=None,
        pickerValue=None,
        renderExtraFooter=None,
        showNow=None,
        showTime=None,
        showTime_defaultValue=None,
        showWeek=None,
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
        self.defaultPickerValue = defaultPickerValue
        self.disabledTime = disabledTime
        self.format = format
        self.multiple = multiple
        self.onOk = create_callback(onOk, "onOk")
        self.onPanelChange = create_callback(onPanelChange, "onPanelChange", [[0], [1]])
        self.pickerValue = pickerValue
        self.renderExtraFooter = renderExtraFooter
        self.showNow = showNow
        self.showTime = showTime
        self.showTime_defaultValue = showTime_defaultValue
        self.showWeek = showWeek

    class RangePicker(InputComponent):
        Module = "antd"
        JSXName = "DatePicker.RangePicker"
        InputName = "value"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onBlur",
            "onCalendarChange",
            "onFocus",
            "onOk",
            "onOpenChange",
            "onPanelChange",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "allowClear",
            "allowEmpty",
            "autoFocus",
            "cellRender",
            "components",
            "dateRender",
            "defaultPickerValue",
            "disabled",
            "disabledDate",
            "disabledTime",
            "format",
            "getPopupContainer",
            "inputReadOnly",
            "locale",
            "maxDate",
            "minDate",
            "mode",
            "multiple",
            "needConfirm",
            "nextIcon",
            "open",
            "order",
            "panelRender",
            "picker",
            "pickerValue",
            "placeholder",
            "placement",
            "popupClassName",
            "popupStyle",
            "preserveInvalidOnBlur",
            "presets",
            "prevIcon",
            "renderExtraFooter",
            "separator",
            "showNow",
            "showTime",
            "showTime_defaultValue",
            "showWeek",
            "size",
            "status",
            "suffixIcon",
            "superNextIcon",
            "superPrevIcon",
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
            allowEmpty=None,
            autoFocus=None,
            cellRender=None,
            components=None,
            dateRender=None,
            defaultPickerValue=None,
            disabled=None,
            disabledDate=None,
            disabledTime=None,
            format=None,
            getPopupContainer=None,
            inputReadOnly=None,
            locale=None,
            maxDate=None,
            minDate=None,
            mode=None,
            multiple=None,
            needConfirm=None,
            nextIcon=None,
            onBlur=None,
            onCalendarChange=None,
            onFocus=None,
            onOk=None,
            onOpenChange=None,
            onPanelChange=None,
            open=None,
            order=None,
            panelRender=None,
            picker=None,
            pickerValue=None,
            placeholder=None,
            placement=None,
            popupClassName=None,
            popupStyle=None,
            preserveInvalidOnBlur=None,
            presets=None,
            prevIcon=None,
            renderExtraFooter=None,
            separator=None,
            showNow=None,
            showTime=None,
            showTime_defaultValue=None,
            showWeek=None,
            size=None,
            status=None,
            suffixIcon=None,
            superNextIcon=None,
            superPrevIcon=None,
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
            self.allowEmpty = allowEmpty
            self.autoFocus = autoFocus
            self.cellRender = cellRender
            self.components = components
            self.dateRender = dateRender
            self.defaultPickerValue = defaultPickerValue
            self.disabled = disabled
            self.disabledDate = disabledDate
            self.disabledTime = disabledTime
            self.format = format
            self.getPopupContainer = getPopupContainer
            self.inputReadOnly = inputReadOnly
            self.locale = locale
            self.maxDate = maxDate
            self.minDate = minDate
            self.mode = mode
            self.multiple = multiple
            self.needConfirm = needConfirm
            self.nextIcon = nextIcon
            self.onBlur = create_callback(onBlur, "onBlur", [[1, "range"]])
            self.onCalendarChange = create_callback(
                onCalendarChange, "onCalendarChange", [[], [2, "range"]]
            )
            self.onFocus = create_callback(onFocus, "onFocus", [[1, "range"]])
            self.onOk = create_callback(onOk, "onOk")
            self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
            self.onPanelChange = create_callback(
                onPanelChange, "onPanelChange", [[0], [1]]
            )
            self.open = open
            self.order = order
            self.panelRender = panelRender
            self.picker = picker
            self.pickerValue = pickerValue
            self.placeholder = placeholder
            self.placement = placement
            self.popupClassName = popupClassName
            self.popupStyle = popupStyle
            self.preserveInvalidOnBlur = preserveInvalidOnBlur
            self.presets = presets
            self.prevIcon = prevIcon
            self.renderExtraFooter = renderExtraFooter
            self.separator = separator
            self.showNow = showNow
            self.showTime = showTime
            self.showTime_defaultValue = showTime_defaultValue
            self.showWeek = showWeek
            self.size = size
            self.status = status
            self.suffixIcon = suffixIcon
            self.superNextIcon = superNextIcon
            self.superPrevIcon = superPrevIcon
            self.variant = variant
