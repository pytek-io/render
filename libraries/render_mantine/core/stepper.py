from render import Component, create_callback


class Stepper(Component):
    Module = "mantine/core"
    JSXName = "Stepper"
    CALLBACKS = ["onKeyPress", "onClick", "onStepClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "allowNextStepsSelect",
        "autoContrast",
        "color",
        "completedIcon",
        "component",
        "contentPadding",
        "h",
        "href",
        "icon",
        "iconPosition",
        "iconSize",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "orientation",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "progressIcon",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "size",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "wrap",
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
        allowNextStepsSelect=None,
        autoContrast=None,
        color=None,
        completedIcon=None,
        component=None,
        contentPadding=None,
        h=None,
        href=None,
        icon=None,
        iconPosition=None,
        iconSize=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        onStepClick=None,
        orientation=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        progressIcon=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        wrap=None,
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
        self.allowNextStepsSelect = allowNextStepsSelect
        self.autoContrast = autoContrast
        self.color = color
        self.completedIcon = completedIcon
        self.component = component
        self.contentPadding = contentPadding
        self.h = h
        self.href = href
        self.icon = icon
        self.iconPosition = iconPosition
        self.iconSize = iconSize
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onStepClick = create_callback(onStepClick, "onStepClick")
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.progressIcon = progressIcon
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.wrap = wrap

    class Step(Component):
        Module = "mantine/core"
        JSXName = "Stepper.Step"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "allowStepClick",
            "allowStepSelect",
            "color",
            "completedIcon",
            "component",
            "description",
            "h",
            "href",
            "icon",
            "iconPosition",
            "iconSize",
            "label",
            "loading",
            "m",
            "mb",
            "me",
            "ml",
            "mr",
            "ms",
            "mt",
            "mx",
            "my",
            "orientation",
            "p",
            "pb",
            "pe",
            "pl",
            "pr",
            "progressIcon",
            "ps",
            "pt",
            "px",
            "py",
            "state",
            "step",
            "sx",
            "ta",
            "target",
            "title",
            "variant",
            "withIcon",
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
            allowStepClick=None,
            allowStepSelect=None,
            color=None,
            completedIcon=None,
            component=None,
            description=None,
            h=None,
            href=None,
            icon=None,
            iconPosition=None,
            iconSize=None,
            label=None,
            loading=None,
            m=None,
            mb=None,
            me=None,
            ml=None,
            mr=None,
            ms=None,
            mt=None,
            mx=None,
            my=None,
            orientation=None,
            p=None,
            pb=None,
            pe=None,
            pl=None,
            pr=None,
            progressIcon=None,
            ps=None,
            pt=None,
            px=None,
            py=None,
            state=None,
            step=None,
            sx=None,
            ta=None,
            target=None,
            title=None,
            variant=None,
            withIcon=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.allowStepClick = allowStepClick
            self.allowStepSelect = allowStepSelect
            self.color = color
            self.completedIcon = completedIcon
            self.component = component
            self.description = description
            self.h = h
            self.href = href
            self.icon = icon
            self.iconPosition = iconPosition
            self.iconSize = iconSize
            self.label = label
            self.loading = loading
            self.m = m
            self.mb = mb
            self.me = me
            self.ml = ml
            self.mr = mr
            self.ms = ms
            self.mt = mt
            self.mx = mx
            self.my = my
            self.orientation = orientation
            self.p = p
            self.pb = pb
            self.pe = pe
            self.pl = pl
            self.pr = pr
            self.progressIcon = progressIcon
            self.ps = ps
            self.pt = pt
            self.px = px
            self.py = py
            self.state = state
            self.step = step
            self.sx = sx
            self.ta = ta
            self.target = target
            self.title = title
            self.variant = variant
            self.withIcon = withIcon
