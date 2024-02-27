from render import Component, create_callback, Props


class FileButton(Component):
    Module = "mantine"
    JSXName = "FileButton"
    CALLBACKS = ["children", "onKeyPress", "onClick", "onChange", "resetRef"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "accept",
        "capture",
        "disabled",
        "form",
        "inputProps",
        "multiple",
        "name",
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
        accept=None,
        capture=None,
        disabled=None,
        form=None,
        inputProps=None,
        multiple=None,
        name=None,
        onChange=None,
        resetRef=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = create_callback(children, "children")
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.accept = accept
        self.capture = capture
        self.disabled = disabled
        self.form = form
        self.inputProps = inputProps
        self.multiple = multiple
        self.name = name
        self.onChange = create_callback(onChange, "onChange")
        self.resetRef = create_callback(resetRef, "resetRef")
