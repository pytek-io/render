from render import Component, create_callback, InputComponent, Props


class Switch(InputComponent):
    Module = "mantine"
    JSXName = "Switch"
    InputName = "checked"
    CALLBACKS = ["onKeyPress", "onClick", "onLabel"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "description",
        "error",
        "label",
        "labelPosition",
        "offLabel",
        "radius",
        "rootRef",
        "size",
        "thumbIcon",
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
        color=None,
        description=None,
        error=None,
        label=None,
        labelPosition=None,
        offLabel=None,
        onLabel=None,
        radius=None,
        rootRef=None,
        size=None,
        thumbIcon=None,
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
        self.color = color
        self.description = description
        self.error = error
        self.label = label
        self.labelPosition = labelPosition
        self.offLabel = offLabel
        self.onLabel = create_callback(onLabel, "onLabel")
        self.radius = radius
        self.rootRef = rootRef
        self.size = size
        self.thumbIcon = thumbIcon
        self.wrapperProps = wrapperProps

    class Group(InputComponent):
        Module = "mantine"
        JSXName = "Switch.Group"
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
            self.readOnly = readOnly
            self.required = required
            self.size = size
            self.withAsterisk = withAsterisk
            self.wrapperProps = wrapperProps
