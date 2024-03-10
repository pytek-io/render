from render import Component, create_callback, Props


class AreaChart(Component):
    Module = "mantine/charts"
    JSXName = "AreaChart"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "activeDotProps",
        "areaChartProps",
        "areaProps",
        "component",
        "connectNulls",
        "curveType",
        "data",
        "dataKey",
        "dotProps",
        "fillOpacity",
        "gridAxis",
        "gridColor",
        "gridProps",
        "h",
        "href",
        "legendProps",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "orientation",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "referenceLines",
        "series",
        "splitColors",
        "splitOffset",
        "strokeDasharray",
        "strokeWidth",
        "sx",
        "ta",
        "target",
        "textColor",
        "tickLine",
        "title",
        "tooltipAnimationDuration",
        "tooltipProps",
        "type",
        "unit",
        "valueFormatter",
        "variant",
        "withDots",
        "withGradient",
        "withLegend",
        "withTooltip",
        "withXAxis",
        "withYAxis",
        "xAxisProps",
        "yAxisProps",
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
        activeDotProps=None,
        areaChartProps=None,
        areaProps=None,
        component=None,
        connectNulls=None,
        curveType=None,
        data=None,
        dataKey=None,
        dotProps=None,
        fillOpacity=None,
        gridAxis=None,
        gridColor=None,
        gridProps=None,
        h=None,
        href=None,
        legendProps=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        orientation=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        referenceLines=None,
        series=None,
        splitColors=None,
        splitOffset=None,
        strokeDasharray=None,
        strokeWidth=None,
        sx=None,
        ta=None,
        target=None,
        textColor=None,
        tickLine=None,
        title=None,
        tooltipAnimationDuration=None,
        tooltipProps=None,
        type=None,
        unit=None,
        valueFormatter=None,
        variant=None,
        withDots=None,
        withGradient=None,
        withLegend=None,
        withTooltip=None,
        withXAxis=None,
        withYAxis=None,
        xAxisProps=None,
        yAxisProps=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.activeDotProps = activeDotProps
        self.areaChartProps = areaChartProps
        self.areaProps = areaProps
        self.component = component
        self.connectNulls = connectNulls
        self.curveType = curveType
        self.data = data
        self.dataKey = dataKey
        self.dotProps = dotProps
        self.fillOpacity = fillOpacity
        self.gridAxis = gridAxis
        self.gridColor = gridColor
        self.gridProps = gridProps
        self.h = h
        self.href = href
        self.legendProps = legendProps
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.referenceLines = referenceLines
        self.series = series
        self.splitColors = splitColors
        self.splitOffset = splitOffset
        self.strokeDasharray = strokeDasharray
        self.strokeWidth = strokeWidth
        self.sx = sx
        self.ta = ta
        self.target = target
        self.textColor = textColor
        self.tickLine = tickLine
        self.title = title
        self.tooltipAnimationDuration = tooltipAnimationDuration
        self.tooltipProps = tooltipProps
        self.type = type
        self.unit = unit
        self.valueFormatter = valueFormatter
        self.variant = variant
        self.withDots = withDots
        self.withGradient = withGradient
        self.withLegend = withLegend
        self.withTooltip = withTooltip
        self.withXAxis = withXAxis
        self.withYAxis = withYAxis
        self.xAxisProps = xAxisProps
        self.yAxisProps = yAxisProps
