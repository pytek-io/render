from render import Component, create_callback


class AgGridColumn(Component):
    Module = "ag-grid"
    JSXName = "AgGridColumn"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onCellClicked",
        "onCellContextMenu",
        "onCellDoubleClicked",
        "onCellValueChanged",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "aggFunc",
        "allowedAggFuncs",
        "autoHeaderHeight",
        "autoHeight",
        "cellClass",
        "cellClassRules",
        "cellEditor",
        "cellEditorParams",
        "cellEditorPopup",
        "cellEditorPopupPosition",
        "cellEditorSelector",
        "cellRenderer",
        "cellRendererParams",
        "cellRendererSelector",
        "cellStyle",
        "chartDataType",
        "checkboxSelection",
        "colId",
        "colSpan",
        "columnGroupShow",
        "columnsMenuParams",
        "comparator",
        "defaultAggFunc",
        "dndSource",
        "dndSourceOnRowDrag",
        "editable",
        "enableCellChangeFlash",
        "enablePivot",
        "enableRowGroup",
        "enableValue",
        "equals",
        "field",
        "filter",
        "filterParams",
        "filterValueGetter",
        "flex",
        "floatingFilter",
        "floatingFilterComponent",
        "floatingFilterComponentParams",
        "getQuickFilterText",
        "groupId",
        "headerCheckboxSelection",
        "headerCheckboxSelectionFilteredOnly",
        "headerClass",
        "headerComponent",
        "headerComponentParams",
        "headerGroupComponent",
        "headerGroupComponentParams",
        "headerName",
        "headerTooltip",
        "headerValueGetter",
        "hide",
        "icons",
        "initialAggFunc",
        "initialFlex",
        "initialHide",
        "initialPinned",
        "initialPivot",
        "initialPivotIndex",
        "initialRowGroup",
        "initialRowGroupIndex",
        "initialSort",
        "initialSortIndex",
        "initialWidth",
        "keyCreator",
        "lockPinned",
        "lockPosition",
        "lockVisible",
        "marryChildren",
        "maxWidth",
        "menuTabs",
        "minWidth",
        "openByDefault",
        "pinned",
        "pivot",
        "pivotComparator",
        "pivotIndex",
        "pivotKeys",
        "pivotTotalColumnIds",
        "pivotValueColumn",
        "refData",
        "resizable",
        "rowDrag",
        "rowDragText",
        "rowGroup",
        "rowGroupIndex",
        "rowSpan",
        "showDisabledCheckboxes",
        "showRowGroup",
        "singleClickEdit",
        "sort",
        "sortIndex",
        "sortable",
        "sortingOrder",
        "suppressAutoSize",
        "suppressCellFlash",
        "suppressColumnsToolPanel",
        "suppressFillHandle",
        "suppressFiltersToolPanel",
        "suppressHeaderKeyboardEvent",
        "suppressKeyboardEvent",
        "suppressMenu",
        "suppressMovable",
        "suppressNavigable",
        "suppressPaste",
        "suppressSizeToFit",
        "toolPanelClass",
        "tooltipComponent",
        "tooltipComponentParams",
        "tooltipField",
        "tooltipValueGetter",
        "type",
        "unSortIcon",
        "valueFormatter",
        "valueGetter",
        "valueParser",
        "valueSetter",
        "width",
        "wrapHeaderText",
        "wrapText",
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
        aggFunc=None,
        allowedAggFuncs=None,
        autoHeaderHeight=None,
        autoHeight=None,
        cellClass=None,
        cellClassRules=None,
        cellEditor=None,
        cellEditorParams=None,
        cellEditorPopup=None,
        cellEditorPopupPosition=None,
        cellEditorSelector=None,
        cellRenderer=None,
        cellRendererParams=None,
        cellRendererSelector=None,
        cellStyle=None,
        chartDataType=None,
        checkboxSelection=None,
        colId=None,
        colSpan=None,
        columnGroupShow=None,
        columnsMenuParams=None,
        comparator=None,
        defaultAggFunc=None,
        dndSource=None,
        dndSourceOnRowDrag=None,
        editable=None,
        enableCellChangeFlash=None,
        enablePivot=None,
        enableRowGroup=None,
        enableValue=None,
        equals=None,
        field=None,
        filter=None,
        filterParams=None,
        filterValueGetter=None,
        flex=None,
        floatingFilter=None,
        floatingFilterComponent=None,
        floatingFilterComponentParams=None,
        getQuickFilterText=None,
        groupId=None,
        headerCheckboxSelection=None,
        headerCheckboxSelectionFilteredOnly=None,
        headerClass=None,
        headerComponent=None,
        headerComponentParams=None,
        headerGroupComponent=None,
        headerGroupComponentParams=None,
        headerName=None,
        headerTooltip=None,
        headerValueGetter=None,
        hide=None,
        icons=None,
        initialAggFunc=None,
        initialFlex=None,
        initialHide=None,
        initialPinned=None,
        initialPivot=None,
        initialPivotIndex=None,
        initialRowGroup=None,
        initialRowGroupIndex=None,
        initialSort=None,
        initialSortIndex=None,
        initialWidth=None,
        keyCreator=None,
        lockPinned=None,
        lockPosition=None,
        lockVisible=None,
        marryChildren=None,
        maxWidth=None,
        menuTabs=None,
        minWidth=None,
        onCellClicked=None,
        onCellContextMenu=None,
        onCellDoubleClicked=None,
        onCellValueChanged=None,
        openByDefault=None,
        pinned=None,
        pivot=None,
        pivotComparator=None,
        pivotIndex=None,
        pivotKeys=None,
        pivotTotalColumnIds=None,
        pivotValueColumn=None,
        refData=None,
        resizable=None,
        rowDrag=None,
        rowDragText=None,
        rowGroup=None,
        rowGroupIndex=None,
        rowSpan=None,
        showDisabledCheckboxes=None,
        showRowGroup=None,
        singleClickEdit=None,
        sort=None,
        sortIndex=None,
        sortable=None,
        sortingOrder=None,
        suppressAutoSize=None,
        suppressCellFlash=None,
        suppressColumnsToolPanel=None,
        suppressFillHandle=None,
        suppressFiltersToolPanel=None,
        suppressHeaderKeyboardEvent=None,
        suppressKeyboardEvent=None,
        suppressMenu=None,
        suppressMovable=None,
        suppressNavigable=None,
        suppressPaste=None,
        suppressSizeToFit=None,
        toolPanelClass=None,
        tooltipComponent=None,
        tooltipComponentParams=None,
        tooltipField=None,
        tooltipValueGetter=None,
        type=None,
        unSortIcon=None,
        valueFormatter=None,
        valueGetter=None,
        valueParser=None,
        valueSetter=None,
        width=None,
        wrapHeaderText=None,
        wrapText=None,
        componentDidMount=None,
        componentWillUnmount=None,
        controller=None,
    ):
        super().__init__(key, controller, componentDidMount, componentWillUnmount)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.aggFunc = aggFunc
        self.allowedAggFuncs = allowedAggFuncs
        self.autoHeaderHeight = autoHeaderHeight
        self.autoHeight = autoHeight
        self.cellClass = cellClass
        self.cellClassRules = cellClassRules
        self.cellEditor = cellEditor
        self.cellEditorParams = cellEditorParams
        self.cellEditorPopup = cellEditorPopup
        self.cellEditorPopupPosition = cellEditorPopupPosition
        self.cellEditorSelector = cellEditorSelector
        self.cellRenderer = cellRenderer
        self.cellRendererParams = cellRendererParams
        self.cellRendererSelector = cellRendererSelector
        self.cellStyle = cellStyle
        self.chartDataType = chartDataType
        self.checkboxSelection = checkboxSelection
        self.colId = colId
        self.colSpan = colSpan
        self.columnGroupShow = columnGroupShow
        self.columnsMenuParams = columnsMenuParams
        self.comparator = comparator
        self.defaultAggFunc = defaultAggFunc
        self.dndSource = dndSource
        self.dndSourceOnRowDrag = dndSourceOnRowDrag
        self.editable = editable
        self.enableCellChangeFlash = enableCellChangeFlash
        self.enablePivot = enablePivot
        self.enableRowGroup = enableRowGroup
        self.enableValue = enableValue
        self.equals = equals
        self.field = field
        self.filter = filter
        self.filterParams = filterParams
        self.filterValueGetter = filterValueGetter
        self.flex = flex
        self.floatingFilter = floatingFilter
        self.floatingFilterComponent = floatingFilterComponent
        self.floatingFilterComponentParams = floatingFilterComponentParams
        self.getQuickFilterText = getQuickFilterText
        self.groupId = groupId
        self.headerCheckboxSelection = headerCheckboxSelection
        self.headerCheckboxSelectionFilteredOnly = headerCheckboxSelectionFilteredOnly
        self.headerClass = headerClass
        self.headerComponent = headerComponent
        self.headerComponentParams = headerComponentParams
        self.headerGroupComponent = headerGroupComponent
        self.headerGroupComponentParams = headerGroupComponentParams
        self.headerName = headerName
        self.headerTooltip = headerTooltip
        self.headerValueGetter = headerValueGetter
        self.hide = hide
        self.icons = icons
        self.initialAggFunc = initialAggFunc
        self.initialFlex = initialFlex
        self.initialHide = initialHide
        self.initialPinned = initialPinned
        self.initialPivot = initialPivot
        self.initialPivotIndex = initialPivotIndex
        self.initialRowGroup = initialRowGroup
        self.initialRowGroupIndex = initialRowGroupIndex
        self.initialSort = initialSort
        self.initialSortIndex = initialSortIndex
        self.initialWidth = initialWidth
        self.keyCreator = keyCreator
        self.lockPinned = lockPinned
        self.lockPosition = lockPosition
        self.lockVisible = lockVisible
        self.marryChildren = marryChildren
        self.maxWidth = maxWidth
        self.menuTabs = menuTabs
        self.minWidth = minWidth
        self.onCellClicked = create_callback(
            onCellClicked,
            "onCellClicked",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onCellContextMenu = create_callback(
            onCellContextMenu,
            "onCellContextMenu",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onCellDoubleClicked = create_callback(
            onCellDoubleClicked,
            "onCellDoubleClicked",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onCellValueChanged = create_callback(
            onCellValueChanged,
            "onCellValueChanged",
            [[0, "node", "data", "id"], [0, "newValue"]],
        )
        self.openByDefault = openByDefault
        self.pinned = pinned
        self.pivot = pivot
        self.pivotComparator = pivotComparator
        self.pivotIndex = pivotIndex
        self.pivotKeys = pivotKeys
        self.pivotTotalColumnIds = pivotTotalColumnIds
        self.pivotValueColumn = pivotValueColumn
        self.refData = refData
        self.resizable = resizable
        self.rowDrag = rowDrag
        self.rowDragText = rowDragText
        self.rowGroup = rowGroup
        self.rowGroupIndex = rowGroupIndex
        self.rowSpan = rowSpan
        self.showDisabledCheckboxes = showDisabledCheckboxes
        self.showRowGroup = showRowGroup
        self.singleClickEdit = singleClickEdit
        self.sort = sort
        self.sortIndex = sortIndex
        self.sortable = sortable
        self.sortingOrder = sortingOrder
        self.suppressAutoSize = suppressAutoSize
        self.suppressCellFlash = suppressCellFlash
        self.suppressColumnsToolPanel = suppressColumnsToolPanel
        self.suppressFillHandle = suppressFillHandle
        self.suppressFiltersToolPanel = suppressFiltersToolPanel
        self.suppressHeaderKeyboardEvent = suppressHeaderKeyboardEvent
        self.suppressKeyboardEvent = suppressKeyboardEvent
        self.suppressMenu = suppressMenu
        self.suppressMovable = suppressMovable
        self.suppressNavigable = suppressNavigable
        self.suppressPaste = suppressPaste
        self.suppressSizeToFit = suppressSizeToFit
        self.toolPanelClass = toolPanelClass
        self.tooltipComponent = tooltipComponent
        self.tooltipComponentParams = tooltipComponentParams
        self.tooltipField = tooltipField
        self.tooltipValueGetter = tooltipValueGetter
        self.type = type
        self.unSortIcon = unSortIcon
        self.valueFormatter = valueFormatter
        self.valueGetter = valueGetter
        self.valueParser = valueParser
        self.valueSetter = valueSetter
        self.width = width
        self.wrapHeaderText = wrapHeaderText
        self.wrapText = wrapText
