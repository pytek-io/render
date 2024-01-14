from render import create_callback, Component, InputComponent


class AppShell(Component):
    Module = "mantine"
    JSXName = "AppShell"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        aside=None,
        asideOffsetBreakpoint=None,
        fixed=None,
        footer=None,
        header=None,
        hidden=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        navbar=None,
        navbarOffsetBreakpoint=None,
        p=None,
        padding=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.aside = aside
        self.asideOffsetBreakpoint = asideOffsetBreakpoint
        self.fixed = fixed
        self.footer = footer
        self.header = header
        self.hidden = hidden
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.navbar = navbar
        self.navbarOffsetBreakpoint = navbarOffsetBreakpoint
        self.p = p
        self.padding = padding
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)


class Aside(Component):
    Module = "mantine"
    JSXName = "Aside"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        fixed=None,
        height=None,
        hidden=None,
        hiddenBreakpoint=None,
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
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        width=None,
        withBorder=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.fixed = fixed
        self.height = height
        self.hidden = hidden
        self.hiddenBreakpoint = hiddenBreakpoint
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
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.width = width
        self.withBorder = withBorder
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)


class Footer(Component):
    Module = "mantine"
    JSXName = "Footer"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        fixed=None,
        height=None,
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
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        withBorder=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.fixed = fixed
        self.height = height
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
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.withBorder = withBorder
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)


class Header(Component):
    Module = "mantine"
    JSXName = "Header"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        fixed=None,
        height=None,
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
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        withBorder=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.fixed = fixed
        self.height = height
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
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.withBorder = withBorder
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)


class Navbar(Component):
    Module = "mantine"
    JSXName = "Navbar"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        fixed=None,
        height=None,
        hidden=None,
        hiddenBreakpoint=None,
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
        position=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        width=None,
        withBorder=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.fixed = fixed
        self.height = height
        self.hidden = hidden
        self.hiddenBreakpoint = hiddenBreakpoint
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
        self.position = position
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.width = width
        self.withBorder = withBorder
        self.zIndex = zIndex
        assert id is None or isinstance(id, str)
