from render import Component, create_callback, Props


class PinInput(Component):
    Module = "mantine"
    JSXName = "PinInput"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onComplete"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "ariaLabel",
        "autoFocus",
        "defaultValue",
        "disabled",
        "error",
        "form",
        "gap",
        "hiddenInputProps",
        "inputMode",
        "inputType",
        "length",
        "manageFocus",
        "mask",
        "name",
        "oneTimeCode",
        "placeholder",
        "radius",
        "readOnly",
        "size",
        "type",
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
        ariaLabel=None,
        autoFocus=None,
        defaultValue=None,
        disabled=None,
        error=None,
        form=None,
        gap=None,
        hiddenInputProps=None,
        inputMode=None,
        inputType=None,
        length=None,
        manageFocus=None,
        mask=None,
        name=None,
        onChange=None,
        onComplete=None,
        oneTimeCode=None,
        placeholder=None,
        radius=None,
        readOnly=None,
        size=None,
        type=None,
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
        self.ariaLabel = ariaLabel
        self.autoFocus = autoFocus
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.error = error
        self.form = form
        self.gap = gap
        self.hiddenInputProps = hiddenInputProps
        self.inputMode = inputMode
        self.inputType = inputType
        self.length = length
        self.manageFocus = manageFocus
        self.mask = mask
        self.name = name
        self.onChange = create_callback(onChange, "onChange")
        self.onComplete = create_callback(onComplete, "onComplete")
        self.oneTimeCode = oneTimeCode
        self.placeholder = placeholder
        self.radius = radius
        self.readOnly = readOnly
        self.size = size
        self.type = type
        self.value = value
