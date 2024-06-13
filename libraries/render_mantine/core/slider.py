from render import Component, create_callback, InputComponent, Props


class Slider(InputComponent):
    Module = "mantine/core"
    JSXName = "Slider"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "component",
        "disabled",
        "h",
        "hiddenInputProps",
        "href",
        "inverted",
        "label",
        "labelAlwaysOn",
        "labelTransitionProps",
        "m",
        "marks",
        "max",
        "mb",
        "me",
        "min",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "name",
        "p",
        "pb",
        "pe",
        "pl",
        "pr",
        "precision",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "scale",
        "showLabelOnHover",
        "size",
        "step",
        "sx",
        "ta",
        "target",
        "thumbChildren",
        "thumbLabel",
        "thumbSize",
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
        color=None,
        component=None,
        disabled=None,
        h=None,
        hiddenInputProps=None,
        href=None,
        inverted=None,
        label=None,
        labelAlwaysOn=None,
        labelTransitionProps=None,
        m=None,
        marks=None,
        max=None,
        mb=None,
        me=None,
        min=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        name=None,
        onChangeEnd=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        pr=None,
        precision=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        scale=None,
        showLabelOnHover=None,
        size=None,
        step=None,
        sx=None,
        ta=None,
        target=None,
        thumbChildren=None,
        thumbLabel=None,
        thumbSize=None,
        title=None,
        variant=None,
        controller=None,
        onChange=None,
        value=None,
        defaultValue=None,
    ):
        super().__init__(key, controller, children, onChange, value, defaultValue)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.component = component
        self.disabled = disabled
        self.h = h
        self.hiddenInputProps = hiddenInputProps
        self.href = href
        self.inverted = inverted
        self.label = label
        self.labelAlwaysOn = labelAlwaysOn
        self.labelTransitionProps = labelTransitionProps
        self.m = m
        self.marks = marks
        self.max = max
        self.mb = mb
        self.me = me
        self.min = min
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.name = name
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.pr = pr
        self.precision = precision
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.scale = scale
        self.showLabelOnHover = showLabelOnHover
        self.size = size
        self.step = step
        self.sx = sx
        self.ta = ta
        self.target = target
        self.thumbChildren = thumbChildren
        self.thumbLabel = thumbLabel
        self.thumbSize = thumbSize
        self.title = title
        self.variant = variant
