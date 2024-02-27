from render import Component, create_callback, Props


class Input(Component):
    Module = "mantine"
    JSXName = "Input"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "disabled",
        "error",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "multiline",
        "pointer",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "withAria",
        "withErrorStyles",
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
        disabled=None,
        error=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        multiline=None,
        pointer=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        withAria=None,
        withErrorStyles=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.disabled = disabled
        self.error = error
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.multiline = multiline
        self.pointer = pointer
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.withAria = withAria
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps

    class Description(Component):
        Module = "mantine"
        JSXName = "Input.Description"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "size"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            size=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.size = size

    class Error(Component):
        Module = "mantine"
        JSXName = "Input.Error"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "size"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            size=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.size = size

    class Label(Component):
        Module = "mantine"
        JSXName = "Input.Label"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "labelElement", "required", "size"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            labelElement=None,
            required=None,
            size=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.labelElement = labelElement
            self.required = required
            self.size = size

    class Wrapper(Component):
        Module = "mantine"
        JSXName = "Input.Wrapper"
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
            "required",
            "size",
            "withAsterisk",
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
            description=None,
            descriptionProps=None,
            error=None,
            errorProps=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelElement=None,
            labelProps=None,
            required=None,
            size=None,
            withAsterisk=None,
            controller=None,
        ):
            super().__init__(key, controller)
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
            self.required = required
            self.size = size
            self.withAsterisk = withAsterisk
