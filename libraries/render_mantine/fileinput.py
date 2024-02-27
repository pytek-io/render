from render import Component, create_callback, InputComponent, Props


class FileInput(InputComponent):
    Module = "mantine"
    JSXName = "FileInput"
    InputName = "value"
    NewValuePath = "name"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "accept",
        "capture",
        "clearButtonProps",
        "clearable",
        "description",
        "descriptionProps",
        "disabled",
        "error",
        "errorProps",
        "fileInputProps",
        "form",
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "multiple",
        "name",
        "placeholder",
        "pointer",
        "radius",
        "readOnly",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "valueComponent",
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
        accept=None,
        capture=None,
        clearButtonProps=None,
        clearable=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        error=None,
        errorProps=None,
        fileInputProps=None,
        form=None,
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        multiple=None,
        name=None,
        placeholder=None,
        pointer=None,
        radius=None,
        readOnly=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        valueComponent=None,
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
        self.accept = accept
        self.capture = capture
        self.clearButtonProps = clearButtonProps
        self.clearable = clearable
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.fileInputProps = fileInputProps
        self.form = form
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.multiple = multiple
        self.name = name
        self.placeholder = placeholder
        self.pointer = pointer
        self.radius = radius
        self.readOnly = readOnly
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.valueComponent = valueComponent
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps
