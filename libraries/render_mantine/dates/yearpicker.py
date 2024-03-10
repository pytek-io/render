from render import Component, create_callback, Props


class YearPicker(Component):
    Module = "mantine/dates"
    JSXName = "YearPicker"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onChange",
        "onDateChange",
        "onNextDecade",
        "onPreviousDecade",
        "onYearSelect",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowDeselect",
        "allowSingleDateInRange",
        "ariaLabels",
        "columnsToScroll",
        "component",
        "date",
        "decadeLabelFormat",
        "defaultDate",
        "defaultValue",
        "getYearControlProps",
        "h",
        "href",
        "locale",
        "m",
        "maxDate",
        "mb",
        "me",
        "minDate",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "numberOfColumns",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "type",
        "value",
        "variant",
        "withCellSpacing",
        "yearsListFormat",
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
        allowDeselect=None,
        allowSingleDateInRange=None,
        ariaLabels=None,
        columnsToScroll=None,
        component=None,
        date=None,
        decadeLabelFormat=None,
        defaultDate=None,
        defaultValue=None,
        getYearControlProps=None,
        h=None,
        href=None,
        locale=None,
        m=None,
        maxDate=None,
        mb=None,
        me=None,
        minDate=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        numberOfColumns=None,
        onChange=None,
        onDateChange=None,
        onNextDecade=None,
        onPreviousDecade=None,
        onYearSelect=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        type=None,
        value=None,
        variant=None,
        withCellSpacing=None,
        yearsListFormat=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowDeselect = allowDeselect
        self.allowSingleDateInRange = allowSingleDateInRange
        self.ariaLabels = ariaLabels
        self.columnsToScroll = columnsToScroll
        self.component = component
        self.date = date
        self.decadeLabelFormat = decadeLabelFormat
        self.defaultDate = defaultDate
        self.defaultValue = defaultValue
        self.getYearControlProps = getYearControlProps
        self.h = h
        self.href = href
        self.locale = locale
        self.m = m
        self.maxDate = maxDate
        self.mb = mb
        self.me = me
        self.minDate = minDate
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.numberOfColumns = numberOfColumns
        self.onChange = create_callback(onChange, "onChange")
        self.onDateChange = create_callback(onDateChange, "onDateChange")
        self.onNextDecade = create_callback(onNextDecade, "onNextDecade")
        self.onPreviousDecade = create_callback(onPreviousDecade, "onPreviousDecade")
        self.onYearSelect = create_callback(onYearSelect, "onYearSelect")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.type = type
        self.value = value
        self.variant = variant
        self.withCellSpacing = withCellSpacing
        self.yearsListFormat = yearsListFormat

    class Input(Component):
        Module = "mantine/dates"
        JSXName = "YearPicker.Input"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onChange",
            "onDateChange",
            "onNextDecade",
            "onPreviousDecade",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "allowDeselect",
            "allowSingleDateInRange",
            "ariaLabels",
            "clearButtonProps",
            "clearable",
            "closeOnChange",
            "columnsToScroll",
            "component",
            "date",
            "decadeLabelFormat",
            "defaultDate",
            "defaultValue",
            "description",
            "descriptionProps",
            "disabled",
            "dropdownType",
            "error",
            "errorProps",
            "getYearControlProps",
            "h",
            "href",
            "inputContainer",
            "inputWrapperOrder",
            "label",
            "labelProps",
            "labelSeparator",
            "leftSection",
            "leftSectionPointerEvents",
            "leftSectionProps",
            "leftSectionWidth",
            "locale",
            "m",
            "maxDate",
            "mb",
            "me",
            "minDate",
            "ml",
            "modalProps",
            "mr",
            "ms",
            "mt",
            "mx",
            "my",
            "numberOfColumns",
            "p",
            "pb",
            "pe",
            "pl",
            "placeholder",
            "pointer",
            "popoverProps",
            "pr",
            "ps",
            "pt",
            "px",
            "py",
            "radius",
            "readOnly",
            "required",
            "rightSection",
            "rightSectionPointerEvents",
            "rightSectionProps",
            "rightSectionWidth",
            "size",
            "sortDates",
            "sx",
            "ta",
            "target",
            "title",
            "type",
            "value",
            "valueFormat",
            "valueFormatter",
            "variant",
            "withAsterisk",
            "withCellSpacing",
            "withErrorStyles",
            "wrapperProps",
            "yearsListFormat",
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
            allowDeselect=None,
            allowSingleDateInRange=None,
            ariaLabels=None,
            clearButtonProps=None,
            clearable=None,
            closeOnChange=None,
            columnsToScroll=None,
            component=None,
            date=None,
            decadeLabelFormat=None,
            defaultDate=None,
            defaultValue=None,
            description=None,
            descriptionProps=None,
            disabled=None,
            dropdownType=None,
            error=None,
            errorProps=None,
            getYearControlProps=None,
            h=None,
            href=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelProps=None,
            labelSeparator=None,
            leftSection=None,
            leftSectionPointerEvents=None,
            leftSectionProps=None,
            leftSectionWidth=None,
            locale=None,
            m=None,
            maxDate=None,
            mb=None,
            me=None,
            minDate=None,
            ml=None,
            modalProps=None,
            mr=None,
            ms=None,
            mt=None,
            mx=None,
            my=None,
            numberOfColumns=None,
            onChange=None,
            onDateChange=None,
            onNextDecade=None,
            onPreviousDecade=None,
            p=None,
            pb=None,
            pe=None,
            pl=None,
            placeholder=None,
            pointer=None,
            popoverProps=None,
            pr=None,
            ps=None,
            pt=None,
            px=None,
            py=None,
            radius=None,
            readOnly=None,
            required=None,
            rightSection=None,
            rightSectionPointerEvents=None,
            rightSectionProps=None,
            rightSectionWidth=None,
            size=None,
            sortDates=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            type=None,
            value=None,
            valueFormat=None,
            valueFormatter=None,
            variant=None,
            withAsterisk=None,
            withCellSpacing=None,
            withErrorStyles=None,
            wrapperProps=None,
            yearsListFormat=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.allowDeselect = allowDeselect
            self.allowSingleDateInRange = allowSingleDateInRange
            self.ariaLabels = ariaLabels
            self.clearButtonProps = clearButtonProps
            self.clearable = clearable
            self.closeOnChange = closeOnChange
            self.columnsToScroll = columnsToScroll
            self.component = component
            self.date = date
            self.decadeLabelFormat = decadeLabelFormat
            self.defaultDate = defaultDate
            self.defaultValue = defaultValue
            self.description = description
            self.descriptionProps = descriptionProps
            self.disabled = disabled
            self.dropdownType = dropdownType
            self.error = error
            self.errorProps = errorProps
            self.getYearControlProps = getYearControlProps
            self.h = h
            self.href = href
            self.inputContainer = inputContainer
            self.inputWrapperOrder = inputWrapperOrder
            self.label = label
            self.labelProps = labelProps
            self.labelSeparator = labelSeparator
            self.leftSection = leftSection
            self.leftSectionPointerEvents = leftSectionPointerEvents
            self.leftSectionProps = leftSectionProps
            self.leftSectionWidth = leftSectionWidth
            self.locale = locale
            self.m = m
            self.maxDate = maxDate
            self.mb = mb
            self.me = me
            self.minDate = minDate
            self.ml = ml
            self.modalProps = modalProps
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.mx = mx
            self.my = my
            self.numberOfColumns = numberOfColumns
            self.onChange = create_callback(onChange, "onChange")
            self.onDateChange = create_callback(onDateChange, "onDateChange")
            self.onNextDecade = create_callback(onNextDecade, "onNextDecade")
            self.onPreviousDecade = create_callback(
                onPreviousDecade, "onPreviousDecade"
            )
            self.p = p
            self.pb = pb
            self.pe = pe
            self.pl = pl
            self.placeholder = placeholder
            self.pointer = pointer
            self.popoverProps = popoverProps
            self.pr = pr
            self.ps = ps
            self.pt = pt
            self.px = px
            self.py = py
            self.radius = radius
            self.readOnly = readOnly
            self.required = required
            self.rightSection = rightSection
            self.rightSectionPointerEvents = rightSectionPointerEvents
            self.rightSectionProps = rightSectionProps
            self.rightSectionWidth = rightSectionWidth
            self.size = size
            self.sortDates = sortDates
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.type = type
            self.value = value
            self.valueFormat = valueFormat
            self.valueFormatter = valueFormatter
            self.variant = variant
            self.withAsterisk = withAsterisk
            self.withCellSpacing = withCellSpacing
            self.withErrorStyles = withErrorStyles
            self.wrapperProps = wrapperProps
            self.yearsListFormat = yearsListFormat
