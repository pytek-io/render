from render import Component, create_callback, InputComponent, Props


class ColorInput(InputComponent):
    Module = "mantine"
    JSXName = "ColorInput"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "closeOnColorSwatchClick",
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
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "pointer",
        "popoverProps",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "swatches",
        "swatchesPerRow",
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
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        onChangeEnd=None,
        pointer=None,
        popoverProps=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        swatches=None,
        swatchesPerRow=None,
        withAsterisk=None,
        withErrorStyles=None,
        withEyeDropper=None,
        withPicker=None,
        withPreview=None,
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
        self.closeOnColorSwatchClick = closeOnColorSwatchClick
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
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.pointer = pointer
        self.popoverProps = popoverProps
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.swatches = swatches
        self.swatchesPerRow = swatchesPerRow
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.withEyeDropper = withEyeDropper
        self.withPicker = withPicker
        self.withPreview = withPreview
        self.wrapperProps = wrapperProps
