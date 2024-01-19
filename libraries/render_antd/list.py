from render import Component, create_callback


class List(Component):
    Module = "antd"
    JSXName = "List"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "bordered",
        "column",
        "dataSource",
        "footer",
        "grid",
        "gutter",
        "header",
        "itemLayout",
        "lg",
        "loadMore",
        "loading",
        "locale",
        "md",
        "pagination",
        "position",
        "renderItem",
        "rowKey",
        "size",
        "sm",
        "split",
        "xl",
        "xs",
        "xxl",
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
        align=None,
        bordered=None,
        column=None,
        dataSource=None,
        footer=None,
        grid=None,
        gutter=None,
        header=None,
        itemLayout=None,
        lg=None,
        loadMore=None,
        loading=None,
        locale=None,
        md=None,
        pagination=None,
        position=None,
        renderItem=None,
        rowKey=None,
        size=None,
        sm=None,
        split=None,
        xl=None,
        xs=None,
        xxl=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.bordered = bordered
        self.column = column
        self.dataSource = dataSource
        self.footer = footer
        self.grid = grid
        self.gutter = gutter
        self.header = header
        self.itemLayout = itemLayout
        self.lg = lg
        self.loadMore = loadMore
        self.loading = loading
        self.locale = locale
        self.md = md
        self.pagination = pagination
        self.position = position
        self.renderItem = renderItem
        self.rowKey = rowKey
        self.size = size
        self.sm = sm
        self.split = split
        self.xl = xl
        self.xs = xs
        self.xxl = xxl


class Item(Component):
    Module = "antd"
    JSXName = "List.Item"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "actions",
        "avatar",
        "description",
        "extra",
        "title",
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
        actions=None,
        avatar=None,
        description=None,
        extra=None,
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
        self.actions = actions
        self.avatar = avatar
        self.description = description
        self.extra = extra
        self.title = title
