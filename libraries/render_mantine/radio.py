from render import Component, create_callback, InputComponent, Props


class Radio(InputComponent):
    Module = "mantine"
    JSXName = "Radio"
    InputName = "checked"
    NewValuePath = "currentTarget.value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "description",
        "error",
        "icon",
        "iconColor",
        "label",
        "labelPosition",
        "radius",
        "rootRef",
        "size",
        "wrapperProps",
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
        defaultChecked=None,
        checked=None,
        autoContrast=None,
        color=None,
        description=None,
        error=None,
        icon=None,
        iconColor=None,
        label=None,
        labelPosition=None,
        radius=None,
        rootRef=None,
        size=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.description = description
        self.error = error
        self.icon = icon
        self.iconColor = iconColor
        self.label = label
        self.labelPosition = labelPosition
        self.radius = radius
        self.rootRef = rootRef
        self.size = size
        self.wrapperProps = wrapperProps

    class Group(InputComponent):
        Module = "mantine"
        JSXName = "Radio.Group"
        InputName = "value"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "description",
            "descriptionProps",
            "error",
            "errorProps",
            "inputContainer",
            "inputWrapperOrder",
            "label",
            "labelElement",
            "labelProps",
            "name",
            "readOnly",
            "required",
            "size",
            "withAsterisk",
            "wrapperProps",
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
            description=None,
            descriptionProps=None,
            error=None,
            errorProps=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelElement=None,
            labelProps=None,
            name=None,
            readOnly=None,
            required=None,
            size=None,
            withAsterisk=None,
            wrapperProps=None,
            controller=None,
        ):
            super().__init__(key, controller, onChange, value, defaultValue)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.description = description
            self.descriptionProps = descriptionProps
            self.error = error
            self.errorProps = errorProps
            self.inputContainer = inputContainer
            self.inputWrapperOrder = inputWrapperOrder
            self.label = label
            self.labelElement = labelElement
            self.labelProps = labelProps
            self.name = name
            self.readOnly = readOnly
            self.required = required
            self.size = size
            self.withAsterisk = withAsterisk
            self.wrapperProps = wrapperProps
