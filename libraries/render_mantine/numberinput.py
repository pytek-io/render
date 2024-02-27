from render import Component, create_callback, InputComponent, Props


class NumberInput(InputComponent):
    Module = "mantine"
    JSXName = "NumberInput"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onValueChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowDecimal",
        "allowLeadingZeros",
        "allowNegative",
        "allowedDecimalSeparators",
        "clampBehavior",
        "decimalScale",
        "decimalSeparator",
        "description",
        "descriptionProps",
        "disabled",
        "error",
        "errorProps",
        "fixedDecimalScale",
        "handlersRef",
        "hideControls",
        "inputContainer",
        "inputWrapperOrder",
        "isAllowed",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "max",
        "min",
        "pointer",
        "prefix",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "startValue",
        "step",
        "stepHoldDelay",
        "stepHoldInterval",
        "suffix",
        "thousandSeparator",
        "thousandsGroupStyle",
        "type",
        "valueIsNumericString",
        "withAsterisk",
        "withErrorStyles",
        "wrapperProps",
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
        allowDecimal=None,
        allowLeadingZeros=None,
        allowNegative=None,
        allowedDecimalSeparators=None,
        clampBehavior=None,
        decimalScale=None,
        decimalSeparator=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        error=None,
        errorProps=None,
        fixedDecimalScale=None,
        handlersRef=None,
        hideControls=None,
        inputContainer=None,
        inputWrapperOrder=None,
        isAllowed=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        max=None,
        min=None,
        onValueChange=None,
        pointer=None,
        prefix=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        startValue=None,
        step=None,
        stepHoldDelay=None,
        stepHoldInterval=None,
        suffix=None,
        thousandSeparator=None,
        thousandsGroupStyle=None,
        type=None,
        valueIsNumericString=None,
        withAsterisk=None,
        withErrorStyles=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowDecimal = allowDecimal
        self.allowLeadingZeros = allowLeadingZeros
        self.allowNegative = allowNegative
        self.allowedDecimalSeparators = allowedDecimalSeparators
        self.clampBehavior = clampBehavior
        self.decimalScale = decimalScale
        self.decimalSeparator = decimalSeparator
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.fixedDecimalScale = fixedDecimalScale
        self.handlersRef = handlersRef
        self.hideControls = hideControls
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.isAllowed = isAllowed
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.max = max
        self.min = min
        self.onValueChange = create_callback(onValueChange, "onValueChange")
        self.pointer = pointer
        self.prefix = prefix
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.startValue = startValue
        self.step = step
        self.stepHoldDelay = stepHoldDelay
        self.stepHoldInterval = stepHoldInterval
        self.suffix = suffix
        self.thousandSeparator = thousandSeparator
        self.thousandsGroupStyle = thousandsGroupStyle
        self.type = type
        self.valueIsNumericString = valueIsNumericString
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps
