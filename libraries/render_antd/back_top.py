from render import create_callback, Component, InputComponent


class BackTop(Component):
    Module = "ant"
    JSXName = "BackTop"

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
        target=None,
        visibilityHeight=None,
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
        self.target = target
        self.visibilityHeight = visibilityHeight
        assert id is None or isinstance(id, str)
