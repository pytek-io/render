from render import Component, create_callback, InputComponent


class Switch(InputComponent):
    Module = "ant"
    JSXName = "Switch"
    InputName = "checked"

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
        autoFocus=None,
        checkedChildren=None,
        disabled=None,
        loading=None,
        size=None,
        unCheckedChildren=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, checked, defaultChecked)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick", [[0]])
        self.autoFocus = autoFocus
        self.checkedChildren = checkedChildren
        self.disabled = disabled
        self.loading = loading
        self.size = size
        self.unCheckedChildren = unCheckedChildren
