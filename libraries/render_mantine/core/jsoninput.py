from render import Component, create_callback, InputComponent, Props


class JsonInput(InputComponent):
    Module = "mantine/core"
    JSXName = "JsonInput"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autosize",
        "component",
        "description",
        "descriptionProps",
        "deserialize",
        "disabled",
        "error",
        "errorProps",
        "formatOnBlur",
        "h",
        "href",
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "m",
        "maxRows",
        "mb",
        "me",
        "minRows",
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
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "required",
        "resize",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "serialize",
        "size",
        "sx",
        "ta",
        "target",
        "validationError",
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
        autosize=None,
        component=None,
        description=None,
        descriptionProps=None,
        deserialize=None,
        disabled=None,
        error=None,
        errorProps=None,
        formatOnBlur=None,
        h=None,
        href=None,
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        m=None,
        maxRows=None,
        mb=None,
        me=None,
        minRows=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pointer=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        required=None,
        resize=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        serialize=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        validationError=None,
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
        self.autosize = autosize
        self.component = component
        self.description = description
        self.descriptionProps = descriptionProps
        self.deserialize = deserialize
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.formatOnBlur = formatOnBlur
        self.h = h
        self.href = href
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.m = m
        self.maxRows = maxRows
        self.mb = mb
        self.me = me
        self.minRows = minRows
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pointer = pointer
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.required = required
        self.resize = resize
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.serialize = serialize
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.validationError = validationError
        self.variant = variant
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps
