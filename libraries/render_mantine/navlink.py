from render import Component, create_callback


class NavLink(Component):
    Module = "mantine"
    JSXName = "NavLink"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onKeyDown"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "autoContrast",
        "childrenOffset",
        "color",
        "defaultOpened",
        "description",
        "disableRightSectionRotation",
        "disabled",
        "label",
        "leftSection",
        "noWrap",
        "opened",
        "rightSection",
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
        autoContrast=None,
        childrenOffset=None,
        color=None,
        defaultOpened=None,
        description=None,
        disableRightSectionRotation=None,
        disabled=None,
        label=None,
        leftSection=None,
        noWrap=None,
        onChange=None,
        onKeyDown=None,
        opened=None,
        rightSection=None,
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
        self.autoContrast = autoContrast
        self.childrenOffset = childrenOffset
        self.color = color
        self.defaultOpened = defaultOpened
        self.description = description
        self.disableRightSectionRotation = disableRightSectionRotation
        self.disabled = disabled
        self.label = label
        self.leftSection = leftSection
        self.noWrap = noWrap
        self.onChange = create_callback(onChange, "onChange")
        self.onKeyDown = create_callback(onKeyDown, "onKeyDown")
        self.opened = opened
        self.rightSection = rightSection
