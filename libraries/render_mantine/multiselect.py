from render import Component, create_callback, InputComponent


class MultiSelect(InputComponent):
    Module = "mantine"
    JSXName = "MultiSelect"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onCreate", "onSearchChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "clearButtonLabel",
        "clearButtonTabIndex",
        "clearSearchOnBlur",
        "clearSearchOnChange",
        "clearable",
        "creatable",
        "dropdownComponent",
        "filter",
        "getCreateLabel",
        "m",
        "maxDropdownHeight",
        "maxSelectedValues",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "searchValue",
        "searchable",
        "selectOnBlur",
        "shouldCreate",
        "sx",
        "valueComponent",
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
        defaultValue=None,
        value=None,
        clearButtonLabel=None,
        clearButtonTabIndex=None,
        clearSearchOnBlur=None,
        clearSearchOnChange=None,
        clearable=None,
        creatable=None,
        dropdownComponent=None,
        filter=None,
        getCreateLabel=None,
        m=None,
        maxDropdownHeight=None,
        maxSelectedValues=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onCreate=None,
        onSearchChange=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        searchValue=None,
        searchable=None,
        selectOnBlur=None,
        shouldCreate=None,
        sx=None,
        valueComponent=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.clearButtonLabel = clearButtonLabel
        self.clearButtonTabIndex = clearButtonTabIndex
        self.clearSearchOnBlur = clearSearchOnBlur
        self.clearSearchOnChange = clearSearchOnChange
        self.clearable = clearable
        self.creatable = creatable
        self.dropdownComponent = dropdownComponent
        self.filter = filter
        self.getCreateLabel = getCreateLabel
        self.m = m
        self.maxDropdownHeight = maxDropdownHeight
        self.maxSelectedValues = maxSelectedValues
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onCreate = create_callback(onCreate, "onCreate")
        self.onSearchChange = create_callback(onSearchChange, "onSearchChange")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.searchValue = searchValue
        self.searchable = searchable
        self.selectOnBlur = selectOnBlur
        self.shouldCreate = shouldCreate
        self.sx = sx
        self.valueComponent = valueComponent


class MultiSelectValue(Component):
    Module = "mantine"
    JSXName = "MultiSelect.Value"
    CALLBACKS = ["onKeyPress", "onClick", "onRemove"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "disabled",
        "label",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "readOnly",
        "size",
        "sx",
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
        disabled=None,
        label=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onRemove=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        readOnly=None,
        size=None,
        sx=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.disabled = disabled
        self.label = label
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onRemove = create_callback(onRemove, "onRemove")
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.readOnly = readOnly
        self.size = size
        self.sx = sx
