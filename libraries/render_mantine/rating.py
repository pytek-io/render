from render import Component, create_callback


class Rating(Component):
    Module = "mantine"
    JSXName = "Rating"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onHover"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "count",
        "defaultValue",
        "emptySymbol",
        "fractions",
        "fullSymbol",
        "getSymbolLabel",
        "highlightSelectedOnly",
        "name",
        "readOnly",
        "size",
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
        color=None,
        count=None,
        defaultValue=None,
        emptySymbol=None,
        fractions=None,
        fullSymbol=None,
        getSymbolLabel=None,
        highlightSelectedOnly=None,
        name=None,
        onChange=None,
        onHover=None,
        readOnly=None,
        size=None,
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
        self.color = color
        self.count = count
        self.defaultValue = defaultValue
        self.emptySymbol = emptySymbol
        self.fractions = fractions
        self.fullSymbol = fullSymbol
        self.getSymbolLabel = getSymbolLabel
        self.highlightSelectedOnly = highlightSelectedOnly
        self.name = name
        self.onChange = create_callback(onChange, "onChange")
        self.onHover = create_callback(onHover, "onHover")
        self.readOnly = readOnly
        self.size = size
        self.value = value
