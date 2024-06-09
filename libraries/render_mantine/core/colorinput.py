from render import Component, create_callback, InputComponent, Props


class ColorInput(InputComponent):
    Module = "mantine/core"
    JSXName = "ColorInput"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeOnColorSwatchClick",
        "component",
        "description",
        "descriptionProps",
        "disabled",
        "disallowInput",
        "error",
        "errorProps",
        "eyeDropperButtonProps",
        "eyeDropperIcon",
        "fixOnBlur",
        "format",
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
        "mb",
        "me",
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
        "popoverProps",
        "pr",
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
        "swatches",
        "swatchesPerRow",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "withAsterisk",
        "withErrorStyles",
        "withEyeDropper",
        "withPicker",
        "withPreview",
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
        defaultValue="",
        value=None,
        closeOnColorSwatchClick=None,
        component=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        disallowInput=None,
        error=None,
        errorProps=None,
        eyeDropperButtonProps=None,
        eyeDropperIcon=None,
        fixOnBlur=None,
        format=None,
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
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        onChangeEnd=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pointer=None,
        popoverProps=None,
        pr=None,
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
        swatches=None,
        swatchesPerRow=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        withAsterisk=None,
        withErrorStyles=None,
        withEyeDropper=None,
        withPicker=None,
        withPreview=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.closeOnColorSwatchClick = closeOnColorSwatchClick
        self.component = component
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.disallowInput = disallowInput
        self.error = error
        self.errorProps = errorProps
        self.eyeDropperButtonProps = eyeDropperButtonProps
        self.eyeDropperIcon = eyeDropperIcon
        self.fixOnBlur = fixOnBlur
        self.format = format
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
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pointer = pointer
        self.popoverProps = popoverProps
        self.pr = pr
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
        self.swatches = swatches
        self.swatchesPerRow = swatchesPerRow
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.withEyeDropper = withEyeDropper
        self.withPicker = withPicker
        self.withPreview = withPreview
        self.wrapperProps = wrapperProps
