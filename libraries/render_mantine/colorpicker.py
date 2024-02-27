from render import Component, create_callback


class ColorPicker(Component):
    Module = "mantine"
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
        "defaultValue",
        "focusable",
        "format",
        "fullWidth",
        "hueLabel",
        "saturationLabel",
        "size",
        "swatches",
        "swatchesPerRow",
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
        alphaLabel=None,
        defaultValue=None,
        focusable=None,
        format=None,
        fullWidth=None,
        hueLabel=None,
        onChange=None,
        onChangeEnd=None,
        onColorSwatchClick=None,
        saturationLabel=None,
        size=None,
        swatches=None,
        swatchesPerRow=None,
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
        self.alphaLabel = alphaLabel
        self.defaultValue = defaultValue
        self.focusable = focusable
        self.format = format
        self.fullWidth = fullWidth
        self.hueLabel = hueLabel
        self.onChange = create_callback(onChange, "onChange")
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.onColorSwatchClick = create_callback(
            onColorSwatchClick, "onColorSwatchClick"
        )
        self.saturationLabel = saturationLabel
        self.size = size
        self.swatches = swatches
        self.swatchesPerRow = swatchesPerRow
        self.value = value
        self.withPicker = withPicker
