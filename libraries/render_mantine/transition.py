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
        "keepMounted",
        "mounted",
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
        keepMounted=None,
        mounted=None,
        onEnter=None,
        onEntered=None,
        onExit=None,
        onExited=None,
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
        self.keepMounted = keepMounted
        self.mounted = mounted
        self.onEnter = create_callback(onEnter, "onEnter")
        self.onEntered = create_callback(onEntered, "onEntered")
        self.onExit = create_callback(onExit, "onExit")
        self.onExited = create_callback(onExited, "onExited")
        self.timingFunction = timingFunction
        self.transition = transition
