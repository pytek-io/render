from render import Component, create_callback


class NumberFormatter(Component):
    Module = "mantine"
    JSXName = "NumberFormatter"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowNegative",
        "decimalScale",
        "decimalSeparator",
        "fixedDecimalScale",
        "prefix",
        "suffix",
        "thousandSeparator",
        "thousandsGroupStyle",
        "value",
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
        decimalScale=None,
        decimalSeparator=None,
        fixedDecimalScale=None,
        prefix=None,
        suffix=None,
        thousandSeparator=None,
        thousandsGroupStyle=None,
        value=None,
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
        self.decimalScale = decimalScale
        self.decimalSeparator = decimalSeparator
        self.fixedDecimalScale = fixedDecimalScale
        self.prefix = prefix
        self.suffix = suffix
        self.thousandSeparator = thousandSeparator
        self.thousandsGroupStyle = thousandsGroupStyle
        self.value = value
