from render import Component, create_callback, InputComponent, Props


class Autocomplete(InputComponent):
    Module = "mantine"
    JSXName = "Autocomplete"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onDropdownClose",
        "onDropdownOpen",
        "onOptionSubmit",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "comboboxProps",
        "data",
        "defaultDropdownOpened",
        "description",
        "descriptionProps",
        "disabled",
        "dropdownOpened",
        "error",
        "errorProps",
        "filter",
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "limit",
        "maxDropdownHeight",
        "pointer",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "selectFirstOptionOnChange",
        "size",
        "withAsterisk",
        "withErrorStyles",
        "withScrollArea",
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
        comboboxProps=None,
        data=None,
        defaultDropdownOpened=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        dropdownOpened=None,
        error=None,
        errorProps=None,
        filter=None,
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        limit=None,
        maxDropdownHeight=None,
        onDropdownClose=None,
        onDropdownOpen=None,
        onOptionSubmit=None,
        pointer=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        selectFirstOptionOnChange=None,
        size=None,
        withAsterisk=None,
        withErrorStyles=None,
        withScrollArea=None,
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
        self.comboboxProps = comboboxProps
        self.data = data
        self.defaultDropdownOpened = defaultDropdownOpened
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.dropdownOpened = dropdownOpened
        self.error = error
        self.errorProps = errorProps
        self.filter = filter
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.limit = limit
        self.maxDropdownHeight = maxDropdownHeight
        self.onDropdownClose = create_callback(onDropdownClose, "onDropdownClose")
        self.onDropdownOpen = create_callback(onDropdownOpen, "onDropdownOpen")
        self.onOptionSubmit = create_callback(onOptionSubmit, "onOptionSubmit")
        self.pointer = pointer
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.selectFirstOptionOnChange = selectFirstOptionOnChange
        self.size = size
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.withScrollArea = withScrollArea
        self.wrapperProps = wrapperProps
