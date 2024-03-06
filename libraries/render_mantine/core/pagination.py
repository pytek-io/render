from render import Component, create_callback, InputComponent, Props


class Pagination(InputComponent):
    Module = "mantine/core"
    JSXName = "Pagination"
    InputName = "page"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onFirstPage",
        "onLastPage",
        "onNextPage",
        "onPreviousPage",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "boundaries",
        "color",
        "component",
        "defaultValue",
        "disabled",
        "dotsIcon",
        "firstIcon",
        "gap",
        "getControlProps",
        "getItemProps",
        "h",
        "href",
        "lastIcon",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "nextIcon",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "previousIcon",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "siblings",
        "size",
        "sx",
        "ta",
        "target",
        "total",
        "value",
        "variant",
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
        autoContrast=None,
        boundaries=None,
        color=None,
        component=None,
        defaultValue=None,
        disabled=None,
        dotsIcon=None,
        firstIcon=None,
        gap=None,
        getControlProps=None,
        getItemProps=None,
        h=None,
        href=None,
        lastIcon=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        nextIcon=None,
        onFirstPage=None,
        onLastPage=None,
        onNextPage=None,
        onPreviousPage=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        previousIcon=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        siblings=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        total=None,
        value=None,
        variant=None,
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
        self.autoContrast = autoContrast
        self.boundaries = boundaries
        self.color = color
        self.component = component
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.dotsIcon = dotsIcon
        self.firstIcon = firstIcon
        self.gap = gap
        self.getControlProps = getControlProps
        self.getItemProps = getItemProps
        self.h = h
        self.href = href
        self.lastIcon = lastIcon
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nextIcon = nextIcon
        self.onFirstPage = create_callback(onFirstPage, "onFirstPage")
        self.onLastPage = create_callback(onLastPage, "onLastPage")
        self.onNextPage = create_callback(onNextPage, "onNextPage")
        self.onPreviousPage = create_callback(onPreviousPage, "onPreviousPage")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.previousIcon = previousIcon
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.siblings = siblings
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.total = total
        self.value = value
        self.variant = variant
        self.withControls = withControls
        self.withEdges = withEdges

    class Control(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Control"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "active",
            "component",
            "h",
            "href",
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
            "sx",
            "ta",
            "target",
            "variant",
            "withPadding",
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
            component=None,
            h=None,
            href=None,
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
            sx=None,
            ta=None,
            target=None,
            variant=None,
            withPadding=None,
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
            self.component = component
            self.h = h
            self.href = href
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant
            self.withPadding = withPadding

    class Dots(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Dots"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "icon",
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
            "sx",
            "ta",
            "target",
            "variant",
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
            component=None,
            h=None,
            href=None,
            icon=None,
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
            sx=None,
            ta=None,
            target=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.icon = icon
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant

    class First(Component):
        Module = "mantine/core"
        JSXName = "Pagination.First"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "icon",
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
            "sx",
            "ta",
            "target",
            "variant",
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
            component=None,
            h=None,
            href=None,
            icon=None,
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
            sx=None,
            ta=None,
            target=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.icon = icon
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant

    class Items(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Items"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "dotsIcon",
            "h",
            "href",
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
            "sx",
            "ta",
            "target",
            "variant",
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
            component=None,
            dotsIcon=None,
            h=None,
            href=None,
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
            ta=None,
            target=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.dotsIcon = dotsIcon
            self.h = h
            self.href = href
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
            self.ta = ta
            self.target = target
            self.variant = variant

    class Last(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Last"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "icon",
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
            "sx",
            "ta",
            "target",
            "variant",
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
            component=None,
            h=None,
            href=None,
            icon=None,
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
            sx=None,
            ta=None,
            target=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.icon = icon
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant

    class Next(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Next"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "icon",
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
            "sx",
            "ta",
            "target",
            "variant",
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
            component=None,
            h=None,
            href=None,
            icon=None,
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
            sx=None,
            ta=None,
            target=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.icon = icon
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant

    class Previous(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Previous"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "icon",
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
            "sx",
            "ta",
            "target",
            "variant",
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
            component=None,
            h=None,
            href=None,
            icon=None,
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
            sx=None,
            ta=None,
            target=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.icon = icon
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
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant

    class Root(Component):
        Module = "mantine/core"
        JSXName = "Pagination.Root"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "onChange",
            "onFirstPage",
            "onLastPage",
            "onNextPage",
            "onPreviousPage",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "autoContrast",
            "boundaries",
            "color",
            "component",
            "defaultValue",
            "disabled",
            "getItemProps",
            "h",
            "href",
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
            "radius",
            "siblings",
            "size",
            "sx",
            "ta",
            "target",
            "total",
            "value",
            "variant",
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
            autoContrast=None,
            boundaries=None,
            color=None,
            component=None,
            defaultValue=None,
            disabled=None,
            getItemProps=None,
            h=None,
            href=None,
            m=None,
            mb=None,
            me=None,
            ml=None,
            mr=None,
            ms=None,
            mt=None,
            mx=None,
            my=None,
            onChange=None,
            onFirstPage=None,
            onLastPage=None,
            onNextPage=None,
            onPreviousPage=None,
            p=None,
            pb=None,
            pe=None,
            pl=None,
            pr=None,
            ps=None,
            pt=None,
            px=None,
            py=None,
            radius=None,
            siblings=None,
            size=None,
            sx=None,
            ta=None,
            target=None,
            total=None,
            value=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.autoContrast = autoContrast
            self.boundaries = boundaries
            self.color = color
            self.component = component
            self.defaultValue = defaultValue
            self.disabled = disabled
            self.getItemProps = getItemProps
            self.h = h
            self.href = href
            self.m = m
            self.mb = mb
            self.me = me
            self.ml = ml
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.mx = mx
            self.my = my
            self.onChange = create_callback(onChange, "onChange")
            self.onFirstPage = create_callback(onFirstPage, "onFirstPage")
            self.onLastPage = create_callback(onLastPage, "onLastPage")
            self.onNextPage = create_callback(onNextPage, "onNextPage")
            self.onPreviousPage = create_callback(onPreviousPage, "onPreviousPage")
            self.p = p
            self.pb = pb
            self.pe = pe
            self.pl = pl
            self.pr = pr
            self.ps = ps
            self.pt = pt
            self.px = px
            self.py = py
            self.radius = radius
            self.siblings = siblings
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.total = total
            self.value = value
            self.variant = variant
