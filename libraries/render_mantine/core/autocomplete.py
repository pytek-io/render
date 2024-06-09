from render import Component, create_callback, InputComponent, Props


class Autocomplete(InputComponent):
    Module = "mantine/core"
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
        "component",
        "data",
        "defaultDropdownOpened",
        "description",
        "descriptionProps",
        "disabled",
        "dropdownOpened",
        "error",
        "errorProps",
        "filter",
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
        "selectFirstOptionOnChange",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
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
        component=None,
        data=None,
        defaultDropdownOpened=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        dropdownOpened=None,
        error=None,
        errorProps=None,
        filter=None,
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
        onDropdownClose=None,
        onDropdownOpen=None,
        onOptionSubmit=None,
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
        selectFirstOptionOnChange=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        withAsterisk=None,
        withErrorStyles=None,
        withScrollArea=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.comboboxProps = comboboxProps
        self.component = component
        self.data = data
        self.defaultDropdownOpened = defaultDropdownOpened
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.dropdownOpened = dropdownOpened
        self.error = error
        self.errorProps = errorProps
        self.filter = filter
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
        self.onDropdownClose = create_callback(onDropdownClose, "onDropdownClose")
        self.onDropdownOpen = create_callback(onDropdownOpen, "onDropdownOpen")
        self.onOptionSubmit = create_callback(onOptionSubmit, "onOptionSubmit")
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
        self.selectFirstOptionOnChange = selectFirstOptionOnChange
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withAsterisk = withAsterisk
        self.withErrorStyles = withErrorStyles
        self.withScrollArea = withScrollArea
        self.wrapperProps = wrapperProps
