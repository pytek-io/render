from render import Component, create_callback, InputComponent, Props


class JsonInput(InputComponent):
    Module = "mantine"
    JSXName = "JsonInput"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autosize",
        "description",
        "descriptionProps",
        "deserialize",
        "disabled",
        "error",
        "errorProps",
        "formatOnBlur",
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "maxRows",
        "minRows",
        "pointer",
        "radius",
        "required",
        "resize",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "serialize",
        "size",
        "validationError",
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
        description=None,
        descriptionProps=None,
        deserialize=None,
        disabled=None,
        error=None,
        errorProps=None,
        formatOnBlur=None,
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        maxRows=None,
        minRows=None,
        pointer=None,
        radius=None,
        required=None,
        resize=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        serialize=None,
        size=None,
        validationError=None,
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
        self.description = description
        self.descriptionProps = descriptionProps
        self.deserialize = deserialize
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.formatOnBlur = formatOnBlur
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.maxRows = maxRows
        self.minRows = minRows
        self.pointer = pointer
        self.radius = radius
        self.required = required
        self.resize = resize
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.serialize = serialize
        self.size = size
        self.validationError = validationError
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps
