from render import Component, create_callback, InputComponent


class Pagination(InputComponent):
    Module = "antd"
    JSXName = "Pagination"
    InputName = "current"
    CALLBACKS = ["onKeyPress", "onClick", "onShowSizeChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "defaultPageSize",
        "disabled",
        "hideOnSinglePage",
        "itemRender",
        "pageSize",
        "pageSizeOptions",
        "responsive",
        "showLessItems",
        "showQuickJumper",
        "showSizeChanger",
        "showTitle",
        "showTotal",
        "simple",
        "size",
        "total",
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
        defaultCurrent=None,
        current=None,
        defaultPageSize=None,
        disabled=None,
        hideOnSinglePage=None,
        itemRender=None,
        onShowSizeChange=None,
        pageSize=None,
        pageSizeOptions=None,
        responsive=None,
        showLessItems=None,
        showQuickJumper=None,
        showSizeChanger=None,
        showTitle=None,
        showTotal=None,
        simple=None,
        size=None,
        total=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, current, defaultCurrent)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.defaultPageSize = defaultPageSize
        self.disabled = disabled
        self.hideOnSinglePage = hideOnSinglePage
        self.itemRender = itemRender
        self.onShowSizeChange = create_callback(
            onShowSizeChange, "onShowSizeChange", [[0], [1]]
        )
        self.pageSize = pageSize
        self.pageSizeOptions = pageSizeOptions
        self.responsive = responsive
        self.showLessItems = showLessItems
        self.showQuickJumper = showQuickJumper
        self.showSizeChanger = showSizeChanger
        self.showTitle = showTitle
        self.showTotal = showTotal
        self.simple = simple
        self.size = size
        self.total = total
