from render import create_callback, Component, InputComponent


class Col(Component):
    Module = "mantine"
    JSXName = "Col"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        lg=None,
        m=None,
        mb=None,
        md=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        offset=None,
        offsetLg=None,
        offsetMd=None,
        offsetSm=None,
        offsetXl=None,
        offsetXs=None,
        order=None,
        orderLg=None,
        orderMd=None,
        orderSm=None,
        orderXl=None,
        orderXs=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sm=None,
        span=None,
        sx=None,
        xl=None,
        xs=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.lg = lg
        self.m = m
        self.mb = mb
        self.md = md
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.offset = offset
        self.offsetLg = offsetLg
        self.offsetMd = offsetMd
        self.offsetSm = offsetSm
        self.offsetXl = offsetXl
        self.offsetXs = offsetXs
        self.order = order
        self.orderLg = orderLg
        self.orderMd = orderMd
        self.orderSm = orderSm
        self.orderXl = orderXl
        self.orderXs = orderXs
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sm = sm
        self.span = span
        self.sx = sx
        self.xl = xl
        self.xs = xs
        assert id is None or isinstance(id, str)


class Grid(Component):
    Module = "mantine"
    JSXName = "Grid"

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
        columns=None,
        grow=None,
        gutter=None,
        justify=None,
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
        sx=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.align = align
        self.columns = columns
        self.grow = grow
        self.gutter = gutter
        self.justify = justify
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
        self.sx = sx
        assert id is None or isinstance(id, str)
