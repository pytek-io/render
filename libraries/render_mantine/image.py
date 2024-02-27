from render import Component, create_callback, add_data_namespace


class Image(Component):
    Module = "mantine"
    JSXName = "Image"
    CALLBACKS = ["onKeyPress", "onClick", "onError"]
    DATA = ["src"]
    ATTRIBUTES = ["style", "className", "id", "fallbackSrc", "fit", "radius"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        fallbackSrc=None,
        fit=None,
        onError=None,
        radius=None,
        src=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.fallbackSrc = fallbackSrc
        self.fit = fit
        self.onError = create_callback(onError, "onError")
        self.radius = radius
        self.src = add_data_namespace(src)
