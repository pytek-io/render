from render import Component, create_callback


class Spoiler(Component):
    Module = "mantine"
    JSXName = "Spoiler"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "controlRef",
        "hideLabel",
        "initialState",
        "maxHeight",
        "showLabel",
        "transitionDuration",
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
        controlRef=None,
        hideLabel=None,
        initialState=None,
        maxHeight=None,
        showLabel=None,
        transitionDuration=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.controlRef = controlRef
        self.hideLabel = hideLabel
        self.initialState = initialState
        self.maxHeight = maxHeight
        self.showLabel = showLabel
        self.transitionDuration = transitionDuration
