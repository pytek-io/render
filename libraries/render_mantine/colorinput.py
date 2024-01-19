from render import Component, create_callback, InputComponent


class ColorInput(InputComponent):
    Module = "mantine"
    JSXName = "ColorInput"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "disallowInput",
        "dropdownZIndex",
        "fixOnBlur",
        "format",
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
        "shadow",
        "size",
        "swatches",
        "swatchesPerRow",
        "sx",
        "transition",
        "transitionDuration",
        "transitionTimingFunction",
        "withPicker",
        "withPreview",
        "withinPortal",
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
        onChange=None,
        defaultValue="",
        value=None,
        disallowInput=None,
        dropdownZIndex=None,
        fixOnBlur=None,
        format=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onChangeEnd=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        shadow=None,
        size=None,
        swatches=None,
        swatchesPerRow=None,
        sx=None,
        transition=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        withPicker=None,
        withPreview=None,
        withinPortal=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.disallowInput = disallowInput
        self.dropdownZIndex = dropdownZIndex
        self.fixOnBlur = fixOnBlur
        self.format = format
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.shadow = shadow
        self.size = size
        self.swatches = swatches
        self.swatchesPerRow = swatchesPerRow
        self.sx = sx
        self.transition = transition
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        self.withPicker = withPicker
        self.withPreview = withPreview
        self.withinPortal = withinPortal
