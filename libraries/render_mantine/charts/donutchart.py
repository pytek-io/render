from render import Component, create_callback, Props


class DonutChart(Component):
    Module = "mantine/charts"
    JSXName = "DonutChart"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "chartLabel",
        "component",
        "data",
        "endAngle",
        "h",
        "href",
        "labelColor",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "p",
        "paddingAngle",
        "pb",
        "pe",
        "pieChartProps",
        "pieProps",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "size",
        "startAngle",
        "strokeColor",
        "strokeWidth",
        "sx",
        "ta",
        "target",
        "thickness",
        "title",
        "tooltipAnimationDuration",
        "tooltipDataSource",
        "tooltipProps",
        "valueFormatter",
        "variant",
        "withLabels",
        "withLabelsLine",
        "withTooltip",
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
        chartLabel=None,
        component=None,
        data=None,
        endAngle=None,
        h=None,
        href=None,
        labelColor=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        paddingAngle=None,
        pb=None,
        pe=None,
        pieChartProps=None,
        pieProps=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        startAngle=None,
        strokeColor=None,
        strokeWidth=None,
        sx=None,
        ta=None,
        target=None,
        thickness=None,
        title=None,
        tooltipAnimationDuration=None,
        tooltipDataSource=None,
        tooltipProps=None,
        valueFormatter=None,
        variant=None,
        withLabels=None,
        withLabelsLine=None,
        withTooltip=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.chartLabel = chartLabel
        self.component = component
        self.data = data
        self.endAngle = endAngle
        self.h = h
        self.href = href
        self.labelColor = labelColor
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.paddingAngle = paddingAngle
        self.pb = pb
        self.pe = pe
        self.pieChartProps = pieChartProps
        self.pieProps = pieProps
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.startAngle = startAngle
        self.strokeColor = strokeColor
        self.strokeWidth = strokeWidth
        self.sx = sx
        self.ta = ta
        self.target = target
        self.thickness = thickness
        self.title = title
        self.tooltipAnimationDuration = tooltipAnimationDuration
        self.tooltipDataSource = tooltipDataSource
        self.tooltipProps = tooltipProps
        self.valueFormatter = valueFormatter
        self.variant = variant
        self.withLabels = withLabels
        self.withLabelsLine = withLabelsLine
        self.withTooltip = withTooltip
