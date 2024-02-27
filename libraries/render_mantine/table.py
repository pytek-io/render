from render import Component, create_callback


class Table(Component):
    Module = "mantine"
    JSXName = "Table"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "borderColor",
        "captionSide",
        "data",
        "highlightOnHover",
        "highlightOnHoverColor",
        "horizontalSpacing",
        "layout",
        "stickyHeader",
        "stickyHeaderOffset",
        "striped",
        "stripedColor",
        "verticalSpacing",
        "withColumnBorders",
        "withRowBorders",
        "withTableBorder",
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
        borderColor=None,
        captionSide=None,
        data=None,
        highlightOnHover=None,
        highlightOnHoverColor=None,
        horizontalSpacing=None,
        layout=None,
        stickyHeader=None,
        stickyHeaderOffset=None,
        striped=None,
        stripedColor=None,
        verticalSpacing=None,
        withColumnBorders=None,
        withRowBorders=None,
        withTableBorder=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.borderColor = borderColor
        self.captionSide = captionSide
        self.data = data
        self.highlightOnHover = highlightOnHover
        self.highlightOnHoverColor = highlightOnHoverColor
        self.horizontalSpacing = horizontalSpacing
        self.layout = layout
        self.stickyHeader = stickyHeader
        self.stickyHeaderOffset = stickyHeaderOffset
        self.striped = striped
        self.stripedColor = stripedColor
        self.verticalSpacing = verticalSpacing
        self.withColumnBorders = withColumnBorders
        self.withRowBorders = withRowBorders
        self.withTableBorder = withTableBorder
