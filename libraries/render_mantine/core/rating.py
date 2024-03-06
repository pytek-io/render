from render import Component, create_callback


class Rating(Component):
    Module = "mantine/core"
    JSXName = "Rating"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onHover"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "component",
        "count",
        "defaultValue",
        "emptySymbol",
        "fractions",
        "fullSymbol",
        "getSymbolLabel",
        "h",
        "highlightSelectedOnly",
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
        "name",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "readOnly",
        "size",
        "sx",
        "ta",
        "target",
        "value",
        "variant",
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
        color=None,
        component=None,
        count=None,
        defaultValue=None,
        emptySymbol=None,
        fractions=None,
        fullSymbol=None,
        getSymbolLabel=None,
        h=None,
        highlightSelectedOnly=None,
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
        name=None,
        onChange=None,
        onHover=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        readOnly=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        value=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.component = component
        self.count = count
        self.defaultValue = defaultValue
        self.emptySymbol = emptySymbol
        self.fractions = fractions
        self.fullSymbol = fullSymbol
        self.getSymbolLabel = getSymbolLabel
        self.h = h
        self.highlightSelectedOnly = highlightSelectedOnly
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
        self.name = name
        self.onChange = create_callback(onChange, "onChange")
        self.onHover = create_callback(onHover, "onHover")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.readOnly = readOnly
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.value = value
        self.variant = variant
