from render import create_callback, Component, InputComponent


class NavLink(Component):
    Module = "mantine"
    JSXName = "NavLink"

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
        childrenOffset=None,
        color=None,
        component=None,
        defaultOpened=None,
        description=None,
        disableRightSectionRotation=None,
        disabled=None,
        href=None,
        icon=None,
        label=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        noWrap=None,
        onChange=None,
        opened=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        rightSection=None,
        sx=None,
        target=None,
        title=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.active = active
        self.childrenOffset = childrenOffset
        self.color = color
        self.component = component
        self.defaultOpened = defaultOpened
        self.description = description
        self.disableRightSectionRotation = disableRightSectionRotation
        self.disabled = disabled
        self.href = href
        self.icon = icon
        self.label = label
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.noWrap = noWrap
        self.onChange = create_callback(onChange)
        self.opened = opened
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.rightSection = rightSection
        self.sx = sx
        self.target = target
        self.title = title
        self.variant = variant
        assert id is None or isinstance(id, str)
