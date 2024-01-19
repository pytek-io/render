from render import Component, create_callback, get_window


class AgGridReact(Component):
    Module = "ag-grid"
    JSXName = "AgGridReact"
    REF_HOOK = "ref"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "asyncTransactionsFlushed",
        "bodyScroll",
        "bodyScrollEnd",
        "cellClicked",
        "cellContextMenu",
        "cellDoubleClicked",
        "cellEditRequest",
        "cellEditingStarted",
        "cellEditingStopped",
        "cellFocused",
        "cellKeyDown",
        "cellKeyPress",
        "cellMouseDown",
        "cellMouseOut",
        "cellMouseOver",
        "cellValueChanged",
        "chartCreated",
        "chartDestroyed",
        "chartOptionsChanged",
        "chartRangeSelectionChanged",
        "columnAggFuncChangeRequest",
        "columnEverythingChanged",
        "columnGroupOpened",
        "columnMoved",
        "columnPinned",
        "columnPivotChangeRequest",
        "columnPivotChanged",
        "columnPivotModeChanged",
        "columnResized",
        "columnRowGroupChangeRequest",
        "columnRowGroupChanged",
        "columnValueChangeRequest",
        "columnValueChanged",
        "columnVisible",
        "componentStateChanged",
        "displayedColumnsChanged",
        "dragStarted",
        "dragStopped",
        "expandOrCollapseAll",
        "filterChanged",
        "filterModified",
        "filterOpened",
        "firstDataRendered",
        "gridColumnsChanged",
        "gridReady",
        "gridSizeChanged",
        "modelUpdated",
        "newColumnsLoaded",
        "onAsyncTransactionsFlushed",
        "onBodyScroll",
        "onBodyScrollEnd",
        "onCellClicked",
        "onCellContextMenu",
        "onCellDoubleClicked",
        "onCellEditRequest",
        "onCellEditingStarted",
        "onCellEditingStopped",
        "onCellFocused",
        "onCellKeyDown",
        "onCellKeyPress",
        "onCellMouseDown",
        "onCellMouseOut",
        "onCellMouseOver",
        "onCellValueChanged",
        "onChartCreated",
        "onChartDestroyed",
        "onChartOptionsChanged",
        "onChartRangeSelectionChanged",
        "onColumnAggFuncChangeRequest",
        "onColumnEverythingChanged",
        "onColumnGroupOpened",
        "onColumnMoved",
        "onColumnPinned",
        "onColumnPivotChangeRequest",
        "onColumnPivotChanged",
        "onColumnPivotModeChanged",
        "onColumnResized",
        "onColumnRowGroupChangeRequest",
        "onColumnRowGroupChanged",
        "onColumnValueChangeRequest",
        "onColumnValueChanged",
        "onColumnVisible",
        "onComponentStateChanged",
        "onDisplayedColumnsChanged",
        "onDragStarted",
        "onDragStopped",
        "onExpandOrCollapseAll",
        "onFilterChanged",
        "onFilterModified",
        "onFilterOpened",
        "onFirstDataRendered",
        "onGridColumnsChanged",
        "onGridReady",
        "onGridSizeChanged",
        "onModelUpdated",
        "onNewColumnsLoaded",
        "onPaginationChanged",
        "onPasteEnd",
        "onPasteStart",
        "onPinnedRowDataChanged",
        "onRangeSelectionChanged",
        "onRowClicked",
        "onRowDataUpdated",
        "onRowDoubleClicked",
        "onRowDragEnd",
        "onRowDragEnter",
        "onRowDragLeave",
        "onRowDragMove",
        "onRowEditingStarted",
        "onRowEditingStopped",
        "onRowGroupOpened",
        "onRowSelected",
        "onRowValueChanged",
        "onSelectionChanged",
        "onSortChanged",
        "onToolPanelVisibleChanged",
        "onViewportChanged",
        "onVirtualColumnsChanged",
        "onVirtualRowRemoved",
        "paginationChanged",
        "pasteEnd",
        "pasteStart",
        "pinnedRowDataChanged",
        "rangeSelectionChanged",
        "rowClicked",
        "rowDataUpdated",
        "rowDoubleClicked",
        "rowDragEnd",
        "rowDragEnter",
        "rowDragLeave",
        "rowDragMove",
        "rowEditingStarted",
        "rowEditingStopped",
        "rowGroupOpened",
        "rowSelected",
        "rowValueChanged",
        "selectionChanged",
        "sortChanged",
        "toolPanelVisibleChanged",
        "viewportChanged",
        "virtualColumnsChanged",
        "virtualRowRemoved",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "accentedSort",
        "aggFuncs",
        "aggregateOnlyChangedColumns",
        "alignedGrids",
        "allowContextMenuWithControlKey",
        "allowDragFromColumnsToolPanel",
        "allowShowChangeAfterFilter",
        "alwaysMultiSort",
        "alwaysShowHorizontalScroll",
        "alwaysShowVerticalScroll",
        "angularCompileFilters",
        "angularCompileRows",
        "animateRows",
        "api",
        "asyncTransactionWaitMillis",
        "autoGroupColumnDef",
        "autoSizePadding",
        "blockLoadDebounceMillis",
        "cacheBlockSize",
        "cacheOverflowSize",
        "cacheQuickFilter",
        "cellFadeDelay",
        "cellFlashDelay",
        "chartThemeOverrides",
        "chartThemes",
        "clipboardDelimiter",
        "colResizeDefault",
        "columnApi",
        "columnDefs",
        "columnHoverHighlight",
        "columnTypes",
        "components",
        "context",
        "copyGroupHeadersToClipboard",
        "copyHeadersToClipboard",
        "createChartContainer",
        "customChartThemes",
        "datasource",
        "debounceVerticalScrollbar",
        "debug",
        "defaultColDef",
        "defaultColGroupDef",
        "defaultCsvExportParams",
        "defaultExcelExportParams",
        "deltaSort",
        "detailCellRenderer",
        "detailCellRendererParams",
        "detailRowAutoHeight",
        "detailRowHeight",
        "doesExternalFilterPass",
        "domLayout",
        "editType",
        "embedFullWidthRows",
        "enableBrowserTooltips",
        "enableCellChangeFlash",
        "enableCellExpressions",
        "enableCellTextSelection",
        "enableCharts",
        "enableFillHandle",
        "enableGroupEdit",
        "enableRangeHandle",
        "enableRangeSelection",
        "enableRtl",
        "ensureDomOrder",
        "enterMovesDown",
        "enterMovesDownAfterEdit",
        "excelStyles",
        "excludeChildrenWhenTreeDataFiltering",
        "fillHandleDirection",
        "fillOperation",
        "floatingFiltersHeight",
        "fullWidthCellRenderer",
        "fullWidthCellRendererParams",
        "functionsPassive",
        "functionsReadOnly",
        "getBusinessKeyForNode",
        "getChartToolbarItems",
        "getChildCount",
        "getContextMenuItems",
        "getDataPath",
        "getDocument",
        "getGroupRowAgg",
        "getLocaleText",
        "getMainMenuItems",
        "getRowClass",
        "getRowHeight",
        "getRowId",
        "getRowStyle",
        "getServerSideGroupKey",
        "getServerSideGroupLevelParams",
        "groupAggFiltering",
        "groupDefaultExpanded",
        "groupDisplayType",
        "groupHeaderHeight",
        "groupHideOpenParents",
        "groupIncludeFooter",
        "groupIncludeTotalFooter",
        "groupMaintainOrder",
        "groupRemoveLowestSingleChildren",
        "groupRemoveSingleChildren",
        "groupRowRenderer",
        "groupRowRendererParams",
        "groupRowsSticky",
        "groupSelectsChildren",
        "groupSelectsFiltered",
        "groupSuppressBlankHeader",
        "headerHeight",
        "icons",
        "infiniteInitialRowCount",
        "initialGroupOrderComparator",
        "isApplyServerSideTransaction",
        "isExternalFilterPresent",
        "isFullWidthRow",
        "isGroupOpenByDefault",
        "isRowMaster",
        "isRowSelectable",
        "isServerSideGroup",
        "isServerSideGroupOpenByDefault",
        "keepDetailRows",
        "keepDetailRowsCount",
        "loadingCellRenderer",
        "loadingCellRendererParams",
        "loadingCellRendererSelector",
        "loadingOverlayComponent",
        "loadingOverlayComponentParams",
        "localeText",
        "maintainColumnOrder",
        "masterDetail",
        "maxBlocksInCache",
        "maxConcurrentDatasourceRequests",
        "multiSortKey",
        "navigateToNextCell",
        "navigateToNextHeader",
        "noRowsOverlayComponent",
        "noRowsOverlayComponentParams",
        "overlayLoadingTemplate",
        "overlayNoRowsTemplate",
        "paginateChildRows",
        "pagination",
        "paginationAutoPageSize",
        "paginationNumberFormatter",
        "paginationPageSize",
        "pinnedBottomRowData",
        "pinnedTopRowData",
        "pivotColumnGroupTotals",
        "pivotGroupHeaderHeight",
        "pivotHeaderHeight",
        "pivotMode",
        "pivotPanelShow",
        "pivotRowTotals",
        "pivotSuppressAutoColumn",
        "popupParent",
        "postProcessPopup",
        "postSortRows",
        "preventDefaultOnContextMenu",
        "processCellForClipboard",
        "processCellFromClipboard",
        "processDataFromClipboard",
        "processGroupHeaderForClipboard",
        "processHeaderForClipboard",
        "processPivotResultColDef",
        "processPivotResultColGroupDef",
        "processRowPostCreate",
        "purgeClosedRowNodes",
        "quickFilterText",
        "readOnlyEdit",
        "removePivotHeaderRowWhenSingleValueColumn",
        "resetRowDataOnUpdate",
        "rowBuffer",
        "rowClass",
        "rowClassRules",
        "rowData",
        "rowDragEntireRow",
        "rowDragManaged",
        "rowDragMultiRow",
        "rowGroupPanelShow",
        "rowHeight",
        "rowModelType",
        "rowMultiSelectWithClick",
        "rowSelection",
        "rowStyle",
        "scrollbarWidth",
        "sendToClipboard",
        "serverSideDatasource",
        "serverSideFilterAllLevels",
        "serverSideFilterOnServer",
        "serverSideInfiniteScroll",
        "serverSideInitialRowCount",
        "serverSideSortAllLevels",
        "serverSideSortOnServer",
        "showOpenedGroup",
        "sideBar",
        "singleClickEdit",
        "skipHeaderOnAutoSize",
        "sortingOrder",
        "statusBar",
        "stopEditingWhenCellsLoseFocus",
        "suppressAggAtRootLevel",
        "suppressAggFilteredOnly",
        "suppressAggFuncInHeader",
        "suppressAnimationFrame",
        "suppressAsyncEvents",
        "suppressAutoSize",
        "suppressBrowserResizeObserver",
        "suppressCellFocus",
        "suppressChangeDetection",
        "suppressClearOnFillReduction",
        "suppressClickEdit",
        "suppressClipboardApi",
        "suppressClipboardPaste",
        "suppressColumnMoveAnimation",
        "suppressColumnVirtualisation",
        "suppressContextMenu",
        "suppressCopyRowsToClipboard",
        "suppressCopySingleCellRanges",
        "suppressCsvExport",
        "suppressDragLeaveHidesColumns",
        "suppressExcelExport",
        "suppressExpandablePivotGroups",
        "suppressFieldDotNotation",
        "suppressFocusAfterRefresh",
        "suppressHorizontalScroll",
        "suppressLastEmptyLineOnPaste",
        "suppressLoadingOverlay",
        "suppressMaintainUnsortedOrder",
        "suppressMakeColumnVisibleAfterUnGroup",
        "suppressMaxRenderedRowRestriction",
        "suppressMenuHide",
        "suppressMiddleClickScrolls",
        "suppressModelUpdateAfterUpdateTransaction",
        "suppressMovableColumns",
        "suppressMoveWhenRowDragging",
        "suppressMultiRangeSelection",
        "suppressMultiSort",
        "suppressNoRowsOverlay",
        "suppressPaginationPanel",
        "suppressParentsInRowNodes",
        "suppressPreventDefaultOnMouseWheel",
        "suppressPropertyNamesCheck",
        "suppressRowClickSelection",
        "suppressRowDeselection",
        "suppressRowDrag",
        "suppressRowGroupHidesColumns",
        "suppressRowHoverHighlight",
        "suppressRowTransform",
        "suppressRowVirtualisation",
        "suppressScrollOnNewData",
        "suppressScrollWhenPopupsAreOpen",
        "suppressTouch",
        "tabIndex",
        "tabToNextCell",
        "tabToNextHeader",
        "tooltipHideDelay",
        "tooltipMouseTrack",
        "tooltipShowDelay",
        "treeData",
        "treeDataDisplayType",
        "unSortIcon",
        "undoRedoCellEditing",
        "undoRedoCellEditingLimit",
        "valueCache",
        "valueCacheNeverExpires",
        "viewportDatasource",
        "viewportRowModelBufferSize",
        "viewportRowModelPageSize",
    ]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className="ag-theme-balham",
        id=None,
        onKeyPress=None,
        onClick=None,
        accentedSort=None,
        aggFuncs=None,
        aggregateOnlyChangedColumns=None,
        alignedGrids=None,
        allowContextMenuWithControlKey=None,
        allowDragFromColumnsToolPanel=None,
        allowShowChangeAfterFilter=None,
        alwaysMultiSort=None,
        alwaysShowHorizontalScroll=None,
        alwaysShowVerticalScroll=None,
        angularCompileFilters=None,
        angularCompileRows=None,
        animateRows=None,
        api=None,
        asyncTransactionWaitMillis=None,
        asyncTransactionsFlushed=None,
        autoGroupColumnDef=None,
        autoSizePadding=None,
        blockLoadDebounceMillis=None,
        bodyScroll=None,
        bodyScrollEnd=None,
        cacheBlockSize=None,
        cacheOverflowSize=None,
        cacheQuickFilter=None,
        cellClicked=None,
        cellContextMenu=None,
        cellDoubleClicked=None,
        cellEditRequest=None,
        cellEditingStarted=None,
        cellEditingStopped=None,
        cellFadeDelay=None,
        cellFlashDelay=None,
        cellFocused=None,
        cellKeyDown=None,
        cellKeyPress=None,
        cellMouseDown=None,
        cellMouseOut=None,
        cellMouseOver=None,
        cellValueChanged=None,
        chartCreated=None,
        chartDestroyed=None,
        chartOptionsChanged=None,
        chartRangeSelectionChanged=None,
        chartThemeOverrides=None,
        chartThemes=None,
        clipboardDelimiter=None,
        colResizeDefault=None,
        columnAggFuncChangeRequest=None,
        columnApi=None,
        columnDefs=None,
        columnEverythingChanged=None,
        columnGroupOpened=None,
        columnHoverHighlight=None,
        columnMoved=None,
        columnPinned=None,
        columnPivotChangeRequest=None,
        columnPivotChanged=None,
        columnPivotModeChanged=None,
        columnResized=None,
        columnRowGroupChangeRequest=None,
        columnRowGroupChanged=None,
        columnTypes=None,
        columnValueChangeRequest=None,
        columnValueChanged=None,
        columnVisible=None,
        componentStateChanged=None,
        components=None,
        context=None,
        copyGroupHeadersToClipboard=None,
        copyHeadersToClipboard=None,
        createChartContainer=None,
        customChartThemes=None,
        datasource=None,
        debounceVerticalScrollbar=None,
        debug=None,
        defaultColDef=None,
        defaultColGroupDef=None,
        defaultCsvExportParams=None,
        defaultExcelExportParams=None,
        deltaSort=None,
        detailCellRenderer=None,
        detailCellRendererParams=None,
        detailRowAutoHeight=None,
        detailRowHeight=None,
        displayedColumnsChanged=None,
        doesExternalFilterPass=None,
        domLayout=None,
        dragStarted=None,
        dragStopped=None,
        editType=None,
        embedFullWidthRows=None,
        enableBrowserTooltips=None,
        enableCellChangeFlash=None,
        enableCellExpressions=None,
        enableCellTextSelection=None,
        enableCharts=None,
        enableFillHandle=None,
        enableGroupEdit=None,
        enableRangeHandle=None,
        enableRangeSelection=None,
        enableRtl=None,
        ensureDomOrder=None,
        enterMovesDown=None,
        enterMovesDownAfterEdit=None,
        excelStyles=None,
        excludeChildrenWhenTreeDataFiltering=None,
        expandOrCollapseAll=None,
        fillHandleDirection=None,
        fillOperation=None,
        filterChanged=None,
        filterModified=None,
        filterOpened=None,
        firstDataRendered=None,
        floatingFiltersHeight=None,
        fullWidthCellRenderer=None,
        fullWidthCellRendererParams=None,
        functionsPassive=None,
        functionsReadOnly=None,
        getBusinessKeyForNode=None,
        getChartToolbarItems=None,
        getChildCount=None,
        getContextMenuItems=None,
        getDataPath=None,
        getDocument=None,
        getGroupRowAgg=None,
        getLocaleText=None,
        getMainMenuItems=None,
        getRowClass=None,
        getRowHeight=None,
        getRowId=None,
        getRowStyle=None,
        getServerSideGroupKey=None,
        getServerSideGroupLevelParams=None,
        gridColumnsChanged=None,
        gridReady=None,
        gridSizeChanged=None,
        groupAggFiltering=None,
        groupDefaultExpanded=None,
        groupDisplayType=None,
        groupHeaderHeight=None,
        groupHideOpenParents=None,
        groupIncludeFooter=None,
        groupIncludeTotalFooter=None,
        groupMaintainOrder=None,
        groupRemoveLowestSingleChildren=None,
        groupRemoveSingleChildren=None,
        groupRowRenderer=None,
        groupRowRendererParams=None,
        groupRowsSticky=None,
        groupSelectsChildren=None,
        groupSelectsFiltered=None,
        groupSuppressBlankHeader=None,
        headerHeight=None,
        icons=None,
        infiniteInitialRowCount=None,
        initialGroupOrderComparator=None,
        isApplyServerSideTransaction=None,
        isExternalFilterPresent=None,
        isFullWidthRow=None,
        isGroupOpenByDefault=None,
        isRowMaster=None,
        isRowSelectable=None,
        isServerSideGroup=None,
        isServerSideGroupOpenByDefault=None,
        keepDetailRows=None,
        keepDetailRowsCount=None,
        loadingCellRenderer=None,
        loadingCellRendererParams=None,
        loadingCellRendererSelector=None,
        loadingOverlayComponent=None,
        loadingOverlayComponentParams=None,
        localeText=None,
        maintainColumnOrder=None,
        masterDetail=None,
        maxBlocksInCache=None,
        maxConcurrentDatasourceRequests=None,
        modelUpdated=None,
        multiSortKey=None,
        navigateToNextCell=None,
        navigateToNextHeader=None,
        newColumnsLoaded=None,
        noRowsOverlayComponent=None,
        noRowsOverlayComponentParams=None,
        onAsyncTransactionsFlushed=None,
        onBodyScroll=None,
        onBodyScrollEnd=None,
        onCellClicked=None,
        onCellContextMenu=None,
        onCellDoubleClicked=None,
        onCellEditRequest=None,
        onCellEditingStarted=None,
        onCellEditingStopped=None,
        onCellFocused=None,
        onCellKeyDown=None,
        onCellKeyPress=None,
        onCellMouseDown=None,
        onCellMouseOut=None,
        onCellMouseOver=None,
        onCellValueChanged=None,
        onChartCreated=None,
        onChartDestroyed=None,
        onChartOptionsChanged=None,
        onChartRangeSelectionChanged=None,
        onColumnAggFuncChangeRequest=None,
        onColumnEverythingChanged=None,
        onColumnGroupOpened=None,
        onColumnMoved=None,
        onColumnPinned=None,
        onColumnPivotChangeRequest=None,
        onColumnPivotChanged=None,
        onColumnPivotModeChanged=None,
        onColumnResized=None,
        onColumnRowGroupChangeRequest=None,
        onColumnRowGroupChanged=None,
        onColumnValueChangeRequest=None,
        onColumnValueChanged=None,
        onColumnVisible=None,
        onComponentStateChanged=None,
        onDisplayedColumnsChanged=None,
        onDragStarted=None,
        onDragStopped=None,
        onExpandOrCollapseAll=None,
        onFilterChanged=None,
        onFilterModified=None,
        onFilterOpened=None,
        onFirstDataRendered=None,
        onGridColumnsChanged=None,
        onGridReady=None,
        onGridSizeChanged=None,
        onModelUpdated=None,
        onNewColumnsLoaded=None,
        onPaginationChanged=None,
        onPasteEnd=None,
        onPasteStart=None,
        onPinnedRowDataChanged=None,
        onRangeSelectionChanged=None,
        onRowClicked=None,
        onRowDataUpdated=None,
        onRowDoubleClicked=None,
        onRowDragEnd=None,
        onRowDragEnter=None,
        onRowDragLeave=None,
        onRowDragMove=None,
        onRowEditingStarted=None,
        onRowEditingStopped=None,
        onRowGroupOpened=None,
        onRowSelected=None,
        onRowValueChanged=None,
        onSelectionChanged=None,
        onSortChanged=None,
        onToolPanelVisibleChanged=None,
        onViewportChanged=None,
        onVirtualColumnsChanged=None,
        onVirtualRowRemoved=None,
        overlayLoadingTemplate=None,
        overlayNoRowsTemplate=None,
        paginateChildRows=None,
        pagination=None,
        paginationAutoPageSize=None,
        paginationChanged=None,
        paginationNumberFormatter=None,
        paginationPageSize=None,
        pasteEnd=None,
        pasteStart=None,
        pinnedBottomRowData=None,
        pinnedRowDataChanged=None,
        pinnedTopRowData=None,
        pivotColumnGroupTotals=None,
        pivotGroupHeaderHeight=None,
        pivotHeaderHeight=None,
        pivotMode=None,
        pivotPanelShow=None,
        pivotRowTotals=None,
        pivotSuppressAutoColumn=None,
        popupParent=None,
        postProcessPopup=None,
        postSortRows=None,
        preventDefaultOnContextMenu=None,
        processCellForClipboard=None,
        processCellFromClipboard=None,
        processDataFromClipboard=None,
        processGroupHeaderForClipboard=None,
        processHeaderForClipboard=None,
        processPivotResultColDef=None,
        processPivotResultColGroupDef=None,
        processRowPostCreate=None,
        purgeClosedRowNodes=None,
        quickFilterText=None,
        rangeSelectionChanged=None,
        readOnlyEdit=None,
        removePivotHeaderRowWhenSingleValueColumn=None,
        resetRowDataOnUpdate=None,
        rowBuffer=None,
        rowClass=None,
        rowClassRules=None,
        rowClicked=None,
        rowData=None,
        rowDataUpdated=None,
        rowDoubleClicked=None,
        rowDragEnd=None,
        rowDragEnter=None,
        rowDragEntireRow=None,
        rowDragLeave=None,
        rowDragManaged=None,
        rowDragMove=None,
        rowDragMultiRow=None,
        rowEditingStarted=None,
        rowEditingStopped=None,
        rowGroupOpened=None,
        rowGroupPanelShow=None,
        rowHeight=None,
        rowModelType=None,
        rowMultiSelectWithClick=None,
        rowSelected=None,
        rowSelection=None,
        rowStyle=None,
        rowValueChanged=None,
        scrollbarWidth=None,
        selectionChanged=None,
        sendToClipboard=None,
        serverSideDatasource=None,
        serverSideFilterAllLevels=None,
        serverSideFilterOnServer=None,
        serverSideInfiniteScroll=None,
        serverSideInitialRowCount=None,
        serverSideSortAllLevels=None,
        serverSideSortOnServer=None,
        showOpenedGroup=None,
        sideBar=None,
        singleClickEdit=None,
        skipHeaderOnAutoSize=None,
        sortChanged=None,
        sortingOrder=None,
        statusBar=None,
        stopEditingWhenCellsLoseFocus=None,
        suppressAggAtRootLevel=None,
        suppressAggFilteredOnly=None,
        suppressAggFuncInHeader=None,
        suppressAnimationFrame=None,
        suppressAsyncEvents=None,
        suppressAutoSize=None,
        suppressBrowserResizeObserver=None,
        suppressCellFocus=None,
        suppressChangeDetection=None,
        suppressClearOnFillReduction=None,
        suppressClickEdit=None,
        suppressClipboardApi=None,
        suppressClipboardPaste=None,
        suppressColumnMoveAnimation=None,
        suppressColumnVirtualisation=None,
        suppressContextMenu=None,
        suppressCopyRowsToClipboard=None,
        suppressCopySingleCellRanges=None,
        suppressCsvExport=None,
        suppressDragLeaveHidesColumns=None,
        suppressExcelExport=None,
        suppressExpandablePivotGroups=None,
        suppressFieldDotNotation=None,
        suppressFocusAfterRefresh=None,
        suppressHorizontalScroll=None,
        suppressLastEmptyLineOnPaste=None,
        suppressLoadingOverlay=None,
        suppressMaintainUnsortedOrder=None,
        suppressMakeColumnVisibleAfterUnGroup=None,
        suppressMaxRenderedRowRestriction=None,
        suppressMenuHide=None,
        suppressMiddleClickScrolls=None,
        suppressModelUpdateAfterUpdateTransaction=None,
        suppressMovableColumns=None,
        suppressMoveWhenRowDragging=None,
        suppressMultiRangeSelection=None,
        suppressMultiSort=None,
        suppressNoRowsOverlay=None,
        suppressPaginationPanel=None,
        suppressParentsInRowNodes=None,
        suppressPreventDefaultOnMouseWheel=None,
        suppressPropertyNamesCheck=None,
        suppressRowClickSelection=None,
        suppressRowDeselection=None,
        suppressRowDrag=None,
        suppressRowGroupHidesColumns=None,
        suppressRowHoverHighlight=None,
        suppressRowTransform=None,
        suppressRowVirtualisation=None,
        suppressScrollOnNewData=None,
        suppressScrollWhenPopupsAreOpen=None,
        suppressTouch=None,
        tabIndex=None,
        tabToNextCell=None,
        tabToNextHeader=None,
        toolPanelVisibleChanged=None,
        tooltipHideDelay=None,
        tooltipMouseTrack=None,
        tooltipShowDelay=None,
        treeData=None,
        treeDataDisplayType=None,
        unSortIcon=None,
        undoRedoCellEditing=None,
        undoRedoCellEditingLimit=None,
        valueCache=None,
        valueCacheNeverExpires=None,
        viewportChanged=None,
        viewportDatasource=None,
        viewportRowModelBufferSize=None,
        viewportRowModelPageSize=None,
        virtualColumnsChanged=None,
        virtualRowRemoved=None,
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
        self.accentedSort = accentedSort
        self.aggFuncs = aggFuncs
        self.aggregateOnlyChangedColumns = aggregateOnlyChangedColumns
        self.alignedGrids = alignedGrids
        self.allowContextMenuWithControlKey = allowContextMenuWithControlKey
        self.allowDragFromColumnsToolPanel = allowDragFromColumnsToolPanel
        self.allowShowChangeAfterFilter = allowShowChangeAfterFilter
        self.alwaysMultiSort = alwaysMultiSort
        self.alwaysShowHorizontalScroll = alwaysShowHorizontalScroll
        self.alwaysShowVerticalScroll = alwaysShowVerticalScroll
        self.angularCompileFilters = angularCompileFilters
        self.angularCompileRows = angularCompileRows
        self.animateRows = animateRows
        self.api = api
        self.asyncTransactionWaitMillis = asyncTransactionWaitMillis
        self.asyncTransactionsFlushed = create_callback(
            asyncTransactionsFlushed, "asyncTransactionsFlushed", [[0, "type"]]
        )
        self.autoGroupColumnDef = autoGroupColumnDef
        self.autoSizePadding = autoSizePadding
        self.blockLoadDebounceMillis = blockLoadDebounceMillis
        self.bodyScroll = create_callback(
            bodyScroll,
            "bodyScroll",
            [[0, "top"], [0, "direction"], [0, "left"], [0, "type"]],
        )
        self.bodyScrollEnd = create_callback(
            bodyScrollEnd,
            "bodyScrollEnd",
            [[0, "top"], [0, "direction"], [0, "left"], [0, "type"]],
        )
        self.cacheBlockSize = cacheBlockSize
        self.cacheOverflowSize = cacheOverflowSize
        self.cacheQuickFilter = cacheQuickFilter
        self.cellClicked = create_callback(
            cellClicked,
            "cellClicked",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellContextMenu = create_callback(
            cellContextMenu,
            "cellContextMenu",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellDoubleClicked = create_callback(
            cellDoubleClicked,
            "cellDoubleClicked",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellEditRequest = create_callback(
            cellEditRequest,
            "cellEditRequest",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "source"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "newValue"],
                [0, "column", "header"],
            ],
        )
        self.cellEditingStarted = create_callback(
            cellEditingStarted,
            "cellEditingStarted",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellEditingStopped = create_callback(
            cellEditingStopped,
            "cellEditingStopped",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "newValue"],
                [0, "column", "header"],
            ],
        )
        self.cellFadeDelay = cellFadeDelay
        self.cellFlashDelay = cellFlashDelay
        self.cellFocused = create_callback(
            cellFocused,
            "cellFocused",
            [
                [0, "rowPinned"],
                [0, "isFullWidthCell"],
                [0, "preventScrollOnBrowserFocus"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "forceBrowserFocus"],
                [0, "floating"],
            ],
        )
        self.cellKeyDown = create_callback(
            cellKeyDown,
            "cellKeyDown",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellKeyPress = create_callback(
            cellKeyPress,
            "cellKeyPress",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellMouseDown = create_callback(
            cellMouseDown,
            "cellMouseDown",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellMouseOut = create_callback(
            cellMouseOut,
            "cellMouseOut",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellMouseOver = create_callback(
            cellMouseOver,
            "cellMouseOver",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.cellValueChanged = create_callback(
            cellValueChanged,
            "cellValueChanged",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "source"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "newValue"],
                [0, "column", "header"],
            ],
        )
        self.chartCreated = create_callback(
            chartCreated, "chartCreated", [[0, "chartId"], [0, "type"]]
        )
        self.chartDestroyed = create_callback(
            chartDestroyed, "chartDestroyed", [[0, "chartId"], [0, "type"]]
        )
        self.chartOptionsChanged = create_callback(
            chartOptionsChanged,
            "chartOptionsChanged",
            [[0, "chartType"], [0, "chartThemeName"], [0, "chartId"], [0, "type"]],
        )
        self.chartRangeSelectionChanged = create_callback(
            chartRangeSelectionChanged,
            "chartRangeSelectionChanged",
            [[0, "id"], [0, "chartId"], [0, "type"]],
        )
        self.chartThemeOverrides = chartThemeOverrides
        self.chartThemes = chartThemes
        self.clipboardDelimiter = clipboardDelimiter
        self.colResizeDefault = colResizeDefault
        self.columnAggFuncChangeRequest = create_callback(
            columnAggFuncChangeRequest,
            "columnAggFuncChangeRequest",
            [[0, "aggFunc"], [0, "[]", "columns", "header"], [0, "type"]],
        )
        self.columnApi = columnApi
        self.columnDefs = columnDefs
        self.columnEverythingChanged = create_callback(
            columnEverythingChanged,
            "columnEverythingChanged",
            [[0, "source"], [0, "type"]],
        )
        self.columnGroupOpened = create_callback(
            columnGroupOpened,
            "columnGroupOpened",
            [[0, "columnGroup", "header"], [0, "type"]],
        )
        self.columnHoverHighlight = columnHoverHighlight
        self.columnMoved = create_callback(
            columnMoved,
            "columnMoved",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "toIndex"],
                [0, "type"],
                [0, "column", "header"],
            ],
        )
        self.columnPinned = create_callback(
            columnPinned,
            "columnPinned",
            [
                [0, "pinned"],
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "type"],
                [0, "column", "header"],
            ],
        )
        self.columnPivotChangeRequest = create_callback(
            columnPivotChangeRequest,
            "columnPivotChangeRequest",
            [[0, "[]", "columns", "header"], [0, "type"]],
        )
        self.columnPivotChanged = create_callback(
            columnPivotChanged,
            "columnPivotChanged",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "column", "header"],
                [0, "type"],
            ],
        )
        self.columnPivotModeChanged = create_callback(
            columnPivotModeChanged, "columnPivotModeChanged", [[0, "type"]]
        )
        self.columnResized = create_callback(
            columnResized,
            "columnResized",
            [
                [0, "[]", "columns", "header"],
                [0, "[]", "flexColumns", "header"],
                [0, "source"],
                [0, "type"],
                [0, "finished"],
                [0, "column", "header"],
            ],
        )
        self.columnRowGroupChangeRequest = create_callback(
            columnRowGroupChangeRequest,
            "columnRowGroupChangeRequest",
            [[0, "[]", "columns", "header"], [0, "type"]],
        )
        self.columnRowGroupChanged = create_callback(
            columnRowGroupChanged,
            "columnRowGroupChanged",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "column", "header"],
                [0, "type"],
            ],
        )
        self.columnTypes = columnTypes
        self.columnValueChangeRequest = create_callback(
            columnValueChangeRequest,
            "columnValueChangeRequest",
            [[0, "[]", "columns", "header"], [0, "type"]],
        )
        self.columnValueChanged = create_callback(
            columnValueChanged,
            "columnValueChanged",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "column", "header"],
                [0, "type"],
            ],
        )
        self.columnVisible = create_callback(
            columnVisible,
            "columnVisible",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "visible"],
                [0, "type"],
                [0, "column", "header"],
            ],
        )
        self.componentStateChanged = create_callback(
            componentStateChanged, "componentStateChanged", [[0, "type"]]
        )
        self.components = components
        self.context = context
        self.copyGroupHeadersToClipboard = copyGroupHeadersToClipboard
        self.copyHeadersToClipboard = copyHeadersToClipboard
        self.createChartContainer = createChartContainer
        self.customChartThemes = customChartThemes
        self.datasource = datasource
        self.debounceVerticalScrollbar = debounceVerticalScrollbar
        self.debug = debug
        self.defaultColDef = defaultColDef
        self.defaultColGroupDef = defaultColGroupDef
        self.defaultCsvExportParams = defaultCsvExportParams
        self.defaultExcelExportParams = defaultExcelExportParams
        self.deltaSort = deltaSort
        self.detailCellRenderer = detailCellRenderer
        self.detailCellRendererParams = detailCellRendererParams
        self.detailRowAutoHeight = detailRowAutoHeight
        self.detailRowHeight = detailRowHeight
        self.displayedColumnsChanged = create_callback(
            displayedColumnsChanged, "displayedColumnsChanged", [[0, "type"]]
        )
        self.doesExternalFilterPass = doesExternalFilterPass
        self.domLayout = domLayout
        self.dragStarted = create_callback(dragStarted, "dragStarted", [[0, "type"]])
        self.dragStopped = create_callback(dragStopped, "dragStopped", [[0, "type"]])
        self.editType = editType
        self.embedFullWidthRows = embedFullWidthRows
        self.enableBrowserTooltips = enableBrowserTooltips
        self.enableCellChangeFlash = enableCellChangeFlash
        self.enableCellExpressions = enableCellExpressions
        self.enableCellTextSelection = enableCellTextSelection
        self.enableCharts = enableCharts
        self.enableFillHandle = enableFillHandle
        self.enableGroupEdit = enableGroupEdit
        self.enableRangeHandle = enableRangeHandle
        self.enableRangeSelection = enableRangeSelection
        self.enableRtl = enableRtl
        self.ensureDomOrder = ensureDomOrder
        self.enterMovesDown = enterMovesDown
        self.enterMovesDownAfterEdit = enterMovesDownAfterEdit
        self.excelStyles = excelStyles
        self.excludeChildrenWhenTreeDataFiltering = excludeChildrenWhenTreeDataFiltering
        self.expandOrCollapseAll = create_callback(
            expandOrCollapseAll, "expandOrCollapseAll", [[0, "source"], [0, "type"]]
        )
        self.fillHandleDirection = fillHandleDirection
        self.fillOperation = fillOperation
        self.filterChanged = create_callback(
            filterChanged,
            "filterChanged",
            [
                [0, "afterDataChange"],
                [0, "afterFloatingFilter"],
                [0, "[]", "columns", "header"],
                [0, "type"],
            ],
        )
        self.filterModified = create_callback(
            filterModified, "filterModified", [[0, "column", "header"], [0, "type"]]
        )
        self.filterOpened = create_callback(
            filterOpened, "filterOpened", [[0, "column", "header"], [0, "type"]]
        )
        self.firstDataRendered = create_callback(
            firstDataRendered,
            "firstDataRendered",
            [[0, "lastRow"], [0, "firstRow"], [0, "type"]],
        )
        self.floatingFiltersHeight = floatingFiltersHeight
        self.fullWidthCellRenderer = fullWidthCellRenderer
        self.fullWidthCellRendererParams = fullWidthCellRendererParams
        self.functionsPassive = functionsPassive
        self.functionsReadOnly = functionsReadOnly
        self.getBusinessKeyForNode = getBusinessKeyForNode
        self.getChartToolbarItems = getChartToolbarItems
        self.getChildCount = getChildCount
        self.getContextMenuItems = getContextMenuItems
        self.getDataPath = getDataPath
        self.getDocument = getDocument
        self.getGroupRowAgg = getGroupRowAgg
        self.getLocaleText = getLocaleText
        self.getMainMenuItems = getMainMenuItems
        self.getRowClass = getRowClass
        self.getRowHeight = getRowHeight
        self.getRowId = getRowId
        self.getRowStyle = getRowStyle
        self.getServerSideGroupKey = getServerSideGroupKey
        self.getServerSideGroupLevelParams = getServerSideGroupLevelParams
        self.gridColumnsChanged = create_callback(
            gridColumnsChanged, "gridColumnsChanged", [[0, "type"]]
        )
        self.gridReady = create_callback(gridReady, "gridReady", [[0, "type"]])
        self.gridSizeChanged = create_callback(
            gridSizeChanged,
            "gridSizeChanged",
            [[0, "clientHeight"], [0, "clientWidth"], [0, "type"]],
        )
        self.groupAggFiltering = groupAggFiltering
        self.groupDefaultExpanded = groupDefaultExpanded
        self.groupDisplayType = groupDisplayType
        self.groupHeaderHeight = groupHeaderHeight
        self.groupHideOpenParents = groupHideOpenParents
        self.groupIncludeFooter = groupIncludeFooter
        self.groupIncludeTotalFooter = groupIncludeTotalFooter
        self.groupMaintainOrder = groupMaintainOrder
        self.groupRemoveLowestSingleChildren = groupRemoveLowestSingleChildren
        self.groupRemoveSingleChildren = groupRemoveSingleChildren
        self.groupRowRenderer = groupRowRenderer
        self.groupRowRendererParams = groupRowRendererParams
        self.groupRowsSticky = groupRowsSticky
        self.groupSelectsChildren = groupSelectsChildren
        self.groupSelectsFiltered = groupSelectsFiltered
        self.groupSuppressBlankHeader = groupSuppressBlankHeader
        self.headerHeight = headerHeight
        self.icons = icons
        self.infiniteInitialRowCount = infiniteInitialRowCount
        self.initialGroupOrderComparator = initialGroupOrderComparator
        self.isApplyServerSideTransaction = isApplyServerSideTransaction
        self.isExternalFilterPresent = isExternalFilterPresent
        self.isFullWidthRow = isFullWidthRow
        self.isGroupOpenByDefault = isGroupOpenByDefault
        self.isRowMaster = isRowMaster
        self.isRowSelectable = isRowSelectable
        self.isServerSideGroup = isServerSideGroup
        self.isServerSideGroupOpenByDefault = isServerSideGroupOpenByDefault
        self.keepDetailRows = keepDetailRows
        self.keepDetailRowsCount = keepDetailRowsCount
        self.loadingCellRenderer = loadingCellRenderer
        self.loadingCellRendererParams = loadingCellRendererParams
        self.loadingCellRendererSelector = loadingCellRendererSelector
        self.loadingOverlayComponent = loadingOverlayComponent
        self.loadingOverlayComponentParams = loadingOverlayComponentParams
        self.localeText = localeText
        self.maintainColumnOrder = maintainColumnOrder
        self.masterDetail = masterDetail
        self.maxBlocksInCache = maxBlocksInCache
        self.maxConcurrentDatasourceRequests = maxConcurrentDatasourceRequests
        self.modelUpdated = create_callback(
            modelUpdated,
            "modelUpdated",
            [
                [0, "newData"],
                [0, "animate"],
                [0, "keepRenderedRows"],
                [0, "type"],
                [0, "keepUndoRedoStack"],
                [0, "newPage"],
            ],
        )
        self.multiSortKey = multiSortKey
        self.navigateToNextCell = navigateToNextCell
        self.navigateToNextHeader = navigateToNextHeader
        self.newColumnsLoaded = create_callback(
            newColumnsLoaded, "newColumnsLoaded", [[0, "type"]]
        )
        self.noRowsOverlayComponent = noRowsOverlayComponent
        self.noRowsOverlayComponentParams = noRowsOverlayComponentParams
        self.onAsyncTransactionsFlushed = create_callback(
            onAsyncTransactionsFlushed, "onAsyncTransactionsFlushed", [[0, "type"]]
        )
        self.onBodyScroll = create_callback(
            onBodyScroll,
            "onBodyScroll",
            [[0, "top"], [0, "direction"], [0, "left"], [0, "type"]],
        )
        self.onBodyScrollEnd = create_callback(
            onBodyScrollEnd,
            "onBodyScrollEnd",
            [[0, "top"], [0, "direction"], [0, "left"], [0, "type"]],
        )
        self.onCellClicked = create_callback(
            onCellClicked,
            "onCellClicked",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellContextMenu = create_callback(
            onCellContextMenu,
            "onCellContextMenu",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellDoubleClicked = create_callback(
            onCellDoubleClicked,
            "onCellDoubleClicked",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellEditRequest = create_callback(
            onCellEditRequest,
            "onCellEditRequest",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "source"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "newValue"],
                [0, "column", "header"],
            ],
        )
        self.onCellEditingStarted = create_callback(
            onCellEditingStarted,
            "onCellEditingStarted",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellEditingStopped = create_callback(
            onCellEditingStopped,
            "onCellEditingStopped",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "newValue"],
                [0, "column", "header"],
            ],
        )
        self.onCellFocused = create_callback(
            onCellFocused,
            "onCellFocused",
            [
                [0, "rowPinned"],
                [0, "isFullWidthCell"],
                [0, "preventScrollOnBrowserFocus"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "forceBrowserFocus"],
                [0, "floating"],
            ],
        )
        self.onCellKeyDown = create_callback(
            onCellKeyDown,
            "onCellKeyDown",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellKeyPress = create_callback(
            onCellKeyPress,
            "onCellKeyPress",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellMouseDown = create_callback(
            onCellMouseDown,
            "onCellMouseDown",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellMouseOut = create_callback(
            onCellMouseOut,
            "onCellMouseOut",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellMouseOver = create_callback(
            onCellMouseOver,
            "onCellMouseOver",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "column", "header"],
            ],
        )
        self.onCellValueChanged = create_callback(
            onCellValueChanged,
            "onCellValueChanged",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "source"],
                [0, "type"],
                [0, "rowIndex"],
                [0, "newValue"],
                [0, "column", "header"],
            ],
        )
        self.onChartCreated = create_callback(
            onChartCreated, "onChartCreated", [[0, "chartId"], [0, "type"]]
        )
        self.onChartDestroyed = create_callback(
            onChartDestroyed, "onChartDestroyed", [[0, "chartId"], [0, "type"]]
        )
        self.onChartOptionsChanged = create_callback(
            onChartOptionsChanged,
            "onChartOptionsChanged",
            [[0, "chartType"], [0, "chartThemeName"], [0, "chartId"], [0, "type"]],
        )
        self.onChartRangeSelectionChanged = create_callback(
            onChartRangeSelectionChanged,
            "onChartRangeSelectionChanged",
            [[0, "id"], [0, "chartId"], [0, "type"]],
        )
        self.onColumnAggFuncChangeRequest = create_callback(
            onColumnAggFuncChangeRequest,
            "onColumnAggFuncChangeRequest",
            [[0, "aggFunc"], [0, "[]", "columns", "header"], [0, "type"]],
        )
        self.onColumnEverythingChanged = create_callback(
            onColumnEverythingChanged,
            "onColumnEverythingChanged",
            [[0, "source"], [0, "type"]],
        )
        self.onColumnGroupOpened = create_callback(
            onColumnGroupOpened,
            "onColumnGroupOpened",
            [[0, "columnGroup", "header"], [0, "type"]],
        )
        self.onColumnMoved = create_callback(
            onColumnMoved,
            "onColumnMoved",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "toIndex"],
                [0, "type"],
                [0, "column", "header"],
            ],
        )
        self.onColumnPinned = create_callback(
            onColumnPinned,
            "onColumnPinned",
            [
                [0, "pinned"],
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "type"],
                [0, "column", "header"],
            ],
        )
        self.onColumnPivotChangeRequest = create_callback(
            onColumnPivotChangeRequest,
            "onColumnPivotChangeRequest",
            [[0, "[]", "columns", "header"], [0, "type"]],
        )
        self.onColumnPivotChanged = create_callback(
            onColumnPivotChanged,
            "onColumnPivotChanged",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "column", "header"],
                [0, "type"],
            ],
        )
        self.onColumnPivotModeChanged = create_callback(
            onColumnPivotModeChanged, "onColumnPivotModeChanged", [[0, "type"]]
        )
        self.onColumnResized = create_callback(
            onColumnResized,
            "onColumnResized",
            [
                [0, "[]", "columns", "header"],
                [0, "[]", "flexColumns", "header"],
                [0, "source"],
                [0, "type"],
                [0, "finished"],
                [0, "column", "header"],
            ],
        )
        self.onColumnRowGroupChangeRequest = create_callback(
            onColumnRowGroupChangeRequest,
            "onColumnRowGroupChangeRequest",
            [[0, "[]", "columns", "header"], [0, "type"]],
        )
        self.onColumnRowGroupChanged = create_callback(
            onColumnRowGroupChanged,
            "onColumnRowGroupChanged",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "column", "header"],
                [0, "type"],
            ],
        )
        self.onColumnValueChangeRequest = create_callback(
            onColumnValueChangeRequest,
            "onColumnValueChangeRequest",
            [[0, "[]", "columns", "header"], [0, "type"]],
        )
        self.onColumnValueChanged = create_callback(
            onColumnValueChanged,
            "onColumnValueChanged",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "column", "header"],
                [0, "type"],
            ],
        )
        self.onColumnVisible = create_callback(
            onColumnVisible,
            "onColumnVisible",
            [
                [0, "[]", "columns", "header"],
                [0, "source"],
                [0, "visible"],
                [0, "type"],
                [0, "column", "header"],
            ],
        )
        self.onComponentStateChanged = create_callback(
            onComponentStateChanged, "onComponentStateChanged", [[0, "type"]]
        )
        self.onDisplayedColumnsChanged = create_callback(
            onDisplayedColumnsChanged, "onDisplayedColumnsChanged", [[0, "type"]]
        )
        self.onDragStarted = create_callback(
            onDragStarted, "onDragStarted", [[0, "type"]]
        )
        self.onDragStopped = create_callback(
            onDragStopped, "onDragStopped", [[0, "type"]]
        )
        self.onExpandOrCollapseAll = create_callback(
            onExpandOrCollapseAll, "onExpandOrCollapseAll", [[0, "source"], [0, "type"]]
        )
        self.onFilterChanged = create_callback(
            onFilterChanged,
            "onFilterChanged",
            [
                [0, "afterDataChange"],
                [0, "afterFloatingFilter"],
                [0, "[]", "columns", "header"],
                [0, "type"],
            ],
        )
        self.onFilterModified = create_callback(
            onFilterModified, "onFilterModified", [[0, "column", "header"], [0, "type"]]
        )
        self.onFilterOpened = create_callback(
            onFilterOpened, "onFilterOpened", [[0, "column", "header"], [0, "type"]]
        )
        self.onFirstDataRendered = create_callback(
            onFirstDataRendered,
            "onFirstDataRendered",
            [[0, "lastRow"], [0, "firstRow"], [0, "type"]],
        )
        self.onGridColumnsChanged = create_callback(
            onGridColumnsChanged, "onGridColumnsChanged", [[0, "type"]]
        )
        self.onGridReady = create_callback(onGridReady, "onGridReady")
        self.onGridSizeChanged = create_callback(
            onGridSizeChanged,
            "onGridSizeChanged",
            [[0, "clientHeight"], [0, "clientWidth"], [0, "type"]],
        )
        self.onModelUpdated = create_callback(
            onModelUpdated,
            "onModelUpdated",
            [
                [0, "newData"],
                [0, "animate"],
                [0, "keepRenderedRows"],
                [0, "type"],
                [0, "keepUndoRedoStack"],
                [0, "newPage"],
            ],
        )
        self.onNewColumnsLoaded = create_callback(
            onNewColumnsLoaded, "onNewColumnsLoaded", [[0, "type"]]
        )
        self.onPaginationChanged = create_callback(
            onPaginationChanged,
            "onPaginationChanged",
            [
                [0, "newData"],
                [0, "animate"],
                [0, "keepRenderedRows"],
                [0, "type"],
                [0, "newPage"],
            ],
        )
        self.onPasteEnd = create_callback(
            onPasteEnd, "onPasteEnd", [[0, "source"], [0, "type"]]
        )
        self.onPasteStart = create_callback(
            onPasteStart, "onPasteStart", [[0, "source"], [0, "type"]]
        )
        self.onPinnedRowDataChanged = create_callback(
            onPinnedRowDataChanged, "onPinnedRowDataChanged", [[0, "type"]]
        )
        self.onRangeSelectionChanged = create_callback(
            onRangeSelectionChanged,
            "onRangeSelectionChanged",
            [[0, "id"], [0, "started"], [0, "finished"], [0, "type"]],
        )
        self.onRowClicked = create_callback(
            onRowClicked,
            "onRowClicked",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onRowDataUpdated = create_callback(
            onRowDataUpdated, "onRowDataUpdated", [[0, "type"]]
        )
        self.onRowDoubleClicked = create_callback(
            onRowDoubleClicked,
            "onRowDoubleClicked",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onRowDragEnd = create_callback(
            onRowDragEnd,
            "onRowDragEnd",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.onRowDragEnter = create_callback(
            onRowDragEnter,
            "onRowDragEnter",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.onRowDragLeave = create_callback(
            onRowDragLeave,
            "onRowDragLeave",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.onRowDragMove = create_callback(
            onRowDragMove,
            "onRowDragMove",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.onRowEditingStarted = create_callback(
            onRowEditingStarted,
            "onRowEditingStarted",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onRowEditingStopped = create_callback(
            onRowEditingStopped,
            "onRowEditingStopped",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onRowGroupOpened = create_callback(
            onRowGroupOpened,
            "onRowGroupOpened",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "expanded"],
                [0, "type"],
                [0, "rowIndex"],
            ],
        )
        self.onRowSelected = create_callback(
            onRowSelected,
            "onRowSelected",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onRowValueChanged = create_callback(
            onRowValueChanged,
            "onRowValueChanged",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.onSelectionChanged = create_callback(
            onSelectionChanged, "onSelectionChanged", [[0, "type"]]
        )
        self.onSortChanged = create_callback(
            onSortChanged, "onSortChanged", [[0, "source"], [0, "type"]]
        )
        self.onToolPanelVisibleChanged = create_callback(
            onToolPanelVisibleChanged,
            "onToolPanelVisibleChanged",
            [[0, "source"], [0, "type"]],
        )
        self.onViewportChanged = create_callback(
            onViewportChanged,
            "onViewportChanged",
            [[0, "lastRow"], [0, "firstRow"], [0, "type"]],
        )
        self.onVirtualColumnsChanged = create_callback(
            onVirtualColumnsChanged, "onVirtualColumnsChanged", [[0, "type"]]
        )
        self.onVirtualRowRemoved = create_callback(
            onVirtualRowRemoved,
            "onVirtualRowRemoved",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.overlayLoadingTemplate = overlayLoadingTemplate
        self.overlayNoRowsTemplate = overlayNoRowsTemplate
        self.paginateChildRows = paginateChildRows
        self.pagination = pagination
        self.paginationAutoPageSize = paginationAutoPageSize
        self.paginationChanged = create_callback(
            paginationChanged,
            "paginationChanged",
            [
                [0, "newData"],
                [0, "animate"],
                [0, "keepRenderedRows"],
                [0, "type"],
                [0, "newPage"],
            ],
        )
        self.paginationNumberFormatter = paginationNumberFormatter
        self.paginationPageSize = paginationPageSize
        self.pasteEnd = create_callback(
            pasteEnd, "pasteEnd", [[0, "source"], [0, "type"]]
        )
        self.pasteStart = create_callback(
            pasteStart, "pasteStart", [[0, "source"], [0, "type"]]
        )
        self.pinnedBottomRowData = pinnedBottomRowData
        self.pinnedRowDataChanged = create_callback(
            pinnedRowDataChanged, "pinnedRowDataChanged", [[0, "type"]]
        )
        self.pinnedTopRowData = pinnedTopRowData
        self.pivotColumnGroupTotals = pivotColumnGroupTotals
        self.pivotGroupHeaderHeight = pivotGroupHeaderHeight
        self.pivotHeaderHeight = pivotHeaderHeight
        self.pivotMode = pivotMode
        self.pivotPanelShow = pivotPanelShow
        self.pivotRowTotals = pivotRowTotals
        self.pivotSuppressAutoColumn = pivotSuppressAutoColumn
        self.popupParent = popupParent
        self.postProcessPopup = postProcessPopup
        self.postSortRows = postSortRows
        self.preventDefaultOnContextMenu = preventDefaultOnContextMenu
        self.processCellForClipboard = processCellForClipboard
        self.processCellFromClipboard = processCellFromClipboard
        self.processDataFromClipboard = processDataFromClipboard
        self.processGroupHeaderForClipboard = processGroupHeaderForClipboard
        self.processHeaderForClipboard = processHeaderForClipboard
        self.processPivotResultColDef = processPivotResultColDef
        self.processPivotResultColGroupDef = processPivotResultColGroupDef
        self.processRowPostCreate = processRowPostCreate
        self.purgeClosedRowNodes = purgeClosedRowNodes
        self.quickFilterText = quickFilterText
        self.rangeSelectionChanged = create_callback(
            rangeSelectionChanged,
            "rangeSelectionChanged",
            [[0, "id"], [0, "started"], [0, "finished"], [0, "type"]],
        )
        self.readOnlyEdit = readOnlyEdit
        self.removePivotHeaderRowWhenSingleValueColumn = (
            removePivotHeaderRowWhenSingleValueColumn
        )
        self.resetRowDataOnUpdate = resetRowDataOnUpdate
        self.rowBuffer = rowBuffer
        self.rowClass = rowClass
        self.rowClassRules = rowClassRules
        self.rowClicked = create_callback(
            rowClicked,
            "rowClicked",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.rowData = rowData
        self.rowDataUpdated = create_callback(
            rowDataUpdated, "rowDataUpdated", [[0, "type"]]
        )
        self.rowDoubleClicked = create_callback(
            rowDoubleClicked,
            "rowDoubleClicked",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.rowDragEnd = create_callback(
            rowDragEnd,
            "rowDragEnd",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.rowDragEnter = create_callback(
            rowDragEnter,
            "rowDragEnter",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.rowDragEntireRow = rowDragEntireRow
        self.rowDragLeave = create_callback(
            rowDragLeave,
            "rowDragLeave",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.rowDragManaged = rowDragManaged
        self.rowDragMove = create_callback(
            rowDragMove,
            "rowDragMove",
            [
                [0, "overNode", "data", "id"],
                [0, "node", "data", "id"],
                [0, "[]", "nodes", "data", "id"],
                [0, "y"],
                [0, "type"],
                [0, "overIndex"],
                [0, "vDirection"],
            ],
        )
        self.rowDragMultiRow = rowDragMultiRow
        self.rowEditingStarted = create_callback(
            rowEditingStarted,
            "rowEditingStarted",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.rowEditingStopped = create_callback(
            rowEditingStopped,
            "rowEditingStopped",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.rowGroupOpened = create_callback(
            rowGroupOpened,
            "rowGroupOpened",
            [
                [0, "node", "data", "id"],
                [0, "rowPinned"],
                [0, "expanded"],
                [0, "type"],
                [0, "rowIndex"],
            ],
        )
        self.rowGroupPanelShow = rowGroupPanelShow
        self.rowHeight = rowHeight
        self.rowModelType = rowModelType
        self.rowMultiSelectWithClick = rowMultiSelectWithClick
        self.rowSelected = create_callback(
            rowSelected,
            "rowSelected",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.rowSelection = rowSelection
        self.rowStyle = rowStyle
        self.rowValueChanged = create_callback(
            rowValueChanged,
            "rowValueChanged",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        self.scrollbarWidth = scrollbarWidth
        self.selectionChanged = create_callback(
            selectionChanged, "selectionChanged", [[0, "type"]]
        )
        self.sendToClipboard = sendToClipboard
        self.serverSideDatasource = serverSideDatasource
        self.serverSideFilterAllLevels = serverSideFilterAllLevels
        self.serverSideFilterOnServer = serverSideFilterOnServer
        self.serverSideInfiniteScroll = serverSideInfiniteScroll
        self.serverSideInitialRowCount = serverSideInitialRowCount
        self.serverSideSortAllLevels = serverSideSortAllLevels
        self.serverSideSortOnServer = serverSideSortOnServer
        self.showOpenedGroup = showOpenedGroup
        self.sideBar = sideBar
        self.singleClickEdit = singleClickEdit
        self.skipHeaderOnAutoSize = skipHeaderOnAutoSize
        self.sortChanged = create_callback(
            sortChanged, "sortChanged", [[0, "source"], [0, "type"]]
        )
        self.sortingOrder = sortingOrder
        self.statusBar = statusBar
        self.stopEditingWhenCellsLoseFocus = stopEditingWhenCellsLoseFocus
        self.suppressAggAtRootLevel = suppressAggAtRootLevel
        self.suppressAggFilteredOnly = suppressAggFilteredOnly
        self.suppressAggFuncInHeader = suppressAggFuncInHeader
        self.suppressAnimationFrame = suppressAnimationFrame
        self.suppressAsyncEvents = suppressAsyncEvents
        self.suppressAutoSize = suppressAutoSize
        self.suppressBrowserResizeObserver = suppressBrowserResizeObserver
        self.suppressCellFocus = suppressCellFocus
        self.suppressChangeDetection = suppressChangeDetection
        self.suppressClearOnFillReduction = suppressClearOnFillReduction
        self.suppressClickEdit = suppressClickEdit
        self.suppressClipboardApi = suppressClipboardApi
        self.suppressClipboardPaste = suppressClipboardPaste
        self.suppressColumnMoveAnimation = suppressColumnMoveAnimation
        self.suppressColumnVirtualisation = suppressColumnVirtualisation
        self.suppressContextMenu = suppressContextMenu
        self.suppressCopyRowsToClipboard = suppressCopyRowsToClipboard
        self.suppressCopySingleCellRanges = suppressCopySingleCellRanges
        self.suppressCsvExport = suppressCsvExport
        self.suppressDragLeaveHidesColumns = suppressDragLeaveHidesColumns
        self.suppressExcelExport = suppressExcelExport
        self.suppressExpandablePivotGroups = suppressExpandablePivotGroups
        self.suppressFieldDotNotation = suppressFieldDotNotation
        self.suppressFocusAfterRefresh = suppressFocusAfterRefresh
        self.suppressHorizontalScroll = suppressHorizontalScroll
        self.suppressLastEmptyLineOnPaste = suppressLastEmptyLineOnPaste
        self.suppressLoadingOverlay = suppressLoadingOverlay
        self.suppressMaintainUnsortedOrder = suppressMaintainUnsortedOrder
        self.suppressMakeColumnVisibleAfterUnGroup = (
            suppressMakeColumnVisibleAfterUnGroup
        )
        self.suppressMaxRenderedRowRestriction = suppressMaxRenderedRowRestriction
        self.suppressMenuHide = suppressMenuHide
        self.suppressMiddleClickScrolls = suppressMiddleClickScrolls
        self.suppressModelUpdateAfterUpdateTransaction = (
            suppressModelUpdateAfterUpdateTransaction
        )
        self.suppressMovableColumns = suppressMovableColumns
        self.suppressMoveWhenRowDragging = suppressMoveWhenRowDragging
        self.suppressMultiRangeSelection = suppressMultiRangeSelection
        self.suppressMultiSort = suppressMultiSort
        self.suppressNoRowsOverlay = suppressNoRowsOverlay
        self.suppressPaginationPanel = suppressPaginationPanel
        self.suppressParentsInRowNodes = suppressParentsInRowNodes
        self.suppressPreventDefaultOnMouseWheel = suppressPreventDefaultOnMouseWheel
        self.suppressPropertyNamesCheck = suppressPropertyNamesCheck
        self.suppressRowClickSelection = suppressRowClickSelection
        self.suppressRowDeselection = suppressRowDeselection
        self.suppressRowDrag = suppressRowDrag
        self.suppressRowGroupHidesColumns = suppressRowGroupHidesColumns
        self.suppressRowHoverHighlight = suppressRowHoverHighlight
        self.suppressRowTransform = suppressRowTransform
        self.suppressRowVirtualisation = suppressRowVirtualisation
        self.suppressScrollOnNewData = suppressScrollOnNewData
        self.suppressScrollWhenPopupsAreOpen = suppressScrollWhenPopupsAreOpen
        self.suppressTouch = suppressTouch
        self.tabIndex = tabIndex
        self.tabToNextCell = tabToNextCell
        self.tabToNextHeader = tabToNextHeader
        self.toolPanelVisibleChanged = create_callback(
            toolPanelVisibleChanged,
            "toolPanelVisibleChanged",
            [[0, "source"], [0, "type"]],
        )
        self.tooltipHideDelay = tooltipHideDelay
        self.tooltipMouseTrack = tooltipMouseTrack
        self.tooltipShowDelay = tooltipShowDelay
        self.treeData = treeData
        self.treeDataDisplayType = treeDataDisplayType
        self.unSortIcon = unSortIcon
        self.undoRedoCellEditing = undoRedoCellEditing
        self.undoRedoCellEditingLimit = undoRedoCellEditingLimit
        self.valueCache = valueCache
        self.valueCacheNeverExpires = valueCacheNeverExpires
        self.viewportChanged = create_callback(
            viewportChanged,
            "viewportChanged",
            [[0, "lastRow"], [0, "firstRow"], [0, "type"]],
        )
        self.viewportDatasource = viewportDatasource
        self.viewportRowModelBufferSize = viewportRowModelBufferSize
        self.viewportRowModelPageSize = viewportRowModelPageSize
        self.virtualColumnsChanged = create_callback(
            virtualColumnsChanged, "virtualColumnsChanged", [[0, "type"]]
        )
        self.virtualRowRemoved = create_callback(
            virtualRowRemoved,
            "virtualRowRemoved",
            [[0, "node", "data", "id"], [0, "rowIndex"], [0, "rowPinned"], [0, "type"]],
        )
        get_window().add_css([f"/static/{className}.css"])

    async def applyTransactionAsync(self, *args):
        return await self.call_method("api.applyTransactionAsync", args)

    async def autoSizeColumns(self, *args):
        return await self.call_method("columnApi.autoSizeColumns", args)

    async def getColumnDefs(self, *args):
        return await self.call_method("api.getColumnDefs", args)

    async def sizeColumnsToFit(self, *args):
        return await self.call_method("api.sizeColumnsToFit", args)
