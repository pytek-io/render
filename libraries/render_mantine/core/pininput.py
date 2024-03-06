from render import Component, create_callback, Props


class PinInput(Component):
    Module = "mantine/core"
    JSXName = "PinInput"
    CALLBACKS = ["onKeyPress", "onClick", "onChange", "onComplete"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "ariaLabel",
        "autoFocus",
        "component",
        "defaultValue",
        "disabled",
        "error",
        "form",
        "gap",
        "h",
        "hiddenInputProps",
        "href",
        "inputMode",
        "inputType",
        "length",
        "m",
        "manageFocus",
        "mask",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "name",
        "oneTimeCode",
        "p",
        "pb",
        "pe",
        "pl",
        "placeholder",
        "pr",
        "ps",
        "pt",
        "px",
        "py",
        "radius",
        "readOnly",
        "size",
        "sx",
        "ta",
        "target",
        "type",
        "value",
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
        ariaLabel=None,
        autoFocus=None,
        component=None,
        defaultValue=None,
        disabled=None,
        error=None,
        form=None,
        gap=None,
        h=None,
        hiddenInputProps=None,
        href=None,
        inputMode=None,
        inputType=None,
        length=None,
        m=None,
        manageFocus=None,
        mask=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        name=None,
        onChange=None,
        onComplete=None,
        oneTimeCode=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        placeholder=None,
        pr=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        radius=None,
        readOnly=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        type=None,
        value=None,
        variant=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.ariaLabel = ariaLabel
        self.autoFocus = autoFocus
        self.component = component
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.error = error
        self.form = form
        self.gap = gap
        self.h = h
        self.hiddenInputProps = hiddenInputProps
        self.href = href
        self.inputMode = inputMode
        self.inputType = inputType
        self.length = length
        self.m = m
        self.manageFocus = manageFocus
        self.mask = mask
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.name = name
        self.onChange = create_callback(onChange, "onChange")
        self.onComplete = create_callback(onComplete, "onComplete")
        self.oneTimeCode = oneTimeCode
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.placeholder = placeholder
        self.pr = pr
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.radius = radius
        self.readOnly = readOnly
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.type = type
        self.value = value
        self.variant = variant
