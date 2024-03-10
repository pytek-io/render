from render import Component, create_callback, InputComponent, Props


class Select(InputComponent):
    Module = "mantine/core"
    JSXName = "Select"
    InputName = "value"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onClear",
        "onDropdownClose",
        "onDropdownOpen",
        "onOptionSubmit",
        "onSearchChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowDeselect",
        "checkIconPosition",
        "clearButtonProps",
        "clearable",
        "comboboxProps",
        "component",
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
        "h",
        "hiddenInputProps",
        "href",
        "inputContainer",
        "inputWrapperOrder",
        "label",
        "labelProps",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "limit",
        "m",
        "maxDropdownHeight",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "nothingFoundMessage",
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
        "renderOption",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "searchValue",
        "searchable",
        "selectFirstOptionOnChange",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
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
        allowDeselect=None,
        checkIconPosition=None,
        clearButtonProps=None,
        clearable=None,
        comboboxProps=None,
        component=None,
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
        h=None,
        hiddenInputProps=None,
        href=None,
        inputContainer=None,
        inputWrapperOrder=None,
        label=None,
        labelProps=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        limit=None,
        m=None,
        maxDropdownHeight=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        nothingFoundMessage=None,
        onClear=None,
        onDropdownClose=None,
        onDropdownOpen=None,
        onOptionSubmit=None,
        onSearchChange=None,
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
        renderOption=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        searchValue=None,
        searchable=None,
        selectFirstOptionOnChange=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
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
        self.allowDeselect = allowDeselect
        self.checkIconPosition = checkIconPosition
        self.clearButtonProps = clearButtonProps
        self.clearable = clearable
        self.comboboxProps = comboboxProps
        self.component = component
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
        self.h = h
        self.hiddenInputProps = hiddenInputProps
        self.href = href
        self.inputContainer = inputContainer
        self.inputWrapperOrder = inputWrapperOrder
        self.label = label
        self.labelProps = labelProps
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.limit = limit
        self.m = m
        self.maxDropdownHeight = maxDropdownHeight
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nothingFoundMessage = nothingFoundMessage
        self.onClear = create_callback(onClear, "onClear")
        self.onDropdownClose = create_callback(onDropdownClose, "onDropdownClose")
        self.onDropdownOpen = create_callback(onDropdownOpen, "onDropdownOpen")
        self.onOptionSubmit = create_callback(onOptionSubmit, "onOptionSubmit")
        self.onSearchChange = create_callback(onSearchChange, "onSearchChange")
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
        self.renderOption = renderOption
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.searchValue = searchValue
        self.searchable = searchable
        self.selectFirstOptionOnChange = selectFirstOptionOnChange
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withAsterisk = withAsterisk
        self.withCheckIcon = withCheckIcon
        self.withErrorStyles = withErrorStyles
        self.withScrollArea = withScrollArea
        self.wrapperProps = wrapperProps
