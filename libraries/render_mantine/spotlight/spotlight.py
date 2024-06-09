from render import Component, create_callback, Props


class Spotlight(Component):
    Module = "mantine/spotlight"
    JSXName = "Spotlight"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onQueryChange",
        "onSpotlightClose",
        "onSpotlightOpen",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "actions",
        "centered",
        "clearQueryOnClose",
        "closeOnActionTrigger",
        "closeOnClickOutside",
        "closeOnEscape",
        "component",
        "disabled",
        "filter",
        "forceOpened",
        "fullScreen",
        "h",
        "highlightQuery",
        "href",
        "keepMounted",
        "limit",
        "lockScroll",
        "m",
        "maxHeight",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "nothingFound",
        "overlayProps",
        "p",
        "padding",
        "pb",
        "pe",
        "pl",
        "portalProps",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "query",
        "radius",
        "removeScrollProps",
        "returnFocus",
        "scrollAreaComponent",
        "scrollable",
        "searchProps",
        "shadow",
        "shortcut",
        "size",
        "store",
        "sx",
        "ta",
        "tagsToIgnore",
        "target",
        "title",
        "transitionProps",
        "trapFocus",
        "triggerOnContentEditable",
        "variant",
        "withOverlay",
        "withinPortal",
        "xOffset",
        "yOffset",
        "zIndex",
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
        actions=None,
        centered=None,
        clearQueryOnClose=None,
        closeOnActionTrigger=None,
        closeOnClickOutside=None,
        closeOnEscape=None,
        component=None,
        disabled=None,
        filter=None,
        forceOpened=None,
        fullScreen=None,
        h=None,
        highlightQuery=None,
        href=None,
        keepMounted=None,
        limit=None,
        lockScroll=None,
        m=None,
        maxHeight=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        nothingFound=None,
        onQueryChange=None,
        onSpotlightClose=None,
        onSpotlightOpen=None,
        overlayProps=None,
        p=None,
        padding=None,
        pb=None,
        pe=None,
        pl=None,
        portalProps=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        query=None,
        radius=None,
        removeScrollProps=None,
        returnFocus=None,
        scrollAreaComponent=None,
        scrollable=None,
        searchProps=None,
        shadow=None,
        shortcut=None,
        size=None,
        store=None,
        sx=None,
        ta=None,
        tagsToIgnore=None,
        target=None,
        title=None,
        transitionProps=None,
        trapFocus=None,
        triggerOnContentEditable=None,
        variant=None,
        withOverlay=None,
        withinPortal=None,
        xOffset=None,
        yOffset=None,
        zIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.actions = actions
        self.centered = centered
        self.clearQueryOnClose = clearQueryOnClose
        self.closeOnActionTrigger = closeOnActionTrigger
        self.closeOnClickOutside = closeOnClickOutside
        self.closeOnEscape = closeOnEscape
        self.component = component
        self.disabled = disabled
        self.filter = filter
        self.forceOpened = forceOpened
        self.fullScreen = fullScreen
        self.h = h
        self.highlightQuery = highlightQuery
        self.href = href
        self.keepMounted = keepMounted
        self.limit = limit
        self.lockScroll = lockScroll
        self.m = m
        self.maxHeight = maxHeight
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nothingFound = nothingFound
        self.onQueryChange = create_callback(onQueryChange, "onQueryChange")
        self.onSpotlightClose = create_callback(onSpotlightClose, "onSpotlightClose")
        self.onSpotlightOpen = create_callback(onSpotlightOpen, "onSpotlightOpen")
        self.overlayProps = overlayProps
        self.p = p
        self.padding = padding
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.portalProps = portalProps
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.query = query
        self.radius = radius
        self.removeScrollProps = removeScrollProps
        self.returnFocus = returnFocus
        self.scrollAreaComponent = scrollAreaComponent
        self.scrollable = scrollable
        self.searchProps = searchProps
        self.shadow = shadow
        self.shortcut = shortcut
        self.size = size
        self.store = store
        self.sx = sx
        self.ta = ta
        self.tagsToIgnore = tagsToIgnore
        self.target = target
        self.title = title
        self.transitionProps = transitionProps
        self.trapFocus = trapFocus
        self.triggerOnContentEditable = triggerOnContentEditable
        self.variant = variant
        self.withOverlay = withOverlay
        self.withinPortal = withinPortal
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.zIndex = zIndex
