from render import Component, create_callback, Props


class TagsInput(Component):
    Module = "mantine"
    JSXName = "TagsInput"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onChange",
        "onDropdownClose",
        "onDropdownOpen",
        "onDuplicate",
        "onOptionSubmit",
        "onSearchChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowDuplicates",
        "clearButtonProps",
        "clearable",
        "comboboxProps",
        "data",
        "defaultDropdownOpened",
        "defaultSearchValue",
        "defaultValue",
        "description",
        "descriptionProps",
        "disabled",
        "dropdownOpened",
        "error",
        "errorProps",
        "filter",
        "hiddenInputProps",
        "hiddenInputValuesDivider",
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
        "maxTags",
        "pointer",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "searchValue",
        "selectFirstOptionOnChange",
        "size",
        "splitChars",
        "value",
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
        allowDuplicates=None,
        clearButtonProps=None,
        clearable=None,
        comboboxProps=None,
        data=None,
        defaultDropdownOpened=None,
        defaultSearchValue=None,
        defaultValue=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        dropdownOpened=None,
        error=None,
        errorProps=None,
        filter=None,
        hiddenInputProps=None,
        hiddenInputValuesDivider=None,
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
        maxTags=None,
        onChange=None,
        onDropdownClose=None,
        onDropdownOpen=None,
        onDuplicate=None,
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
        selectFirstOptionOnChange=None,
        size=None,
        splitChars=None,
        value=None,
        withAsterisk=None,
        withErrorStyles=None,
        withScrollArea=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowDuplicates = allowDuplicates
        self.clearButtonProps = clearButtonProps
        self.clearable = clearable
        self.comboboxProps = comboboxProps
        self.data = data
        self.defaultDropdownOpened = defaultDropdownOpened
        self.defaultSearchValue = defaultSearchValue
        self.defaultValue = defaultValue
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.dropdownOpened = dropdownOpened
        self.error = error
        self.errorProps = errorProps
        self.filter = filter
        self.hiddenInputProps = hiddenInputProps
        self.hiddenInputValuesDivider = hiddenInputValuesDivider
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
        self.maxTags = maxTags
        self.onChange = create_callback(onChange, "onChange")
        self.onDropdownClose = create_callback(onDropdownClose, "onDropdownClose")
        self.onDropdownOpen = create_callback(onDropdownOpen, "onDropdownOpen")
        self.onDuplicate = create_callback(onDuplicate, "onDuplicate")
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
        self.selectFirstOptionOnChange = selectFirstOptionOnChange
        self.size = size
        self.splitChars = splitChars
        self.value = value
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.withScrollArea = withScrollArea
        self.wrapperProps = wrapperProps
