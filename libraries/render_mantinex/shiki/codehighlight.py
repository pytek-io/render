from render import Component, create_callback


class CodeHighlight(Component):
    Module = "mantinex/shiki"
    JSXName = "CodeHighlight"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "code",
        "component",
        "copiedLabel",
        "copyLabel",
        "h",
        "highlightOnClient",
        "href",
        "language",
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
        "title",
        "variant",
        "withCopyButton",
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
        code=None,
        component=None,
        copiedLabel=None,
        copyLabel=None,
        h=None,
        highlightOnClient=None,
        href=None,
        language=None,
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
        title=None,
        variant=None,
        withCopyButton=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.code = code
        self.component = component
        self.copiedLabel = copiedLabel
        self.copyLabel = copyLabel
        self.h = h
        self.highlightOnClient = highlightOnClient
        self.href = href
        self.language = language
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
        self.title = title
        self.variant = variant
        self.withCopyButton = withCopyButton

    class Tabs(Component):
        Module = "mantinex/shiki"
        JSXName = "CodeHighlight.Tabs"
        CALLBACKS = ["onKeyPress", "onClick", "onExpandedChange", "onTabChange"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "activeTab",
            "code",
            "collapseCodeLabel",
            "component",
            "copiedLabel",
            "copyLabel",
            "defaultActiveTab",
            "defaultExpanded",
            "expandCodeLabel",
            "expanded",
            "getFileIcon",
            "h",
            "href",
            "m",
            "maxCollapsedHeight",
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
            "title",
            "variant",
            "withCopyButton",
            "withExpandButton",
            "withHeader",
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
            activeTab=None,
            code=None,
            collapseCodeLabel=None,
            component=None,
            copiedLabel=None,
            copyLabel=None,
            defaultActiveTab=None,
            defaultExpanded=None,
            expandCodeLabel=None,
            expanded=None,
            getFileIcon=None,
            h=None,
            href=None,
            m=None,
            maxCollapsedHeight=None,
            mb=None,
            me=None,
            ml=None,
            mr=None,
            ms=None,
            mt=None,
            mx=None,
            my=None,
            onExpandedChange=None,
            onTabChange=None,
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
            title=None,
            variant=None,
            withCopyButton=None,
            withExpandButton=None,
            withHeader=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.activeTab = activeTab
            self.code = code
            self.collapseCodeLabel = collapseCodeLabel
            self.component = component
            self.copiedLabel = copiedLabel
            self.copyLabel = copyLabel
            self.defaultActiveTab = defaultActiveTab
            self.defaultExpanded = defaultExpanded
            self.expandCodeLabel = expandCodeLabel
            self.expanded = expanded
            self.getFileIcon = getFileIcon
            self.h = h
            self.href = href
            self.m = m
            self.maxCollapsedHeight = maxCollapsedHeight
            self.mb = mb
            self.me = me
            self.ml = ml
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.mx = mx
            self.my = my
            self.onExpandedChange = create_callback(
                onExpandedChange, "onExpandedChange"
            )
            self.onTabChange = create_callback(onTabChange, "onTabChange")
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
            self.title = title
            self.variant = variant
            self.withCopyButton = withCopyButton
            self.withExpandButton = withExpandButton
            self.withHeader = withHeader
