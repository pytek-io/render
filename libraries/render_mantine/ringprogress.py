from render import Component, create_callback


class RingProgress(Component):
    Module = "mantine"
    JSXName = "RingProgress"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "label",
        "rootColor",
        "roundCaps",
        "sections",
        "size",
        "thickness",
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
        label=None,
        rootColor=None,
        roundCaps=None,
        sections=None,
        size=None,
        thickness=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.label = label
        self.rootColor = rootColor
        self.roundCaps = roundCaps
        self.sections = sections
        self.size = size
        self.thickness = thickness
