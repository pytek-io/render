from render import Component, create_callback, InputComponent


class Pagination(InputComponent):
    Module = "mantine"
    JSXName = "Pagination"
    InputName = "page"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "boundaries",
        "color",
        "disabled",
        "getItemAriaLabel",
        "initialPage",
        "itemComponent",
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
        "siblings",
        "size",
        "spacing",
        "sx",
        "total",
        "withControls",
        "withEdges",
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
        defaultPage=None,
        page=None,
        boundaries=None,
        color=None,
        disabled=None,
        getItemAriaLabel=None,
        initialPage=None,
        itemComponent=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        siblings=None,
        size=None,
        spacing=None,
        sx=None,
        total=None,
        withControls=None,
        withEdges=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, page, defaultPage)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.boundaries = boundaries
        self.color = color
        self.disabled = disabled
        self.getItemAriaLabel = getItemAriaLabel
        self.initialPage = initialPage
        self.itemComponent = itemComponent
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.siblings = siblings
        self.size = size
        self.spacing = spacing
        self.sx = sx
        self.total = total
        self.withControls = withControls
        self.withEdges = withEdges


class PaginationItem(Component):
    Module = "mantine"
    JSXName = "PaginationItem"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "page",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
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
        active=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        page=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
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
        self.active = active
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.page = page
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
