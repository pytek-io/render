from render import Component, create_callback, InputComponent, Props


class MultiSelect(InputComponent):
    Module = "mantine"
    JSXName = "MultiSelect"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onDropdownClose",
        "onDropdownOpen",
        "onOptionSubmit",
        "onSearchChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "checkIconPosition",
        "clearButtonProps",
        "clearable",
        "comboboxProps",
        "data",
        "defaultDropdownOpened",
        "defaultSearchValue",
        "description",
        "descriptionProps",
        "disabled",
        "dropdownOpened",
        "error",
        "errorProps",
        "filter",
        "hiddenInputProps",
        "hiddenInputValuesDivider",
        "hidePickedOptions",
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
        "maxValues",
        "nothingFoundMessage",
        "pointer",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "searchValue",
        "searchable",
        "selectFirstOptionOnChange",
        "size",
        "withAsterisk",
        "withCheckIcon",
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
        checkIconPosition=None,
        clearButtonProps=None,
        clearable=None,
        comboboxProps=None,
        data=None,
        defaultDropdownOpened=None,
        defaultSearchValue=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        dropdownOpened=None,
        error=None,
        errorProps=None,
        filter=None,
        hiddenInputProps=None,
        hiddenInputValuesDivider=None,
        hidePickedOptions=None,
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
        maxValues=None,
        nothingFoundMessage=None,
        onDropdownClose=None,
        onDropdownOpen=None,
        onOptionSubmit=None,
        onSearchChange=None,
        pointer=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        searchValue=None,
        searchable=None,
        selectFirstOptionOnChange=None,
        size=None,
        withAsterisk=None,
        withCheckIcon=None,
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
        self.checkIconPosition = checkIconPosition
        self.clearButtonProps = clearButtonProps
        self.clearable = clearable
        self.comboboxProps = comboboxProps
        self.data = data
        self.defaultDropdownOpened = defaultDropdownOpened
        self.defaultSearchValue = defaultSearchValue
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.dropdownOpened = dropdownOpened
        self.error = error
        self.errorProps = errorProps
        self.filter = filter
        self.hiddenInputProps = hiddenInputProps
        self.hiddenInputValuesDivider = hiddenInputValuesDivider
        self.hidePickedOptions = hidePickedOptions
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
        self.maxValues = maxValues
        self.nothingFoundMessage = nothingFoundMessage
        self.onDropdownClose = create_callback(onDropdownClose, "onDropdownClose")
        self.onDropdownOpen = create_callback(onDropdownOpen, "onDropdownOpen")
        self.onOptionSubmit = create_callback(onOptionSubmit, "onOptionSubmit")
        self.onSearchChange = create_callback(onSearchChange, "onSearchChange")
        self.pointer = pointer
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.searchValue = searchValue
        self.searchable = searchable
        self.selectFirstOptionOnChange = selectFirstOptionOnChange
        self.size = size
        self.withAsterisk = withAsterisk
        self.withCheckIcon = withCheckIcon
        self.withErrorStyles = withErrorStyles
        self.withScrollArea = withScrollArea
        self.wrapperProps = wrapperProps
