from render import Component, create_callback


class ColorPicker(Component):
    Module = "mantine/core"
    JSXName = "ColorPicker"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onChange",
        "onChangeEnd",
        "onColorSwatchClick",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alphaLabel",
        "component",
        "defaultValue",
        "focusable",
        "format",
        "fullWidth",
        "h",
        "href",
        "hueLabel",
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
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "saturationLabel",
        "size",
        "swatches",
        "swatchesPerRow",
        "sx",
        "ta",
        "target",
        "title",
        "value",
        "variant",
        "withPicker",
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
        alphaLabel=None,
        component=None,
        defaultValue=None,
        focusable=None,
        format=None,
        fullWidth=None,
        h=None,
        href=None,
        hueLabel=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        onChange=None,
        onChangeEnd=None,
        onColorSwatchClick=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        saturationLabel=None,
        size=None,
        swatches=None,
        swatchesPerRow=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        value=None,
        variant=None,
        withPicker=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alphaLabel = alphaLabel
        self.component = component
        self.defaultValue = defaultValue
        self.focusable = focusable
        self.format = format
        self.fullWidth = fullWidth
        self.h = h
        self.href = href
        self.hueLabel = hueLabel
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onChange = create_callback(onChange, "onChange")
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.onColorSwatchClick = create_callback(
            onColorSwatchClick, "onColorSwatchClick"
        )
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.saturationLabel = saturationLabel
        self.size = size
        self.swatches = swatches
        self.swatchesPerRow = swatchesPerRow
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.value = value
        self.variant = variant
        self.withPicker = withPicker
