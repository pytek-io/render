from render import Component, create_callback


class Transition(Component):
    Module = "mantine"
    JSXName = "Transition"
    CALLBACKS = ["onKeyPress", "onClick", "onEnter", "onEntered", "onExit", "onExited"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "duration",
        "exitDuration",
        "m",
        "mb",
        "ml",
        "mounted",
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
        "sx",
        "timingFunction",
        "transition",
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
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
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
        self.onEnter = create_callback(onEnter, "onEnter")
        self.onEntered = create_callback(onEntered, "onEntered")
        self.onExit = create_callback(onExit, "onExit")
        self.onExited = create_callback(onExited, "onExited")
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
