from render import Component, create_callback


class Table(Component):
    Module = "mantine"
    JSXName = "Table"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "captionSide",
        "fontSize",
        "highlightOnHover",
        "horizontalSpacing",
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
        "striped",
        "sx",
        "verticalSpacing",
        "withBorder",
        "withColumnBorders",
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
        captionSide=None,
        fontSize=None,
        highlightOnHover=None,
        horizontalSpacing=None,
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
        striped=None,
        sx=None,
        verticalSpacing=None,
        withBorder=None,
        withColumnBorders=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.captionSide = captionSide
        self.fontSize = fontSize
        self.highlightOnHover = highlightOnHover
        self.horizontalSpacing = horizontalSpacing
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
        self.striped = striped
        self.sx = sx
        self.verticalSpacing = verticalSpacing
        self.withBorder = withBorder
        self.withColumnBorders = withColumnBorders
