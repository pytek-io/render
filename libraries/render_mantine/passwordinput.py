from render import Component, create_callback, InputComponent, Props


class PasswordInput(InputComponent):
    Module = "mantine"
    JSXName = "PasswordInput"
    InputName = "value"
    NewValuePath = "currentTarget.value"
    CALLBACKS = ["onKeyPress", "onClick", "onVisibilityChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "defaultVisible",
        "description",
        "descriptionProps",
        "disabled",
        "error",
        "errorProps",
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "pointer",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "visibilityToggleButtonProps",
        "visibilityToggleIcon",
        "visible",
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
        defaultVisible=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        error=None,
        errorProps=None,
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        onVisibilityChange=None,
        pointer=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        visibilityToggleButtonProps=None,
        visibilityToggleIcon=None,
        visible=None,
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
        self.defaultVisible = defaultVisible
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.onVisibilityChange = create_callback(
            onVisibilityChange, "onVisibilityChange"
        )
        self.pointer = pointer
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.visibilityToggleButtonProps = visibilityToggleButtonProps
        self.visibilityToggleIcon = visibilityToggleIcon
        self.visible = visible
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps
