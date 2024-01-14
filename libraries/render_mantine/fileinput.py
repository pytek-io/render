from render import create_callback, Component, InputComponent


class FileInput(InputComponent):
    Module = "mantine"
    JSXName = "FileInput"
    InputName = "value"
    NewValuePath = "name"

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
        accept=None,
        clearButtonLabel=None,
        clearButtonTabIndex=None,
        clearable=None,
        form=None,
        m=None,
        mb=None,
        ml=None,
        mr=None,
        mt=None,
        multiple=None,
        mx=None,
        my=None,
        name=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        size=None,
        sx=None,
        valueComponent=None,
        wrapperProps=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.accept = accept
        self.clearButtonLabel = clearButtonLabel
        self.clearButtonTabIndex = clearButtonTabIndex
        self.clearable = clearable
        self.form = form
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.mt = mt
        self.multiple = multiple
        self.mx = mx
        self.my = my
        self.name = name
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.size = size
        self.sx = sx
        self.valueComponent = valueComponent
        self.wrapperProps = wrapperProps
        assert id is None or isinstance(id, str)
