from render import Component, create_callback, Props


class Dropzone(Component):
    Module = "mantine/dropzone"
    JSXName = "Dropzone"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "getFilesFromEvent",
        "onDragEnter",
        "onDragLeave",
        "onDragOver",
        "onDrop",
        "onDropAny",
        "onFileDialogCancel",
        "onFileDialogOpen",
        "onReject",
        "openRef",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "accept",
        "acceptColor",
        "activateOnClick",
        "activateOnDrag",
        "activateOnKeyboard",
        "autoFocus",
        "component",
        "disabled",
        "dragEventsBubbling",
        "enablePointerEvents",
        "h",
        "href",
        "loaderProps",
        "loading",
        "m",
        "maxFiles",
        "maxSize",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "multiple",
        "mx",
        "my",
        "name",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "preventDropOnDocument",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "rejectColor",
        "sx",
        "ta",
        "target",
        "useFsAccessApi",
        "validator",
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
        accept=None,
        acceptColor=None,
        activateOnClick=None,
        activateOnDrag=None,
        activateOnKeyboard=None,
        autoFocus=None,
        component=None,
        disabled=None,
        dragEventsBubbling=None,
        enablePointerEvents=None,
        getFilesFromEvent=None,
        h=None,
        href=None,
        loaderProps=None,
        loading=None,
        m=None,
        maxFiles=None,
        maxSize=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        multiple=None,
        mx=None,
        my=None,
        name=None,
        onDragEnter=None,
        onDragLeave=None,
        onDragOver=None,
        onDrop=None,
        onDropAny=None,
        onFileDialogCancel=None,
        onFileDialogOpen=None,
        onReject=None,
        openRef=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        preventDropOnDocument=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        rejectColor=None,
        sx=None,
        ta=None,
        target=None,
        useFsAccessApi=None,
        validator=None,
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
        self.accept = accept
        self.acceptColor = acceptColor
        self.activateOnClick = activateOnClick
        self.activateOnDrag = activateOnDrag
        self.activateOnKeyboard = activateOnKeyboard
        self.autoFocus = autoFocus
        self.component = component
        self.disabled = disabled
        self.dragEventsBubbling = dragEventsBubbling
        self.enablePointerEvents = enablePointerEvents
        self.getFilesFromEvent = create_callback(getFilesFromEvent, "getFilesFromEvent")
        self.h = h
        self.href = href
        self.loaderProps = loaderProps
        self.loading = loading
        self.m = m
        self.maxFiles = maxFiles
        self.maxSize = maxSize
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.multiple = multiple
        self.mx = mx
        self.my = my
        self.name = name
        self.onDragEnter = create_callback(onDragEnter, "onDragEnter")
        self.onDragLeave = create_callback(onDragLeave, "onDragLeave")
        self.onDragOver = create_callback(onDragOver, "onDragOver")
        self.onDrop = create_callback(onDrop, "onDrop")
        self.onDropAny = create_callback(onDropAny, "onDropAny")
        self.onFileDialogCancel = create_callback(
            onFileDialogCancel, "onFileDialogCancel"
        )
        self.onFileDialogOpen = create_callback(onFileDialogOpen, "onFileDialogOpen")
        self.onReject = create_callback(onReject, "onReject")
        self.openRef = create_callback(openRef, "openRef")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.preventDropOnDocument = preventDropOnDocument
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.rejectColor = rejectColor
        self.sx = sx
        self.ta = ta
        self.target = target
        self.useFsAccessApi = useFsAccessApi
        self.validator = validator
        self.variant = variant

    class FullScreen(Component):
        Module = "mantine/dropzone"
        JSXName = "Dropzone.FullScreen"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "getFilesFromEvent",
            "onDragEnter",
            "onDragLeave",
            "onDragOver",
            "onDrop",
            "onDropAny",
            "onFileDialogCancel",
            "onFileDialogOpen",
            "onReject",
            "openRef",
        ]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "accept",
            "acceptColor",
            "activateOnClick",
            "activateOnDrag",
            "activateOnKeyboard",
            "active",
            "autoFocus",
            "component",
            "disabled",
            "dragEventsBubbling",
            "enablePointerEvents",
            "h",
            "href",
            "loaderProps",
            "loading",
            "m",
            "maxFiles",
            "maxSize",
            "mb",
            "me",
            "ml",
            "mr",
            "ms",
            "mt",
            "multiple",
            "mx",
            "my",
            "name",
            "p",
            "pb",
            "pe",
            "pl",
            "portalProps",
            "pr",
            "preventDropOnDocument",
            "ps",
            "pt",
            "px",
            "py",
            "radius",
            "rejectColor",
            "sx",
            "ta",
            "target",
            "useFsAccessApi",
            "validator",
            "variant",
            "withinPortal",
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
            accept=None,
            acceptColor=None,
            activateOnClick=None,
            activateOnDrag=None,
            activateOnKeyboard=None,
            active=None,
            autoFocus=None,
            component=None,
            disabled=None,
            dragEventsBubbling=None,
            enablePointerEvents=None,
            getFilesFromEvent=None,
            h=None,
            href=None,
            loaderProps=None,
            loading=None,
            m=None,
            maxFiles=None,
            maxSize=None,
            mb=None,
            me=None,
            ml=None,
            mr=None,
            ms=None,
            mt=None,
            multiple=None,
            mx=None,
            my=None,
            name=None,
            onDragEnter=None,
            onDragLeave=None,
            onDragOver=None,
            onDrop=None,
            onDropAny=None,
            onFileDialogCancel=None,
            onFileDialogOpen=None,
            onReject=None,
            openRef=None,
            p=None,
            pb=None,
            pe=None,
            pl=None,
            portalProps=None,
            pr=None,
            preventDropOnDocument=None,
            ps=None,
            pt=None,
            px=None,
            py=None,
            radius=None,
            rejectColor=None,
            sx=None,
            ta=None,
            target=None,
            useFsAccessApi=None,
            validator=None,
            variant=None,
            withinPortal=None,
            zIndex=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.accept = accept
            self.acceptColor = acceptColor
            self.activateOnClick = activateOnClick
            self.activateOnDrag = activateOnDrag
            self.activateOnKeyboard = activateOnKeyboard
            self.active = active
            self.autoFocus = autoFocus
            self.component = component
            self.disabled = disabled
            self.dragEventsBubbling = dragEventsBubbling
            self.enablePointerEvents = enablePointerEvents
            self.getFilesFromEvent = create_callback(
                getFilesFromEvent, "getFilesFromEvent"
            )
            self.h = h
            self.href = href
            self.loaderProps = loaderProps
            self.loading = loading
            self.m = m
            self.maxFiles = maxFiles
            self.maxSize = maxSize
            self.mb = mb
            self.me = me
            self.ml = ml
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.multiple = multiple
            self.mx = mx
            self.my = my
            self.name = name
            self.onDragEnter = create_callback(onDragEnter, "onDragEnter")
            self.onDragLeave = create_callback(onDragLeave, "onDragLeave")
            self.onDragOver = create_callback(onDragOver, "onDragOver")
            self.onDrop = create_callback(onDrop, "onDrop")
            self.onDropAny = create_callback(onDropAny, "onDropAny")
            self.onFileDialogCancel = create_callback(
                onFileDialogCancel, "onFileDialogCancel"
            )
            self.onFileDialogOpen = create_callback(
                onFileDialogOpen, "onFileDialogOpen"
            )
            self.onReject = create_callback(onReject, "onReject")
            self.openRef = create_callback(openRef, "openRef")
            self.p = p
            self.pb = pb
            self.pe = pe
            self.pl = pl
            self.portalProps = portalProps
            self.pr = pr
            self.preventDropOnDocument = preventDropOnDocument
            self.ps = ps
            self.pt = pt
            self.px = px
            self.py = py
            self.radius = radius
            self.rejectColor = rejectColor
            self.sx = sx
            self.ta = ta
            self.target = target
            self.useFsAccessApi = useFsAccessApi
            self.validator = validator
            self.variant = variant
            self.withinPortal = withinPortal
            self.zIndex = zIndex
