from render import Component, create_callback, Props


class Pill(Component):
    Module = "mantine"
    JSXName = "Pill"
    CALLBACKS = ["onKeyPress", "onClick", "onRemove"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "disabled",
        "radius",
        "removeButtonProps",
        "size",
        "withRemoveButton",
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
        onRemove=None,
        radius=None,
        removeButtonProps=None,
        size=None,
        withRemoveButton=None,
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
        self.onRemove = create_callback(onRemove, "onRemove")
        self.radius = radius
        self.removeButtonProps = removeButtonProps
        self.size = size
        self.withRemoveButton = withRemoveButton

    class Group(Component):
        Module = "mantine"
        JSXName = "Pill.Group"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "disabled", "gap", "size"]

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
            gap=None,
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
            self.disabled = disabled
            self.gap = gap
            self.size = size

    class sInput(Component):
        Module = "mantine"
        JSXName = "Pill.sInput"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "description",
            "descriptionProps",
            "disabled",
            "error",
            "errorProps",
            "inputContainer",
            "inputWrapperOrder",
            "label",
            "labelProps",
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
            "withAsterisk",
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
            description=None,
            descriptionProps=None,
            disabled=None,
            error=None,
            errorProps=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelProps=None,
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
            withAsterisk=None,
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
            self.description = description
            self.descriptionProps = descriptionProps
            self.disabled = disabled
            self.error = error
            self.errorProps = errorProps
            self.inputContainer = inputContainer
            self.inputWrapperOrder = inputWrapperOrder
            self.label = label
            self.labelProps = labelProps
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
            self.withAsterisk = withAsterisk
            self.withErrorStyles = withErrorStyles
            self.wrapperProps = wrapperProps
