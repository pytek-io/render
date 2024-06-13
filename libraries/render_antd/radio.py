from render import Component, create_callback, InputComponent


class Radio(InputComponent):
    Module = "antd"
    JSXName = "Radio"
    InputName = "checked"
    NewValuePath = "target.checked"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "autoFocus", "disabled", "value"]

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
        disabled=None,
        value=None,
        controller=None,
        onChange=None,
        checked=None,
        defaultChecked=None,
    ):
        super().__init__(key, controller, children, onChange, checked, defaultChecked)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoFocus = autoFocus
        self.disabled = disabled
        self.value = value

    class Button(InputComponent):
        Module = "antd"
        JSXName = "Radio.Button"
        InputName = "checked"
        NewValuePath = "target.checked"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "autoFocus", "disabled", "value"]

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
            disabled=None,
            value=None,
            controller=None,
            onChange=None,
            checked=None,
            defaultChecked=None,
        ):
            super().__init__(
                key, controller, children, onChange, checked, defaultChecked
            )
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.autoFocus = autoFocus
            self.disabled = disabled
            self.value = value

    class Group(InputComponent):
        Module = "antd"
        JSXName = "Radio.Group"
        InputName = "value"
        NewValuePath = "target.value"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "buttonStyle",
            "disabled",
            "name",
            "optionType",
            "options",
            "size",
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
            buttonStyle=None,
            disabled=None,
            name=None,
            optionType=None,
            options=None,
            size=None,
            controller=None,
            onChange=None,
            value=None,
            defaultValue=None,
        ):
            super().__init__(key, controller, children, onChange, value, defaultValue)
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
