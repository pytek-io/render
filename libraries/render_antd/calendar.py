from render import Component, create_callback


class Calendar(Component):
    Module = "ant"
    JSXName = "Calendar"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onPanelChange", "onSelect"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "dateCellRender",
        "dateFullCellRender",
        "defaultValue",
        "disabledDate",
        "fullscreen",
        "headerRender",
        "locale",
        "mode",
        "monthCellRender",
        "monthFullCellRender",
        "validRange",
        "value",
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
        dateCellRender=None,
        dateFullCellRender=None,
        defaultValue=None,
        disabledDate=None,
        fullscreen=None,
        headerRender=None,
        locale=None,
        mode=None,
        monthCellRender=None,
        monthFullCellRender=None,
        onChange=None,
        onPanelChange=None,
        onSelect=None,
        validRange=None,
        value=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.dateCellRender = dateCellRender
        self.dateFullCellRender = dateFullCellRender
        self.defaultValue = defaultValue
        self.disabledDate = disabledDate
        self.fullscreen = fullscreen
        self.headerRender = headerRender
        self.locale = locale
        self.mode = mode
        self.monthCellRender = monthCellRender
        self.monthFullCellRender = monthFullCellRender
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onPanelChange = create_callback(onPanelChange, "onPanelChange", [[0], [1]])
        self.onSelect = create_callback(onSelect, "onSelect", [[0], [1, "source"]])
        self.validRange = validRange
        self.value = value
