from render import Component, create_callback


class Table(Component):
    Module = "mantine/core"
    JSXName = "Table"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "borderColor",
        "captionSide",
        "component",
        "data",
        "h",
        "highlightOnHover",
        "highlightOnHoverColor",
        "horizontalSpacing",
        "href",
        "layout",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "stickyHeader",
        "stickyHeaderOffset",
        "striped",
        "stripedColor",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "verticalSpacing",
        "withColumnBorders",
        "withRowBorders",
        "withTableBorder",
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
        borderColor=None,
        captionSide=None,
        component=None,
        data=None,
        h=None,
        highlightOnHover=None,
        highlightOnHoverColor=None,
        horizontalSpacing=None,
        href=None,
        layout=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        stickyHeader=None,
        stickyHeaderOffset=None,
        striped=None,
        stripedColor=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        verticalSpacing=None,
        withColumnBorders=None,
        withRowBorders=None,
        withTableBorder=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.borderColor = borderColor
        self.captionSide = captionSide
        self.component = component
        self.data = data
        self.h = h
        self.highlightOnHover = highlightOnHover
        self.highlightOnHoverColor = highlightOnHoverColor
        self.horizontalSpacing = horizontalSpacing
        self.href = href
        self.layout = layout
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.stickyHeader = stickyHeader
        self.stickyHeaderOffset = stickyHeaderOffset
        self.striped = striped
        self.stripedColor = stripedColor
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.verticalSpacing = verticalSpacing
        self.withColumnBorders = withColumnBorders
        self.withRowBorders = withRowBorders
        self.withTableBorder = withTableBorder
