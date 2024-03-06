from render import Component, create_callback, InputComponent, Props


class Checkbox(InputComponent):
    Module = "mantine/core"
    JSXName = "Checkbox"
    InputName = "checked"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoContrast",
        "color",
        "component",
        "description",
        "error",
        "h",
        "href",
        "icon",
        "iconColor",
        "indeterminate",
        "label",
        "labelPosition",
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
        "rootRef",
        "size",
        "sx",
        "ta",
        "target",
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
        onChange=None,
        defaultChecked=None,
        checked=None,
        autoContrast=None,
        color=None,
        component=None,
        description=None,
        error=None,
        h=None,
        href=None,
        icon=None,
        iconColor=None,
        indeterminate=None,
        label=None,
        labelPosition=None,
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
        radius=None,
        rootRef=None,
        size=None,
        sx=None,
        ta=None,
        target=None,
        variant=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoContrast = autoContrast
        self.color = color
        self.component = component
        self.description = description
        self.error = error
        self.h = h
        self.href = href
        self.icon = icon
        self.iconColor = iconColor
        self.indeterminate = indeterminate
        self.label = label
        self.labelPosition = labelPosition
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
        self.radius = radius
        self.rootRef = rootRef
        self.size = size
        self.sx = sx
        self.ta = ta
        self.target = target
        self.variant = variant
        self.wrapperProps = wrapperProps

    class Group(InputComponent):
        Module = "mantine/core"
        JSXName = "Checkbox.Group"
        InputName = "value"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "component",
            "description",
            "descriptionProps",
            "error",
            "errorProps",
            "h",
            "href",
            "inputContainer",
            "inputWrapperOrder",
            "label",
            "labelElement",
            "labelProps",
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
            "readOnly",
            "required",
            "size",
            "sx",
            "ta",
            "target",
            "variant",
            "withAsterisk",
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
            onChange=None,
            defaultValue=None,
            value=None,
            component=None,
            description=None,
            descriptionProps=None,
            error=None,
            errorProps=None,
            h=None,
            href=None,
            inputContainer=None,
            inputWrapperOrder=None,
            label=None,
            labelElement=None,
            labelProps=None,
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
            readOnly=None,
            required=None,
            size=None,
            sx=None,
            ta=None,
            target=None,
            variant=None,
            withAsterisk=None,
            wrapperProps=None,
            controller=None,
        ):
            super().__init__(key, controller, onChange, value, defaultValue)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.component = component
            self.description = description
            self.descriptionProps = descriptionProps
            self.error = error
            self.errorProps = errorProps
            self.h = h
            self.href = href
            self.inputContainer = inputContainer
            self.inputWrapperOrder = inputWrapperOrder
            self.label = label
            self.labelElement = labelElement
            self.labelProps = labelProps
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
            self.readOnly = readOnly
            self.required = required
            self.size = size
            self.sx = sx
            self.ta = ta
            self.target = target
            self.variant = variant
            self.withAsterisk = withAsterisk
            self.wrapperProps = wrapperProps
