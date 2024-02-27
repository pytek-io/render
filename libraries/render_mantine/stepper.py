from render import Component, create_callback


class Stepper(Component):
    Module = "mantine"
    JSXName = "Stepper"
    CALLBACKS = ["onKeyPress", "onClick", "onStepClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "allowNextStepsSelect",
        "autoContrast",
        "color",
        "completedIcon",
        "contentPadding",
        "icon",
        "iconPosition",
        "iconSize",
        "orientation",
        "progressIcon",
        "radius",
        "size",
        "wrap",
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
        active=None,
        allowNextStepsSelect=None,
        autoContrast=None,
        color=None,
        completedIcon=None,
        contentPadding=None,
        icon=None,
        iconPosition=None,
        iconSize=None,
        onStepClick=None,
        orientation=None,
        progressIcon=None,
        radius=None,
        size=None,
        wrap=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.active = active
        self.allowNextStepsSelect = allowNextStepsSelect
        self.autoContrast = autoContrast
        self.color = color
        self.completedIcon = completedIcon
        self.contentPadding = contentPadding
        self.icon = icon
        self.iconPosition = iconPosition
        self.iconSize = iconSize
        self.onStepClick = create_callback(onStepClick, "onStepClick")
        self.orientation = orientation
        self.progressIcon = progressIcon
        self.radius = radius
        self.size = size
        self.wrap = wrap

    class Step(Component):
        Module = "mantine"
        JSXName = "Stepper.Step"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "allowStepClick",
            "allowStepSelect",
            "color",
            "completedIcon",
            "description",
            "icon",
            "iconPosition",
            "iconSize",
            "label",
            "loading",
            "orientation",
            "progressIcon",
            "state",
            "step",
            "withIcon",
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
            allowStepClick=None,
            allowStepSelect=None,
            color=None,
            completedIcon=None,
            description=None,
            icon=None,
            iconPosition=None,
            iconSize=None,
            label=None,
            loading=None,
            orientation=None,
            progressIcon=None,
            state=None,
            step=None,
            withIcon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.allowStepClick = allowStepClick
            self.allowStepSelect = allowStepSelect
            self.color = color
            self.completedIcon = completedIcon
            self.description = description
            self.icon = icon
            self.iconPosition = iconPosition
            self.iconSize = iconSize
            self.label = label
            self.loading = loading
            self.orientation = orientation
            self.progressIcon = progressIcon
            self.state = state
            self.step = step
            self.withIcon = withIcon
