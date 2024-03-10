from render import Component, create_callback, InputComponent, Props


class NumberInput(InputComponent):
    Module = "mantine/core"
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
        "component",
        "decimalScale",
        "decimalSeparator",
        "description",
        "descriptionProps",
        "disabled",
        "error",
        "errorProps",
        "fixedDecimalScale",
        "h",
        "handlersRef",
        "hideControls",
        "href",
        "inputContainer",
        "inputWrapperOrder",
        "isAllowed",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "m",
        "max",
        "mb",
        "me",
        "min",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pe",
        "pl",
        "pointer",
        "pr",
        "prefix",
        "ps",
        "pt",
        "px",
        "py",
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
        "sx",
        "ta",
        "target",
        "thousandSeparator",
        "thousandsGroupStyle",
        "title",
        "type",
        "valueIsNumericString",
        "variant",
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
        component=None,
        decimalScale=None,
        decimalSeparator=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        error=None,
        errorProps=None,
        fixedDecimalScale=None,
        h=None,
        handlersRef=None,
        hideControls=None,
        href=None,
        inputContainer=None,
        inputWrapperOrder=None,
        isAllowed=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        m=None,
        max=None,
        mb=None,
        me=None,
        min=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        onValueChange=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pointer=None,
        pr=None,
        prefix=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
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
        sx=None,
        ta=None,
        target=None,
        thousandSeparator=None,
        thousandsGroupStyle=None,
        title=None,
        type=None,
        valueIsNumericString=None,
        variant=None,
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
        self.component = component
        self.decimalScale = decimalScale
        self.decimalSeparator = decimalSeparator
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.fixedDecimalScale = fixedDecimalScale
        self.h = h
        self.handlersRef = handlersRef
        self.hideControls = hideControls
        self.href = href
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.isAllowed = isAllowed
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.m = m
        self.max = max
        self.mb = mb
        self.me = me
        self.min = min
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onValueChange = create_callback(onValueChange, "onValueChange")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pointer = pointer
        self.pr = pr
        self.prefix = prefix
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
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
        self.sx = sx
        self.ta = ta
        self.target = target
        self.thousandSeparator = thousandSeparator
        self.thousandsGroupStyle = thousandsGroupStyle
        self.title = title
        self.type = type
        self.valueIsNumericString = valueIsNumericString
        self.variant = variant
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps
