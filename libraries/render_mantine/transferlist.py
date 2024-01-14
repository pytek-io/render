from render import create_callback, Component, InputComponent


class TransferList(Component):
    Module = "mantine"
    JSXName = "TransferList"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        breakpoint=None,
        filter=None,
        initialSelection=None,
        itemComponent=None,
        limit=None,
        listComponent=None,
        listHeight=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        nothingFound=None,
        onChange=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        searchPlaceholder=None,
        showTransferAll=None,
        sx=None,
        titles=None,
        value=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.breakpoint = breakpoint
        self.filter = filter
        self.initialSelection = initialSelection
        self.itemComponent = itemComponent
        self.limit = limit
        self.listComponent = listComponent
        self.listHeight = listHeight
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nothingFound = nothingFound
        self.onChange = create_callback(onChange)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.searchPlaceholder = searchPlaceholder
        self.showTransferAll = showTransferAll
        self.sx = sx
        self.titles = titles
        self.value = value
        assert id is None or isinstance(id, str)
