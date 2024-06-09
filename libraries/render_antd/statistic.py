from render import Component, create_callback


class Statistic(Component):
    Module = "antd"
    JSXName = "Statistic"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "decimalSeparator",
        "formatter",
        "groupSeparator",
        "loading",
        "precision",
        "prefix",
        "suffix",
        "title",
        "value",
        "valueStyle",
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
        decimalSeparator=None,
        formatter=None,
        groupSeparator=None,
        loading=None,
        precision=None,
        prefix=None,
        suffix=None,
        title=None,
        value=None,
        valueStyle=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.decimalSeparator = decimalSeparator
        self.formatter = formatter
        self.groupSeparator = groupSeparator
        self.loading = loading
        self.precision = precision
        self.prefix = prefix
        self.suffix = suffix
        self.title = title
        self.value = value
        self.valueStyle = valueStyle

    class Countdown(Component):
        Module = "antd"
        JSXName = "Statistic.Countdown"
        CALLBACKS = ["onKeyPress", "onClick", "onChange", "onFinish"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "format",
            "prefix",
            "suffix",
            "title",
            "value",
            "valueStyle",
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
            format=None,
            onChange=None,
            onFinish=None,
            prefix=None,
            suffix=None,
            title=None,
            value=None,
            valueStyle=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.format = format
            self.onChange = create_callback(onChange, "onChange", [[0]])
            self.onFinish = create_callback(onFinish, "onFinish")
            self.prefix = prefix
            self.suffix = suffix
            self.title = title
            self.value = value
            self.valueStyle = valueStyle
