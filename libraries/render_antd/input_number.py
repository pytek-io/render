from render import Component, create_callback, InputComponent


class InputNumber(InputComponent):
    Module = "antd"
    JSXName = "InputNumber"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onPressEnter", "onStep"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "addonAfter",
        "addonBefore",
        "autoFocus",
        "changeOnBlur",
        "changeOnWheel",
        "controls",
        "decimalSeparator",
        "disabled",
        "formatter",
        "keyboard",
        "max",
        "min",
        "parser",
        "placeholder",
        "precision",
        "prefix",
        "readOnly",
        "size",
        "status",
        "step",
        "stringMode",
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
        onChange=None,
        defaultValue=None,
        value=None,
        addonAfter=None,
        addonBefore=None,
        autoFocus=None,
        changeOnBlur=None,
        changeOnWheel=None,
        controls=None,
        decimalSeparator=None,
        disabled=None,
        formatter=None,
        keyboard=None,
        max=None,
        min=None,
        onPressEnter=None,
        onStep=None,
        parser=None,
        placeholder=None,
        precision=None,
        prefix=None,
        readOnly=None,
        size=None,
        status=None,
        step=None,
        stringMode=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.addonAfter = addonAfter
        self.addonBefore = addonBefore
        self.autoFocus = autoFocus
        self.changeOnBlur = changeOnBlur
        self.changeOnWheel = changeOnWheel
        self.controls = controls
        self.decimalSeparator = decimalSeparator
        self.disabled = disabled
        self.formatter = formatter
        self.keyboard = keyboard
        self.max = max
        self.min = min
        self.onPressEnter = create_callback(onPressEnter, "onPressEnter")
        self.onStep = create_callback(
            onStep, "onStep", [[0], [1, "offset"], [1, "type"]]
        )
        self.parser = parser
        self.placeholder = placeholder
        self.precision = precision
        self.prefix = prefix
        self.readOnly = readOnly
        self.size = size
        self.status = status
        self.step = step
        self.stringMode = stringMode
        self.variant = variant
