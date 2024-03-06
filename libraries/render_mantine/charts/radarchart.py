from render import Component, create_callback, Props


class RadarChart(Component):
    Module = "mantine/charts"
    JSXName = "RadarChart"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "data",
        "dataKey",
        "gridColor",
        "h",
        "href",
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
        "pb",
        "pe",
        "pl",
        "polarAngleAxisProps",
        "polarGridProps",
        "polarRadiusAxisProps",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radarChartProps",
        "radarProps",
        "series",
        "sx",
        "ta",
        "target",
        "textColor",
        "variant",
        "withPolarAngleAxis",
        "withPolarGrid",
        "withPolarRadiusAxis",
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
        component=None,
        data=None,
        dataKey=None,
        gridColor=None,
        h=None,
        href=None,
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
        pb=None,
        pe=None,
        pl=None,
        polarAngleAxisProps=None,
        polarGridProps=None,
        polarRadiusAxisProps=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radarChartProps=None,
        radarProps=None,
        series=None,
        sx=None,
        ta=None,
        target=None,
        textColor=None,
        variant=None,
        withPolarAngleAxis=None,
        withPolarGrid=None,
        withPolarRadiusAxis=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.component = component
        self.data = data
        self.dataKey = dataKey
        self.gridColor = gridColor
        self.h = h
        self.href = href
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
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.polarAngleAxisProps = polarAngleAxisProps
        self.polarGridProps = polarGridProps
        self.polarRadiusAxisProps = polarRadiusAxisProps
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radarChartProps = radarChartProps
        self.radarProps = radarProps
        self.series = series
        self.sx = sx
        self.ta = ta
        self.target = target
        self.textColor = textColor
        self.variant = variant
        self.withPolarAngleAxis = withPolarAngleAxis
        self.withPolarGrid = withPolarGrid
        self.withPolarRadiusAxis = withPolarRadiusAxis
