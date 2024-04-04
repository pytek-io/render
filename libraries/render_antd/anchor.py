from render import Component, create_callback


class Anchor(Component):
    Module = "antd"
    JSXName = "Anchor"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "affix",
        "bounds",
        "direction",
        "getContainer",
        "getCurrentAnchor",
        "items",
        "offsetTop",
        "replace",
        "showInkInFixed",
        "targetOffset",
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
        affix=None,
        bounds=None,
        direction=None,
        getContainer=None,
        getCurrentAnchor=None,
        items=None,
        offsetTop=None,
        onChange=None,
        replace=None,
        showInkInFixed=None,
        targetOffset=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick", [[1]])
        self.affix = affix
        self.bounds = bounds
        self.direction = direction
        self.getContainer = getContainer
        self.getCurrentAnchor = getCurrentAnchor
        self.items = items
        self.offsetTop = offsetTop
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.replace = replace
        self.showInkInFixed = showInkInFixed
        self.targetOffset = targetOffset

    class Item(Component):
        Module = "antd"
        JSXName = "Anchor.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "href", "replace", "target", "title"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            href=None,
            replace=None,
            target=None,
            title=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.href = href
            self.replace = replace
            self.target = target
            self.title = title
