from render import create_callback, Component, InputComponent


class NumberInput(InputComponent):
    Module = "mantine"
    JSXName = "NumberInput"
    InputName = "value"

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
        decimalSeparator=None,
        formatter=None,
        handlersRef=None,
        hideControls=None,
        m=None,
        max=None,
        mb=None,
        min=None,
        ml=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        noClampOnBlur=None,
        p=None,
        parser=None,
        pb=None,
        pl=None,
        pr=None,
        precision=None,
        pt=None,
        px=None,
        py=None,
        removeTrailingZeros=None,
        startValue=None,
        step=None,
        stepHoldDelay=None,
        stepHoldInterval=None,
        sx=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.decimalSeparator = decimalSeparator
        self.formatter = formatter
        self.handlersRef = handlersRef
        self.hideControls = hideControls
        self.m = m
        self.max = max
        self.mb = mb
        self.min = min
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.noClampOnBlur = noClampOnBlur
        self.p = p
        self.parser = parser
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.precision = precision
        self.pt = pt
        self.px = px
        self.py = py
        self.removeTrailingZeros = removeTrailingZeros
        self.startValue = startValue
        self.step = step
        self.stepHoldDelay = stepHoldDelay
        self.stepHoldInterval = stepHoldInterval
        self.sx = sx
        self.type = type
        assert id is None or isinstance(id, str)
