from render import create_callback, Component, InputComponent


class MantineProvider(Component):
    Module = "mantine"
    JSXName = "MantineProvider"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        emotionCache=None,
        inherit=None,
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
        sx=None,
        theme=None,
        withCSSVariables=None,
        withGlobalStyles=None,
        withNormalizeCSS=None,
        styles=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.emotionCache = emotionCache
        self.inherit = inherit
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
        self.sx = sx
        self.theme = theme
        self.withCSSVariables = withCSSVariables
        self.withGlobalStyles = withGlobalStyles
        self.withNormalizeCSS = withNormalizeCSS
        self.styles = styles
        assert id is None or isinstance(id, str)
