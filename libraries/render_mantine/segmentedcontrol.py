from render import Component, create_callback, InputComponent


class SegmentedControl(InputComponent):
    Module = "mantine"
    JSXName = "SegmentedControl"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "data",
        "disabled",
        "fullWidth",
        "name",
        "orientation",
        "radius",
        "readOnly",
        "size",
        "transitionDuration",
        "transitionTimingFunction",
        "withItemsBorders",
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
        autoContrast=None,
        color=None,
        data=None,
        disabled=None,
        fullWidth=None,
        name=None,
        orientation=None,
        radius=None,
        readOnly=None,
        size=None,
        transitionDuration=None,
        transitionTimingFunction=None,
        withItemsBorders=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.data = data
        self.disabled = disabled
        self.fullWidth = fullWidth
        self.name = name
        self.orientation = orientation
        self.radius = radius
        self.readOnly = readOnly
        self.size = size
        self.transitionDuration = transitionDuration
        self.transitionTimingFunction = transitionTimingFunction
        self.withItemsBorders = withItemsBorders
