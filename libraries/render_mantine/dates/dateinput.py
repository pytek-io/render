from render import Component, create_callback, Props


class DateInput(Component):
    Module = "mantine/dates"
    JSXName = "DateInput"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onChange",
        "onDateChange",
        "onLevelChange",
        "onLevelClick",
        "onNext",
        "onNextDecade",
        "onNextMonth",
        "onNextYear",
        "onPrevious",
        "onPreviousDecade",
        "onPreviousMonth",
        "onPreviousYear",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowDeselect",
        "ariaLabels",
        "clearButtonProps",
        "clearable",
        "columnsToScroll",
        "component",
        "date",
        "dateParser",
        "decadeLabelFormat",
        "defaultDate",
        "defaultLevel",
        "defaultValue",
        "description",
        "descriptionProps",
        "disabled",
        "error",
        "errorProps",
        "excludeDate",
        "firstDayOfWeek",
        "fixOnBlur",
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
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "level",
        "locale",
        "m",
        "maxDate",
        "maxLevel",
        "mb",
        "me",
        "minDate",
        "ml",
        "monthLabelFormat",
        "monthsListFormat",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "nextDisabled",
        "nextIcon",
        "nextLabel",
        "numberOfColumns",
        "p",
        "pb",
        "pe",
        "pl",
        "pointer",
        "popoverProps",
        "pr",
        "preserveTime",
        "previousDisabled",
        "previousIcon",
        "previousLabel",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "renderDay",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "value",
        "valueFormat",
        "variant",
        "weekdayFormat",
        "weekendDays",
        "withAsterisk",
        "withCellSpacing",
        "withErrorStyles",
        "withNext",
        "withPrevious",
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
        allowDeselect=None,
        ariaLabels=None,
        clearButtonProps=None,
        clearable=None,
        columnsToScroll=None,
        component=None,
        date=None,
        dateParser=None,
        decadeLabelFormat=None,
        defaultDate=None,
        defaultLevel=None,
        defaultValue=None,
        description=None,
        descriptionProps=None,
        disabled=None,
        error=None,
        errorProps=None,
        excludeDate=None,
        firstDayOfWeek=None,
        fixOnBlur=None,
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
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        level=None,
        locale=None,
        m=None,
        maxDate=None,
        maxLevel=None,
        mb=None,
        me=None,
        minDate=None,
        ml=None,
        monthLabelFormat=None,
        monthsListFormat=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        nextDisabled=None,
        nextIcon=None,
        nextLabel=None,
        numberOfColumns=None,
        onChange=None,
        onDateChange=None,
        onLevelChange=None,
        onLevelClick=None,
        onNext=None,
        onNextDecade=None,
        onNextMonth=None,
        onNextYear=None,
        onPrevious=None,
        onPreviousDecade=None,
        onPreviousMonth=None,
        onPreviousYear=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pointer=None,
        popoverProps=None,
        pr=None,
        preserveTime=None,
        previousDisabled=None,
        previousIcon=None,
        previousLabel=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        renderDay=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        value=None,
        valueFormat=None,
        variant=None,
        weekdayFormat=None,
        weekendDays=None,
        withAsterisk=None,
        withCellSpacing=None,
        withErrorStyles=None,
        withNext=None,
        withPrevious=None,
        wrapperProps=None,
        yearLabelFormat=None,
        yearsListFormat=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowDeselect = allowDeselect
        self.ariaLabels = ariaLabels
        self.clearButtonProps = clearButtonProps
        self.clearable = clearable
        self.columnsToScroll = columnsToScroll
        self.component = component
        self.date = date
        self.dateParser = dateParser
        self.decadeLabelFormat = decadeLabelFormat
        self.defaultDate = defaultDate
        self.defaultLevel = defaultLevel
        self.defaultValue = defaultValue
        self.description = description
        self.descriptionProps = descriptionProps
        self.disabled = disabled
        self.error = error
        self.errorProps = errorProps
        self.excludeDate = excludeDate
        self.firstDayOfWeek = firstDayOfWeek
        self.fixOnBlur = fixOnBlur
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
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.level = level
        self.locale = locale
        self.m = m
        self.maxDate = maxDate
        self.maxLevel = maxLevel
        self.mb = mb
        self.me = me
        self.minDate = minDate
        self.ml = ml
        self.monthLabelFormat = monthLabelFormat
        self.monthsListFormat = monthsListFormat
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nextDisabled = nextDisabled
        self.nextIcon = nextIcon
        self.nextLabel = nextLabel
        self.numberOfColumns = numberOfColumns
        self.onChange = create_callback(onChange, "onChange")
        self.onDateChange = create_callback(onDateChange, "onDateChange")
        self.onLevelChange = create_callback(onLevelChange, "onLevelChange")
        self.onLevelClick = create_callback(onLevelClick, "onLevelClick")
        self.onNext = create_callback(onNext, "onNext")
        self.onNextDecade = create_callback(onNextDecade, "onNextDecade")
        self.onNextMonth = create_callback(onNextMonth, "onNextMonth")
        self.onNextYear = create_callback(onNextYear, "onNextYear")
        self.onPrevious = create_callback(onPrevious, "onPrevious")
        self.onPreviousDecade = create_callback(onPreviousDecade, "onPreviousDecade")
        self.onPreviousMonth = create_callback(onPreviousMonth, "onPreviousMonth")
        self.onPreviousYear = create_callback(onPreviousYear, "onPreviousYear")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pointer = pointer
        self.popoverProps = popoverProps
        self.pr = pr
        self.preserveTime = preserveTime
        self.previousDisabled = previousDisabled
        self.previousIcon = previousIcon
        self.previousLabel = previousLabel
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.renderDay = renderDay
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.value = value
        self.valueFormat = valueFormat
        self.variant = variant
        self.weekdayFormat = weekdayFormat
        self.weekendDays = weekendDays
        self.withAsterisk = withAsterisk
        self.withCellSpacing = withCellSpacing
        self.withErrorStyles = withErrorStyles
        self.withNext = withNext
        self.withPrevious = withPrevious
        self.wrapperProps = wrapperProps
        self.yearLabelFormat = yearLabelFormat
        self.yearsListFormat = yearsListFormat
