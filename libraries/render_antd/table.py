from render import Component, create_callback, Props


class Table(Component):
    Module = "antd"
    JSXName = "Table"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onCell",
        "onChange",
        "onExpand",
        "onExpandedRowsChange",
        "onHeaderRow",
        "onRow",
        "onSelect",
        "onSelectAll",
        "onSelectInvert",
        "onSelectMultiple",
        "onSelectNone",
        "scrollTo",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "bordered",
        "checkStrictly",
        "childrenColumnName",
        "columnTitle",
        "columnWidth",
        "columns",
        "components",
        "dataSource",
        "defaultExpandAllRows",
        "defaultExpandedRowKeys",
        "expandIcon",
        "expandRowByClick",
        "expandable",
        "expandedRowClassName",
        "expandedRowKeys",
        "expandedRowRender",
        "fixed",
        "footer",
        "getCheckboxProps",
        "getPopupContainer",
        "hideSelectAll",
        "indentSize",
        "loading",
        "locale",
        "nativeElement",
        "pagination",
        "position",
        "preserveSelectedRowKeys",
        "renderCell",
        "rowClassName",
        "rowExpandable",
        "rowKey",
        "rowSelection",
        "scroll",
        "scrollToFirstRowOnChange",
        "selectedRowKeys",
        "selections",
        "showExpandColumn",
        "showHeader",
        "showSorterTooltip",
        "size",
        "sortDirections",
        "sticky",
        "summary",
        "tableLayout",
        "text",
        "title",
        "type",
        "virtual",
        "x",
        "y",
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
        bordered=None,
        checkStrictly=None,
        childrenColumnName=None,
        columnTitle=None,
        columnWidth=None,
        columns=None,
        components=None,
        dataSource=None,
        defaultExpandAllRows=None,
        defaultExpandedRowKeys=None,
        expandIcon=None,
        expandRowByClick=None,
        expandable=None,
        expandedRowClassName=None,
        expandedRowKeys=None,
        expandedRowRender=None,
        fixed=None,
        footer=None,
        getCheckboxProps=None,
        getPopupContainer=None,
        hideSelectAll=None,
        indentSize=None,
        loading=None,
        locale=None,
        nativeElement=None,
        onCell=None,
        onChange=None,
        onExpand=None,
        onExpandedRowsChange=None,
        onHeaderRow=None,
        onRow=None,
        onSelect=None,
        onSelectAll=None,
        onSelectInvert=None,
        onSelectMultiple=None,
        onSelectNone=None,
        pagination=None,
        position=None,
        preserveSelectedRowKeys=None,
        renderCell=None,
        rowClassName=None,
        rowExpandable=None,
        rowKey=None,
        rowSelection=None,
        scroll=None,
        scrollTo=None,
        scrollToFirstRowOnChange=None,
        selectedRowKeys=None,
        selections=None,
        showExpandColumn=None,
        showHeader=None,
        showSorterTooltip=None,
        size=None,
        sortDirections=None,
        sticky=None,
        summary=None,
        tableLayout=None,
        text=None,
        title=None,
        type=None,
        virtual=None,
        x=None,
        y=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.bordered = bordered
        self.checkStrictly = checkStrictly
        self.childrenColumnName = childrenColumnName
        self.columnTitle = columnTitle
        self.columnWidth = columnWidth
        self.columns = columns
        self.components = components
        self.dataSource = dataSource
        self.defaultExpandAllRows = defaultExpandAllRows
        self.defaultExpandedRowKeys = defaultExpandedRowKeys
        self.expandIcon = expandIcon
        self.expandRowByClick = expandRowByClick
        self.expandable = expandable
        self.expandedRowClassName = expandedRowClassName
        self.expandedRowKeys = expandedRowKeys
        self.expandedRowRender = expandedRowRender
        self.fixed = fixed
        self.footer = footer
        self.getCheckboxProps = getCheckboxProps
        self.getPopupContainer = getPopupContainer
        self.hideSelectAll = hideSelectAll
        self.indentSize = indentSize
        self.loading = loading
        self.locale = locale
        self.nativeElement = nativeElement
        self.onCell = create_callback(onCell, "onCell", [[1]])
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onExpand = create_callback(onExpand, "onExpand")
        self.onExpandedRowsChange = create_callback(
            onExpandedRowsChange, "onExpandedRowsChange", [[0]]
        )
        self.onHeaderRow = create_callback(onHeaderRow, "onHeaderRow", [[0], [1]])
        self.onRow = create_callback(onRow, "onRow", [[1]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0]])
        self.onSelectAll = create_callback(onSelectAll, "onSelectAll", [[0], [1], [2]])
        self.onSelectInvert = create_callback(onSelectInvert, "onSelectInvert", [[0]])
        self.onSelectMultiple = create_callback(
            onSelectMultiple, "onSelectMultiple", [[0], [1], [2]]
        )
        self.onSelectNone = create_callback(onSelectNone, "onSelectNone")
        self.pagination = pagination
        self.position = position
        self.preserveSelectedRowKeys = preserveSelectedRowKeys
        self.renderCell = renderCell
        self.rowClassName = rowClassName
        self.rowExpandable = rowExpandable
        self.rowKey = rowKey
        self.rowSelection = rowSelection
        self.scroll = scroll
        self.scrollTo = create_callback(scrollTo, "scrollTo")
        self.scrollToFirstRowOnChange = scrollToFirstRowOnChange
        self.selectedRowKeys = selectedRowKeys
        self.selections = selections
        self.showExpandColumn = showExpandColumn
        self.showHeader = showHeader
        self.showSorterTooltip = showSorterTooltip
        self.size = size
        self.sortDirections = sortDirections
        self.sticky = sticky
        self.summary = summary
        self.tableLayout = tableLayout
        self.text = text
        self.title = title
        self.type = type
        self.virtual = virtual
        self.x = x
        self.y = y
