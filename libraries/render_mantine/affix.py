from render import Component, create_callback, Props


class Affix(Component):
    Module = "mantine"
    JSXName = "Affix"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "portalProps",
        "position",
        "withinPortal",
        "zIndex",
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
        portalProps=None,
        position=None,
        withinPortal=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.portalProps = portalProps
        self.position = position
        self.withinPortal = withinPortal
        self.zIndex = zIndex
