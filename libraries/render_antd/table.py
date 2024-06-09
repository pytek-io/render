from render import Component, create_callback, Props


class Table(Component):
    Module = "antd"
    JSXName = "Table"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onHeaderRow", "onRow"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "bordered",
        "columns",
        "components",
        "dataSource",
        "expandable",
        "footer",
        "getPopupContainer",
        "loading",
        "locale",
        "pagination",
        "rowClassName",
        "rowKey",
        "rowSelection",
        "scroll",
        "showHeader",
        "showSorterTooltip",
        "size",
        "sortDirections",
        "sticky",
        "summary",
        "tableLayout",
        "title",
        "virtual",
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
        columns=None,
        components=None,
        dataSource=None,
        expandable=None,
        footer=None,
        getPopupContainer=None,
        loading=None,
        locale=None,
        onChange=None,
        onHeaderRow=None,
        onRow=None,
        pagination=None,
        rowClassName=None,
        rowKey=None,
        rowSelection=None,
        scroll=None,
        showHeader=None,
        showSorterTooltip=None,
        size=None,
        sortDirections=None,
        sticky=None,
        summary=None,
        tableLayout=None,
        title=None,
        virtual=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.bordered = bordered
        self.columns = columns
        self.components = components
        self.dataSource = dataSource
        self.expandable = expandable
        self.footer = footer
        self.getPopupContainer = getPopupContainer
        self.loading = loading
        self.locale = locale
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onHeaderRow = create_callback(onHeaderRow, "onHeaderRow", [[0], [1]])
        self.onRow = create_callback(onRow, "onRow", [[1]])
        self.pagination = pagination
        self.rowClassName = rowClassName
        self.rowKey = rowKey
        self.rowSelection = rowSelection
        self.scroll = scroll
        self.showHeader = showHeader
        self.showSorterTooltip = showSorterTooltip
        self.size = size
        self.sortDirections = sortDirections
        self.sticky = sticky
        self.summary = summary
        self.tableLayout = tableLayout
        self.title = title
        self.virtual = virtual

    class Column(Component):
        Module = "antd"
        JSXName = "Table.Column"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onCell",
            "onFilter",
            "onFilterDropdownOpenChange",
            "onHeaderCell",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "align",
            "colSpan",
            "dataIndex",
            "defaultFilteredValue",
            "defaultSortOrder",
            "ellipsis",
            "filterDropdown",
            "filterDropdownOpen",
            "filterIcon",
            "filterMode",
            "filterMultiple",
            "filterOnClose",
            "filterResetToDefaultFilteredValue",
            "filterSearch",
            "filtered",
            "filteredValue",
            "filters",
            "fixed",
            "hidden",
            "render",
            "responsive",
            "rowScope",
            "shouldCellUpdate",
            "showSorterTooltip",
            "sortDirections",
            "sortIcon",
            "sortOrder",
            "sorter",
            "title",
            "width",
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
            colSpan=None,
            dataIndex=None,
            defaultFilteredValue=None,
            defaultSortOrder=None,
            ellipsis=None,
            filterDropdown=None,
            filterDropdownOpen=None,
            filterIcon=None,
            filterMode=None,
            filterMultiple=None,
            filterOnClose=None,
            filterResetToDefaultFilteredValue=None,
            filterSearch=None,
            filtered=None,
            filteredValue=None,
            filters=None,
            fixed=None,
            hidden=None,
            onCell=None,
            onFilter=None,
            onFilterDropdownOpenChange=None,
            onHeaderCell=None,
            render=None,
            responsive=None,
            rowScope=None,
            shouldCellUpdate=None,
            showSorterTooltip=None,
            sortDirections=None,
            sortIcon=None,
            sortOrder=None,
            sorter=None,
            title=None,
            width=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.align = align
            self.colSpan = colSpan
            self.dataIndex = dataIndex
            self.defaultFilteredValue = defaultFilteredValue
            self.defaultSortOrder = defaultSortOrder
            self.ellipsis = ellipsis
            self.filterDropdown = filterDropdown
            self.filterDropdownOpen = filterDropdownOpen
            self.filterIcon = filterIcon
            self.filterMode = filterMode
            self.filterMultiple = filterMultiple
            self.filterOnClose = filterOnClose
            self.filterResetToDefaultFilteredValue = filterResetToDefaultFilteredValue
            self.filterSearch = filterSearch
            self.filtered = filtered
            self.filteredValue = filteredValue
            self.filters = filters
            self.fixed = fixed
            self.hidden = hidden
            self.onCell = create_callback(onCell, "onCell", [[1]])
            self.onFilter = create_callback(onFilter, "onFilter", [[0]])
            self.onFilterDropdownOpenChange = create_callback(
                onFilterDropdownOpenChange, "onFilterDropdownOpenChange", [[0]]
            )
            self.onHeaderCell = create_callback(onHeaderCell, "onHeaderCell", [[0]])
            self.render = render
            self.responsive = responsive
            self.rowScope = rowScope
            self.shouldCellUpdate = shouldCellUpdate
            self.showSorterTooltip = showSorterTooltip
            self.sortDirections = sortDirections
            self.sortIcon = sortIcon
            self.sortOrder = sortOrder
            self.sorter = sorter
            self.title = title
            self.width = width

    class ColumnGroup(Component):
        Module = "antd"
        JSXName = "Table.ColumnGroup"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onCell",
            "onChange",
            "onExpand",
            "onExpandedRowsChange",
            "onSelect",
            "onSelectAll",
            "onSelectInvert",
            "onSelectMultiple",
            "onSelectNone",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "checkStrictly",
            "childrenColumnName",
            "columnTitle",
            "columnWidth",
            "defaultExpandAllRows",
            "defaultExpandedRowKeys",
            "expandIcon",
            "expandRowByClick",
            "expandedRowClassName",
            "expandedRowKeys",
            "expandedRowRender",
            "fixed",
            "getCheckboxProps",
            "hideSelectAll",
            "indentSize",
            "position",
            "preserveSelectedRowKeys",
            "renderCell",
            "rowExpandable",
            "scrollToFirstRowOnChange",
            "selectedRowKeys",
            "selections",
            "showExpandColumn",
            "text",
            "title",
            "type",
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
            checkStrictly=None,
            childrenColumnName=None,
            columnTitle=None,
            columnWidth=None,
            defaultExpandAllRows=None,
            defaultExpandedRowKeys=None,
            expandIcon=None,
            expandRowByClick=None,
            expandedRowClassName=None,
            expandedRowKeys=None,
            expandedRowRender=None,
            fixed=None,
            getCheckboxProps=None,
            hideSelectAll=None,
            indentSize=None,
            onCell=None,
            onChange=None,
            onExpand=None,
            onExpandedRowsChange=None,
            onSelect=None,
            onSelectAll=None,
            onSelectInvert=None,
            onSelectMultiple=None,
            onSelectNone=None,
            position=None,
            preserveSelectedRowKeys=None,
            renderCell=None,
            rowExpandable=None,
            scrollToFirstRowOnChange=None,
            selectedRowKeys=None,
            selections=None,
            showExpandColumn=None,
            text=None,
            title=None,
            type=None,
            x=None,
            y=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.checkStrictly = checkStrictly
            self.childrenColumnName = childrenColumnName
            self.columnTitle = columnTitle
            self.columnWidth = columnWidth
            self.defaultExpandAllRows = defaultExpandAllRows
            self.defaultExpandedRowKeys = defaultExpandedRowKeys
            self.expandIcon = expandIcon
            self.expandRowByClick = expandRowByClick
            self.expandedRowClassName = expandedRowClassName
            self.expandedRowKeys = expandedRowKeys
            self.expandedRowRender = expandedRowRender
            self.fixed = fixed
            self.getCheckboxProps = getCheckboxProps
            self.hideSelectAll = hideSelectAll
            self.indentSize = indentSize
            self.onCell = create_callback(onCell, "onCell", [[1]])
            self.onChange = create_callback(onChange, "onChange", [[0]])
            self.onExpand = create_callback(onExpand, "onExpand")
            self.onExpandedRowsChange = create_callback(
                onExpandedRowsChange, "onExpandedRowsChange", [[0]]
            )
            self.onSelect = create_callback(onSelect, "onSelect", [[0]])
            self.onSelectAll = create_callback(
                onSelectAll, "onSelectAll", [[0], [1], [2]]
            )
            self.onSelectInvert = create_callback(
                onSelectInvert, "onSelectInvert", [[0]]
            )
            self.onSelectMultiple = create_callback(
                onSelectMultiple, "onSelectMultiple", [[0], [1], [2]]
            )
            self.onSelectNone = create_callback(onSelectNone, "onSelectNone")
            self.position = position
            self.preserveSelectedRowKeys = preserveSelectedRowKeys
            self.renderCell = renderCell
            self.rowExpandable = rowExpandable
            self.scrollToFirstRowOnChange = scrollToFirstRowOnChange
            self.selectedRowKeys = selectedRowKeys
            self.selections = selections
            self.showExpandColumn = showExpandColumn
            self.text = text
            self.title = title
            self.type = type
            self.x = x
            self.y = y
