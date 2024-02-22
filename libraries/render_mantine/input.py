from render import Component, create_callback, Props


class Input(Component):
    Module = "mantine"
    JSXName = "Input"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "component",
        "disabled",
        "href",
        "icon",
        "iconWidth",
        "invalid",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "multiline",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "pointer",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "required",
        "rightSection",
        "rightSectionProps",
        "rightSectionWidth",
        "size",
        "sx",
        "target",
        "title",
        "variant",
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
        href=None,
        icon=None,
        iconWidth=None,
        invalid=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        multiline=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pl=None,
        pointer=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        required=None,
        rightSection=None,
        rightSectionProps=None,
        rightSectionWidth=None,
        size=None,
        sx=None,
        target=None,
        title=None,
        variant=None,
        wrapperProps=None,
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
        self.disabled = disabled
        self.href = href
        self.icon = icon
        self.iconWidth = iconWidth
        self.invalid = invalid
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.multiline = multiline
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pointer = pointer
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.required = required
        self.rightSection = rightSection
        self.rightSectionProps = rightSectionProps
        self.rightSectionWidth = rightSectionWidth
        self.size = size
        self.sx = sx
        self.target = target
        self.title = title
        self.variant = variant
        self.wrapperProps = wrapperProps
