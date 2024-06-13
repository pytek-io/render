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
        "cellRender",
        "changeOnScroll",
        "disabled",
        "disabledTime",
        "format",
        "getPopupContainer",
        "hideDisabledOptions",
        "hourStep",
        "inputReadOnly",
        "minuteStep",
        "needConfirm",
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
        cellRender=None,
        changeOnScroll=None,
        disabled=None,
        disabledTime=None,
        format=None,
        getPopupContainer=None,
        hideDisabledOptions=None,
        hourStep=None,
        inputReadOnly=None,
        minuteStep=None,
        needConfirm=None,
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
        self.cellRender = cellRender
        self.changeOnScroll = changeOnScroll
        self.disabled = disabled
        self.disabledTime = disabledTime
        self.format = format
        self.getPopupContainer = getPopupContainer
        self.hideDisabledOptions = hideDisabledOptions
        self.hourStep = hourStep
        self.inputReadOnly = inputReadOnly
        self.minuteStep = minuteStep
        self.needConfirm = needConfirm
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
        self.variant = variant

    class RangePicker(InputComponent):
        Module = "antd"
        JSXName = "TimePicker.RangePicker"
        InputName = "value"
        CALLBACKS = ["onKeyPress", "onClick", "onOpenChange", "onSelect"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "allowClear",
            "autoFocus",
            "cellRender",
            "changeOnScroll",
            "disabled",
            "disabledTime",
            "format",
            "getPopupContainer",
            "hideDisabledOptions",
            "hourStep",
            "inputReadOnly",
            "minuteStep",
            "needConfirm",
            "open",
            "order",
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
            cellRender=None,
            changeOnScroll=None,
            disabled=None,
            disabledTime=None,
            format=None,
            getPopupContainer=None,
            hideDisabledOptions=None,
            hourStep=None,
            inputReadOnly=None,
            minuteStep=None,
            needConfirm=None,
            onOpenChange=None,
            onSelect=None,
            open=None,
            order=None,
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
            self.cellRender = cellRender
            self.changeOnScroll = changeOnScroll
            self.disabled = disabled
            self.disabledTime = disabledTime
            self.format = format
            self.getPopupContainer = getPopupContainer
            self.hideDisabledOptions = hideDisabledOptions
            self.hourStep = hourStep
            self.inputReadOnly = inputReadOnly
            self.minuteStep = minuteStep
            self.needConfirm = needConfirm
            self.onOpenChange = create_callback(onOpenChange, "onOpenChange", [[0]])
            self.onSelect = create_callback(onSelect, "onSelect", [[0]])
            self.open = open
            self.order = order
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
            self.variant = variant
