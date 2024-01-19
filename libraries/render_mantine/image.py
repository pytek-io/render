from render import Component, create_callback, add_data_namespace, Props


class Image(Component):
    Module = "mantine"
    JSXName = "Image"
    CALLBACKS = ["onKeyPress", "onClick"]
    DATA = ["src"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alt",
        "caption",
        "fit",
        "height",
        "imageProps",
        "imageRef",
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
        "placeholder",
        "pr",
        "pt",
        "px",
        "py",
        "radius",
        "sx",
        "width",
        "withPlaceholder",
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
        alt=None,
        caption=None,
        fit=None,
        height=None,
        imageProps=None,
        imageRef=None,
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
        placeholder=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        src=None,
        sx=None,
        width=None,
        withPlaceholder=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alt = alt
        self.caption = caption
        self.fit = fit
        self.height = height
        self.imageProps = imageProps
        self.imageRef = imageRef
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
        self.placeholder = placeholder
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.src = add_data_namespace(src)
        self.sx = sx
        self.width = width
        self.withPlaceholder = withPlaceholder
