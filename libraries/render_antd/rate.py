from render import Component, create_callback


class Rate(Component):
    Module = "ant"
    JSXName = "Rate"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        allowClear=None,
        allowHalf=None,
        autoFocus=None,
        character=None,
        count=None,
        defaultValue=None,
        disabled=None,
        onBlur=None,
        onChange=None,
        onFocus=None,
        onHoverChange=None,
        onKeyDown=None,
        tooltips=None,
        value=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.allowClear = allowClear
        self.allowHalf = allowHalf
        self.autoFocus = autoFocus
        self.character = character
        self.count = count
        self.defaultValue = defaultValue
        self.disabled = disabled
        self.onBlur = create_callback(onBlur, "onBlur", [])
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.onFocus = create_callback(onFocus, "onFocus", [])
        self.onHoverChange = create_callback(onHoverChange, "onHoverChange", [[0]])
        self.onKeyDown = create_callback(onKeyDown, "onKeyDown", [])
        self.tooltips = tooltips
        self.value = value
