from render import create_callback, Component, InputComponent


class Select(InputComponent):
    Module = "mantine"
    JSXName = "Select"
    InputName = "value"

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
        allowDeselect=None,
        clearButtonLabel=None,
        clearButtonTabIndex=None,
        clearable=None,
        creatable=None,
        dropdownComponent=None,
        filterDataOnExactSearchMatch=None,
        getCreateLabel=None,
        m=None,
        maxDropdownHeight=None,
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
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.allowDeselect = allowDeselect
        self.clearButtonLabel = clearButtonLabel
        self.clearButtonTabIndex = clearButtonTabIndex
        self.clearable = clearable
        self.creatable = creatable
        self.dropdownComponent = dropdownComponent
        self.filterDataOnExactSearchMatch = filterDataOnExactSearchMatch
        self.getCreateLabel = getCreateLabel
        self.m = m
        self.maxDropdownHeight = maxDropdownHeight
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onCreate = create_callback(onCreate)
        self.onSearchChange = create_callback(onSearchChange)
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
        assert id is None or isinstance(id, str)
