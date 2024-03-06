from render import Component, create_callback


class NumberFormatter(Component):
    Module = "mantine/core"
    JSXName = "NumberFormatter"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowNegative",
        "component",
        "decimalScale",
        "decimalSeparator",
        "fixedDecimalScale",
        "h",
        "href",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "pr",
        "prefix",
        "pt",
        "px",
        "py",
        "suffix",
        "sx",
        "ta",
        "target",
        "thousandSeparator",
        "thousandsGroupStyle",
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
        allowNegative=None,
        component=None,
        decimalScale=None,
        decimalSeparator=None,
        fixedDecimalScale=None,
        h=None,
        href=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        prefix=None,
        pt=None,
        px=None,
        py=None,
        suffix=None,
        sx=None,
        ta=None,
        target=None,
        thousandSeparator=None,
        thousandsGroupStyle=None,
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
        self.allowNegative = allowNegative
        self.component = component
        self.decimalScale = decimalScale
        self.decimalSeparator = decimalSeparator
        self.fixedDecimalScale = fixedDecimalScale
        self.h = h
        self.href = href
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.prefix = prefix
        self.pt = pt
        self.px = px
        self.py = py
        self.suffix = suffix
        self.sx = sx
        self.ta = ta
        self.target = target
        self.thousandSeparator = thousandSeparator
        self.thousandsGroupStyle = thousandsGroupStyle
        self.value = value
        self.variant = variant
