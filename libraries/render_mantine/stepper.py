from render import Component, create_callback


class Step(Component):
    Module = "mantine"
    JSXName = "Step"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "allowStepClick",
        "allowStepSelect",
        "color",
        "completedIcon",
        "description",
        "icon",
        "iconPosition",
        "iconSize",
        "label",
        "loading",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "orientation",
        "p",
        "pb",
        "pl",
        "pr",
        "progressIcon",
        "pt",
        "px",
        "py",
        "radius",
        "size",
        "state",
        "sx",
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
        description=None,
        icon=None,
        iconPosition=None,
        iconSize=None,
        label=None,
        loading=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        orientation=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        progressIcon=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        size=None,
        state=None,
        sx=None,
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
        self.description = description
        self.icon = icon
        self.iconPosition = iconPosition
        self.iconSize = iconSize
        self.label = label
        self.loading = loading
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.progressIcon = progressIcon
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.size = size
        self.state = state
        self.sx = sx
        self.withIcon = withIcon


class Stepper(Component):
    Module = "mantine"
    JSXName = "Stepper"
    CALLBACKS = ["onKeyPress", "onClick", "onStepClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "breakpoint",
        "color",
        "completedIcon",
        "contentPadding",
        "iconPosition",
        "iconSize",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "orientation",
        "p",
        "pb",
        "pl",
        "pr",
        "progressIcon",
        "pt",
        "px",
        "py",
        "radius",
        "size",
        "sx",
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
        breakpoint=None,
        color=None,
        completedIcon=None,
        contentPadding=None,
        iconPosition=None,
        iconSize=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onStepClick=None,
        orientation=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        progressIcon=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        size=None,
        sx=None,
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
        self.breakpoint = breakpoint
        self.color = color
        self.completedIcon = completedIcon
        self.contentPadding = contentPadding
        self.iconPosition = iconPosition
        self.iconSize = iconSize
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onStepClick = create_callback(onStepClick, "onStepClick")
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.progressIcon = progressIcon
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.size = size
        self.sx = sx
