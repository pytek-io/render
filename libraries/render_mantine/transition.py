from render import create_callback, Component, InputComponent


class GroupedTransition(Component):
    Module = "mantine"
    JSXName = "GroupedTransition"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        duration=None,
        exitDuration=None,
        m=None,
        mb=None,
        ml=None,
        mounted=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onEnter=None,
        onEntered=None,
        onExit=None,
        onExited=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        timingFunction=None,
        transitions=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.duration = duration
        self.exitDuration = exitDuration
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mounted = mounted
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onEnter = create_callback(onEnter)
        self.onEntered = create_callback(onEntered)
        self.onExit = create_callback(onExit)
        self.onExited = create_callback(onExited)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.timingFunction = timingFunction
        self.transitions = transitions
        assert id is None or isinstance(id, str)


class Transition(Component):
    Module = "mantine"
    JSXName = "Transition"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        duration=None,
        exitDuration=None,
        m=None,
        mb=None,
        ml=None,
        mounted=None,
        mr=None,
        mt=None,
        mx=None,
        my=None,
        onEnter=None,
        onEntered=None,
        onExit=None,
        onExited=None,
        p=None,
        pb=None,
        pl=None,
        pr=None,
        pt=None,
        px=None,
        py=None,
        sx=None,
        timingFunction=None,
        transition=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.duration = duration
        self.exitDuration = exitDuration
        self.m = m
        self.mb = mb
        self.ml = ml
        self.mounted = mounted
        self.mr = mr
        self.mt = mt
        self.mx = mx
        self.my = my
        self.onEnter = create_callback(onEnter)
        self.onEntered = create_callback(onEntered)
        self.onExit = create_callback(onExit)
        self.onExited = create_callback(onExited)
        self.p = p
        self.pb = pb
        self.pl = pl
        self.pr = pr
        self.pt = pt
        self.px = px
        self.py = py
        self.sx = sx
        self.timingFunction = timingFunction
        self.transition = transition
        assert id is None or isinstance(id, str)
