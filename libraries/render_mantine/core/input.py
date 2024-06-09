from render import Component, create_callback, Props


class Input(Component):
    Module = "mantine/core"
    JSXName = "Input"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "disabled",
        "error",
        "h",
        "href",
        "leftSection",
        "leftSectionPointerEvents",
        "leftSectionProps",
        "leftSectionWidth",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "multiline",
        "mx",
        "my",
        "p",
        "pb",
        "pe",
        "pl",
        "pointer",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "required",
        "rightSection",
        "rightSectionPointerEvents",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "withAria",
        "withErrorStyles",
        "wrapperProps",
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
        disabled=None,
        error=None,
        h=None,
        href=None,
        leftSection=None,
        leftSectionPointerEvents=None,
        leftSectionProps=None,
        leftSectionWidth=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        multiline=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pointer=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionPointerEvents=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        withAria=None,
        withErrorStyles=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.component = component
        self.disabled = disabled
        self.error = error
        self.h = h
        self.href = href
        self.leftSection = leftSection
        self.leftSectionPointerEvents = leftSectionPointerEvents
        self.leftSectionProps = leftSectionProps
        self.leftSectionWidth = leftSectionWidth
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.multiline = multiline
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pointer = pointer
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionPointerEvents = rightSectionPointerEvents
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withAria = withAria
        self.withErrorStyles = withErrorStyles
        self.wrapperProps = wrapperProps

    class Description(Component):
        Module = "mantine/core"
        JSXName = "Input.Description"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
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
            "size",
            "sx",
            "ta",
            "target",
            "title",
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
            size=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
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
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant

    class Error(Component):
        Module = "mantine/core"
        JSXName = "Input.Error"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
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
            "size",
            "sx",
            "ta",
            "target",
            "title",
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
            size=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
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
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant

    class Label(Component):
        Module = "mantine/core"
        JSXName = "Input.Label"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "h",
            "href",
            "labelElement",
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
            "required",
            "size",
            "sx",
            "ta",
            "target",
            "title",
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
            labelElement=None,
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
            required=None,
            size=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.h = h
            self.href = href
            self.labelElement = labelElement
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
            self.required = required
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant

    class Wrapper(Component):
        Module = "mantine/core"
        JSXName = "Input.Wrapper"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "description",
            "descriptionProps",
            "error",
            "errorProps",
            "h",
            "href",
            "inputContainer",
            "inputWrapperOrder",
            "label",
            "labelElement",
            "labelProps",
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
            "required",
            "size",
            "sx",
            "ta",
            "target",
            "title",
            "variant",
            "withAsterisk",
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
            description=None,
            descriptionProps=None,
            error=None,
            errorProps=None,
            h=None,
            href=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelElement=None,
            labelProps=None,
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
            required=None,
            size=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            withAsterisk=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.description = description
            self.descriptionProps = descriptionProps
            self.error = error
            self.errorProps = errorProps
            self.h = h
            self.href = href
            self.inputContainer = inputContainer
            self.inputWrapperOrder = inputWrapperOrder
            self.label = label
            self.labelElement = labelElement
            self.labelProps = labelProps
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
            self.required = required
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant
            self.withAsterisk = withAsterisk
