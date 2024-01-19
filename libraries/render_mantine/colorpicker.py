from render import Component, create_callback


class ColorPicker(Component):
    Module = "mantine"
    JSXName = "ColorPicker"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "__staticSelector",
        "alphaLabel",
        "defaultValue",
        "focusable",
        "format",
        "fullWidth",
        "hueLabel",
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
        "pt",
        "px",
        "py",
        "saturationLabel",
        "size",
        "swatches",
        "swatchesPerRow",
        "sx",
        "value",
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
        __staticSelector=None,
        alphaLabel=None,
        defaultValue=None,
        focusable=None,
        format=None,
        fullWidth=None,
        hueLabel=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onChange=None,
        onChangeEnd=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        saturationLabel=None,
        size=None,
        swatches=None,
        swatchesPerRow=None,
        sx=None,
        value=None,
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
        self.__staticSelector = __staticSelector
        self.alphaLabel = alphaLabel
        self.defaultValue = defaultValue
        self.focusable = focusable
        self.format = format
        self.fullWidth = fullWidth
        self.hueLabel = hueLabel
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onChange = create_callback(onChange, "onChange")
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.saturationLabel = saturationLabel
        self.size = size
        self.swatches = swatches
        self.swatchesPerRow = swatchesPerRow
        self.sx = sx
        self.value = value
        self.withPicker = withPicker
