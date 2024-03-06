from render import Component, create_callback, Props


class DateTimePicker(Component):
    Module = "mantine/dates"
    JSXName = "DateTimePicker"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onChange",
        "onDateChange",
        "onLevelChange",
        "onMonthSelect",
        "onNextDecade",
        "onNextMonth",
        "onNextYear",
        "onPreviousDecade",
        "onPreviousMonth",
        "onPreviousYear",
        "onYearSelect",
        "timeInputProps",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "ariaLabels",
        "clearButtonProps",
        "clearable",
        "columnsToScroll",
        "component",
        "date",
        "decadeLabelFormat",
        "defaultLevel",
        "defaultValue",
        "description",
        "descriptionProps",
        "disabled",
        "dropdownType",
        "error",
        "errorProps",
        "excludeDate",
        "firstDayOfWeek",
        "getDayAriaLabel",
        "getDayProps",
        "getMonthControlProps",
        "getYearControlProps",
        "h",
        "hasNextLevel",
        "hideOutsideDates",
        "hideWeekdays",
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
        "level",
        "locale",
        "m",
        "maxDate",
        "mb",
        "me",
        "minDate",
        "ml",
        "modalProps",
        "monthLabelFormat",
        "monthsListFormat",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "nextIcon",
        "nextLabel",
        "numberOfColumns",
        "p",
        "pb",
        "pe",
        "pl",
        "placeholder",
        "pointer",
        "popoverProps",
        "pr",
        "previousIcon",
        "previousLabel",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "readOnly",
        "renderDay",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "sortDates",
        "submitButtonProps",
        "sx",
        "ta",
        "target",
        "value",
        "valueFormat",
        "valueFormatter",
        "variant",
        "weekdayFormat",
        "weekendDays",
        "withAsterisk",
        "withCellSpacing",
        "withErrorStyles",
        "withSeconds",
        "wrapperProps",
        "yearLabelFormat",
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
        ariaLabels=None,
        clearButtonProps=None,
        clearable=None,
        columnsToScroll=None,
        component=None,
        date=None,
        decadeLabelFormat=None,
        defaultLevel=None,
        defaultValue=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        dropdownType=None,
        error=None,
        errorProps=None,
        excludeDate=None,
        firstDayOfWeek=None,
        getDayAriaLabel=None,
        getDayProps=None,
        getMonthControlProps=None,
        getYearControlProps=None,
        h=None,
        hasNextLevel=None,
        hideOutsideDates=None,
        hideWeekdays=None,
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
        level=None,
        locale=None,
        m=None,
        maxDate=None,
        mb=None,
        me=None,
        minDate=None,
        ml=None,
        modalProps=None,
        monthLabelFormat=None,
        monthsListFormat=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        nextIcon=None,
        nextLabel=None,
        numberOfColumns=None,
        onChange=None,
        onDateChange=None,
        onLevelChange=None,
        onMonthSelect=None,
        onNextDecade=None,
        onNextMonth=None,
        onNextYear=None,
        onPreviousDecade=None,
        onPreviousMonth=None,
        onPreviousYear=None,
        onYearSelect=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        placeholder=None,
        pointer=None,
        popoverProps=None,
        pr=None,
        previousIcon=None,
        previousLabel=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        readOnly=None,
        renderDay=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        sortDates=None,
        submitButtonProps=None,
        sx=None,
        ta=None,
        target=None,
        timeInputProps=None,
        value=None,
        valueFormat=None,
        valueFormatter=None,
        variant=None,
        weekdayFormat=None,
        weekendDays=None,
        withAsterisk=None,
        withCellSpacing=None,
        withErrorStyles=None,
        withSeconds=None,
        wrapperProps=None,
        yearLabelFormat=None,
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
        self.ariaLabels = ariaLabels
        self.clearButtonProps = clearButtonProps
        self.clearable = clearable
        self.columnsToScroll = columnsToScroll
        self.component = component
        self.date = date
        self.decadeLabelFormat = decadeLabelFormat
        self.defaultLevel = defaultLevel
        self.defaultValue = defaultValue
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.dropdownType = dropdownType
        self.error = error
        self.errorProps = errorProps
        self.excludeDate = excludeDate
        self.firstDayOfWeek = firstDayOfWeek
        self.getDayAriaLabel = getDayAriaLabel
        self.getDayProps = getDayProps
        self.getMonthControlProps = getMonthControlProps
        self.getYearControlProps = getYearControlProps
        self.h = h
        self.hasNextLevel = hasNextLevel
        self.hideOutsideDates = hideOutsideDates
        self.hideWeekdays = hideWeekdays
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
        self.level = level
        self.locale = locale
        self.m = m
        self.maxDate = maxDate
        self.mb = mb
        self.me = me
        self.minDate = minDate
        self.ml = ml
        self.modalProps = modalProps
        self.monthLabelFormat = monthLabelFormat
        self.monthsListFormat = monthsListFormat
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nextIcon = nextIcon
        self.nextLabel = nextLabel
        self.numberOfColumns = numberOfColumns
        self.onChange = create_callback(onChange, "onChange")
        self.onDateChange = create_callback(onDateChange, "onDateChange")
        self.onLevelChange = create_callback(onLevelChange, "onLevelChange")
        self.onMonthSelect = create_callback(onMonthSelect, "onMonthSelect")
        self.onNextDecade = create_callback(onNextDecade, "onNextDecade")
        self.onNextMonth = create_callback(onNextMonth, "onNextMonth")
        self.onNextYear = create_callback(onNextYear, "onNextYear")
        self.onPreviousDecade = create_callback(onPreviousDecade, "onPreviousDecade")
        self.onPreviousMonth = create_callback(onPreviousMonth, "onPreviousMonth")
        self.onPreviousYear = create_callback(onPreviousYear, "onPreviousYear")
        self.onYearSelect = create_callback(onYearSelect, "onYearSelect")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.placeholder = placeholder
        self.pointer = pointer
        self.popoverProps = popoverProps
        self.pr = pr
        self.previousIcon = previousIcon
        self.previousLabel = previousLabel
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.readOnly = readOnly
        self.renderDay = renderDay
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.sortDates = sortDates
        self.submitButtonProps = submitButtonProps
        self.sx = sx
        self.ta = ta
        self.target = target
        self.timeInputProps = create_callback(timeInputProps, "timeInputProps")
        self.value = value
        self.valueFormat = valueFormat
        self.valueFormatter = valueFormatter
        self.variant = variant
        self.weekdayFormat = weekdayFormat
        self.weekendDays = weekendDays
        self.withAsterisk = withAsterisk
        self.withCellSpacing = withCellSpacing
        self.withErrorStyles = withErrorStyles
        self.withSeconds = withSeconds
        self.wrapperProps = wrapperProps
        self.yearLabelFormat = yearLabelFormat
        self.yearsListFormat = yearsListFormat
