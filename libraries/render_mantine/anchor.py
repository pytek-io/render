from render import Component, create_callback


class Anchor(Component):
    Module = "mantine"
    JSXName = "Anchor"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "color",
        "component",
        "gradient",
        "href",
        "inherit",
        "inline",
        "italic",
        "lineClamp",
        "m",
        "mb",
        "ml",
        "mr",
        "mt",
        "mx",
        "my",
        "p",
        "pb",
        "pl",
        "pr",
        "pt",
        "px",
        "py",
        "size",
        "span",
        "strikethrough",
        "sx",
        "target",
        "title",
        "transform",
        "underline",
        "variant",
        "weight",
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
        align=None,
        color=None,
        component=None,
        gradient=None,
        href=None,
        inherit=None,
        inline=None,
        italic=None,
        lineClamp=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        span=None,
        strikethrough=None,
        sx=None,
        target=None,
        title=None,
        transform=None,
        underline=None,
        variant=None,
        weight=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.color = color
        self.component = component
        self.gradient = gradient
        self.href = href
        self.inherit = inherit
        self.inline = inline
        self.italic = italic
        self.lineClamp = lineClamp
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.span = span
        self.strikethrough = strikethrough
        self.sx = sx
        self.target = target
        self.title = title
        self.transform = transform
        self.underline = underline
        self.variant = variant
        self.weight = weight
