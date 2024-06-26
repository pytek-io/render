from render import Component, create_callback, Props


class Pill(Component):
    Module = "mantine/core"
    JSXName = "Pill"
    CALLBACKS = ["onKeyPress", "onClick", "onRemove"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "disabled",
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
        "removeButtonProps",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "withRemoveButton",
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
        onRemove=None,
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
        removeButtonProps=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        withRemoveButton=None,
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
        self.onRemove = create_callback(onRemove, "onRemove")
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
        self.removeButtonProps = removeButtonProps
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withRemoveButton = withRemoveButton

    class Group(Component):
        Module = "mantine/core"
        JSXName = "Pill.Group"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "disabled",
            "gap",
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
            disabled=None,
            gap=None,
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
            self.disabled = disabled
            self.gap = gap
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

    class sInput(Component):
        Module = "mantine/core"
        JSXName = "Pill.sInput"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "description",
            "descriptionProps",
            "disabled",
            "error",
            "errorProps",
            "h",
            "href",
            "inputContainer",
            "inputWrapperOrder",
            "label",
            "labelProps",
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
            "withAsterisk",
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
            description=None,
            descriptionProps=None,
            disabled=None,
            error=None,
            errorProps=None,
            h=None,
            href=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelProps=None,
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
            withAsterisk=None,
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
            self.description = description
            self.descriptionProps = descriptionProps
            self.disabled = disabled
            self.error = error
            self.errorProps = errorProps
            self.h = h
            self.href = href
            self.inputContainer = inputContainer
            self.inputWrapperOrder = inputWrapperOrder
            self.label = label
            self.labelProps = labelProps
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
            self.withAsterisk = withAsterisk
            self.withErrorStyles = withErrorStyles
            self.wrapperProps = wrapperProps
