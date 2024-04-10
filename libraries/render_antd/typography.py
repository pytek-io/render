from render import Component, create_callback


class Typography(Component):
    Module = "antd"
    JSXName = "Typography"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")

    class Link(Component):
        Module = "antd"
        JSXName = "Typography.Link"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = ["style", "className", "id", "href", "target", "title"]

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
            self.target = target
            self.title = title

    class Paragraph(Component):
        Module = "antd"
        JSXName = "Typography.Paragraph"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onCancel",
            "onChange",
            "onCopy",
            "onEllipsis",
            "onEnd",
            "onExpand",
            "onStart",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoSize",
            "code",
            "copyable",
            "delete",
            "disabled",
            "editable",
            "editing",
            "ellipsis",
            "enterIcon",
            "expandable",
            "format",
            "icon",
            "italic",
            "mark",
            "maxLength",
            "rows",
            "strong",
            "suffix",
            "symbol",
            "text",
            "tooltip",
            "tooltips",
            "triggerType",
            "type",
            "underline",
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
            autoSize=None,
            code=None,
            copyable=None,
            delete=None,
            disabled=None,
            editable=None,
            editing=None,
            ellipsis=None,
            enterIcon=None,
            expandable=None,
            format=None,
            icon=None,
            italic=None,
            mark=None,
            maxLength=None,
            onCancel=None,
            onChange=None,
            onCopy=None,
            onEllipsis=None,
            onEnd=None,
            onExpand=None,
            onStart=None,
            rows=None,
            strong=None,
            suffix=None,
            symbol=None,
            text=None,
            tooltip=None,
            tooltips=None,
            triggerType=None,
            type=None,
            underline=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.autoSize = autoSize
            self.code = code
            self.copyable = copyable
            self.delete = delete
            self.disabled = disabled
            self.editable = editable
            self.editing = editing
            self.ellipsis = ellipsis
            self.enterIcon = enterIcon
            self.expandable = expandable
            self.format = format
            self.icon = icon
            self.italic = italic
            self.mark = mark
            self.maxLength = maxLength
            self.onCancel = create_callback(onCancel, "onCancel")
            self.onChange = create_callback(onChange, "onChange", [[0]])
            self.onCopy = create_callback(onCopy, "onCopy")
            self.onEllipsis = create_callback(onEllipsis, "onEllipsis", [[0]])
            self.onEnd = create_callback(onEnd, "onEnd")
            self.onExpand = create_callback(onExpand, "onExpand")
            self.onStart = create_callback(onStart, "onStart")
            self.rows = rows
            self.strong = strong
            self.suffix = suffix
            self.symbol = symbol
            self.text = text
            self.tooltip = tooltip
            self.tooltips = tooltips
            self.triggerType = triggerType
            self.type = type
            self.underline = underline

    class Text(Component):
        Module = "antd"
        JSXName = "Typography.Text"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "code",
            "copyable",
            "delete",
            "disabled",
            "editable",
            "ellipsis",
            "italic",
            "keyboard",
            "mark",
            "strong",
            "type",
            "underline",
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
            code=None,
            copyable=None,
            delete=None,
            disabled=None,
            editable=None,
            ellipsis=None,
            italic=None,
            keyboard=None,
            mark=None,
            strong=None,
            type=None,
            underline=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.code = code
            self.copyable = copyable
            self.delete = delete
            self.disabled = disabled
            self.editable = editable
            self.ellipsis = ellipsis
            self.italic = italic
            self.keyboard = keyboard
            self.mark = mark
            self.strong = strong
            self.type = type
            self.underline = underline

    class Title(Component):
        Module = "antd"
        JSXName = "Typography.Title"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "code",
            "copyable",
            "delete",
            "disabled",
            "editable",
            "ellipsis",
            "italic",
            "level",
            "mark",
            "type",
            "underline",
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
            code=None,
            copyable=None,
            delete=None,
            disabled=None,
            editable=None,
            ellipsis=None,
            italic=None,
            level=None,
            mark=None,
            type=None,
            underline=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.code = code
            self.copyable = copyable
            self.delete = delete
            self.disabled = disabled
            self.editable = editable
            self.ellipsis = ellipsis
            self.italic = italic
            self.level = level
            self.mark = mark
            self.type = type
            self.underline = underline
