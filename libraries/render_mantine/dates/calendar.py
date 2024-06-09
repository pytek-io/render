from render import Component, create_callback, Props


class Calendar(Component):
    Module = "mantine/dates"
    JSXName = "Calendar"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onDateChange",
        "onLevelChange",
        "onMonthMouseEnter",
        "onMonthSelect",
        "onNextDecade",
        "onNextMonth",
        "onNextYear",
        "onPreviousDecade",
        "onPreviousMonth",
        "onPreviousYear",
        "onYearMouseEnter",
        "onYearSelect",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "ariaLabels",
        "columnsToScroll",
        "component",
        "date",
        "decadeLabelFormat",
        "defaultDate",
        "defaultLevel",
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
        "level",
        "locale",
        "m",
        "maxDate",
        "maxLevel",
        "mb",
        "me",
        "minDate",
        "minLevel",
        "ml",
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
        "pr",
        "previousIcon",
        "previousLabel",
        "ps",
        "pt",
        "px",
        "py",
        "renderDay",
        "size",
        "static",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "weekdayFormat",
        "weekendDays",
        "withCellSpacing",
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
        columnsToScroll=None,
        component=None,
        date=None,
        decadeLabelFormat=None,
        defaultDate=None,
        defaultLevel=None,
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
        level=None,
        locale=None,
        m=None,
        maxDate=None,
        maxLevel=None,
        mb=None,
        me=None,
        minDate=None,
        minLevel=None,
        ml=None,
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
        onDateChange=None,
        onLevelChange=None,
        onMonthMouseEnter=None,
        onMonthSelect=None,
        onNextDecade=None,
        onNextMonth=None,
        onNextYear=None,
        onPreviousDecade=None,
        onPreviousMonth=None,
        onPreviousYear=None,
        onYearMouseEnter=None,
        onYearSelect=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        previousIcon=None,
        previousLabel=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        renderDay=None,
        size=None,
        static=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        weekdayFormat=None,
        weekendDays=None,
        withCellSpacing=None,
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
        self.ariaLabels = ariaLabels
        self.columnsToScroll = columnsToScroll
        self.component = component
        self.date = date
        self.decadeLabelFormat = decadeLabelFormat
        self.defaultDate = defaultDate
        self.defaultLevel = defaultLevel
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
        self.level = level
        self.locale = locale
        self.m = m
        self.maxDate = maxDate
        self.maxLevel = maxLevel
        self.mb = mb
        self.me = me
        self.minDate = minDate
        self.minLevel = minLevel
        self.ml = ml
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
        self.onDateChange = create_callback(onDateChange, "onDateChange")
        self.onLevelChange = create_callback(onLevelChange, "onLevelChange")
        self.onMonthMouseEnter = create_callback(onMonthMouseEnter, "onMonthMouseEnter")
        self.onMonthSelect = create_callback(onMonthSelect, "onMonthSelect")
        self.onNextDecade = create_callback(onNextDecade, "onNextDecade")
        self.onNextMonth = create_callback(onNextMonth, "onNextMonth")
        self.onNextYear = create_callback(onNextYear, "onNextYear")
        self.onPreviousDecade = create_callback(onPreviousDecade, "onPreviousDecade")
        self.onPreviousMonth = create_callback(onPreviousMonth, "onPreviousMonth")
        self.onPreviousYear = create_callback(onPreviousYear, "onPreviousYear")
        self.onYearMouseEnter = create_callback(onYearMouseEnter, "onYearMouseEnter")
        self.onYearSelect = create_callback(onYearSelect, "onYearSelect")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.previousIcon = previousIcon
        self.previousLabel = previousLabel
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.renderDay = renderDay
        self.size = size
        self.static = static
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.weekdayFormat = weekdayFormat
        self.weekendDays = weekendDays
        self.withCellSpacing = withCellSpacing
        self.yearLabelFormat = yearLabelFormat
        self.yearsListFormat = yearsListFormat
