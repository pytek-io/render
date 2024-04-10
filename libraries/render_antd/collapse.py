from render import Component, create_callback


class Collapse(Component):
    Module = "antd"
    JSXName = "Collapse"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "accordion",
        "activeKey",
        "bordered",
        "collapsible",
        "defaultActiveKey",
        "destroyInactivePanel",
        "expandIcon",
        "expandIconPosition",
        "ghost",
        "items",
        "size",
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
        accordion=None,
        activeKey=None,
        bordered=None,
        collapsible=None,
        defaultActiveKey=None,
        destroyInactivePanel=None,
        expandIcon=None,
        expandIconPosition=None,
        ghost=None,
        items=None,
        onChange=None,
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
        self.accordion = accordion
        self.activeKey = activeKey
        self.bordered = bordered
        self.collapsible = collapsible
        self.defaultActiveKey = defaultActiveKey
        self.destroyInactivePanel = destroyInactivePanel
        self.expandIcon = expandIcon
        self.expandIconPosition = expandIconPosition
        self.ghost = ghost
        self.items = items
        self.onChange = create_callback(onChange, "onChange")
        self.size = size

    class Panel(Component):
        Module = "antd"
        JSXName = "Collapse.Panel"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "collapsible",
            "extra",
            "forceRender",
            "header",
            "showArrow",
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
            collapsible=None,
            extra=None,
            forceRender=None,
            header=None,
            showArrow=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.collapsible = collapsible
            self.extra = extra
            self.forceRender = forceRender
            self.header = header
            self.showArrow = showArrow
