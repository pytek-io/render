from render import Component, create_callback


class NavLink(Component):
    Module = "mantine/core"
    JSXName = "NavLink"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onKeyDown"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "active",
        "autoContrast",
        "childrenOffset",
        "color",
        "component",
        "defaultOpened",
        "description",
        "disableRightSectionRotation",
        "disabled",
        "h",
        "href",
        "label",
        "leftSection",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "noWrap",
        "opened",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "rightSection",
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
        active=None,
        autoContrast=None,
        childrenOffset=None,
        color=None,
        component=None,
        defaultOpened=None,
        description=None,
        disableRightSectionRotation=None,
        disabled=None,
        h=None,
        href=None,
        label=None,
        leftSection=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        noWrap=None,
        onChange=None,
        onKeyDown=None,
        opened=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        rightSection=None,
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
        self.active = active
        self.autoContrast = autoContrast
        self.childrenOffset = childrenOffset
        self.color = color
        self.component = component
        self.defaultOpened = defaultOpened
        self.description = description
        self.disableRightSectionRotation = disableRightSectionRotation
        self.disabled = disabled
        self.h = h
        self.href = href
        self.label = label
        self.leftSection = leftSection
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.noWrap = noWrap
        self.onChange = create_callback(onChange, "onChange")
        self.onKeyDown = create_callback(onKeyDown, "onKeyDown")
        self.opened = opened
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.rightSection = rightSection
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
