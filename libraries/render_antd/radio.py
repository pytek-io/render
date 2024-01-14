from render import Component, create_callback, InputComponent


class Radio(Component):
    Module = "ant"
    JSXName = "Radio"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        autoFocus=None,
        checked=None,
        defaultChecked=None,
        disabled=None,
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
        self.autoFocus = autoFocus
        self.checked = checked
        self.defaultChecked = defaultChecked
        self.disabled = disabled
        self.value = value


class RadioGroup(InputComponent):
    Module = "ant"
    JSXName = "Radio.Group"
    InputName = "value"

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
        buttonStyle=None,
        disabled=None,
        name=None,
        optionType=None,
        options=None,
        size=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.buttonStyle = buttonStyle
        self.disabled = disabled
        self.name = name
        self.optionType = optionType
        self.options = options
        self.size = size
