from render import Component, create_callback, InputComponent


class Slider(InputComponent):
    Module = "antd"
    JSXName = "Slider"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeComplete"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoAdjustOverflow",
        "autoFocus",
        "classNames",
        "disabled",
        "dots",
        "draggableTrack",
        "formatter",
        "getPopupContainer",
        "included",
        "keyboard",
        "marks",
        "max",
        "min",
        "open",
        "placement",
        "range",
        "reverse",
        "step",
        "styles",
        "tooltip",
        "vertical",
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
        onChange=None,
        defaultValue=None,
        value=None,
        autoAdjustOverflow=None,
        autoFocus=None,
        classNames=None,
        disabled=None,
        dots=None,
        draggableTrack=None,
        formatter=None,
        getPopupContainer=None,
        included=None,
        keyboard=None,
        marks=None,
        max=None,
        min=None,
        onChangeComplete=None,
        open=None,
        placement=None,
        range=None,
        reverse=None,
        step=None,
        styles=None,
        tooltip=None,
        vertical=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoAdjustOverflow = autoAdjustOverflow
        self.autoFocus = autoFocus
        self.classNames = classNames
        self.disabled = disabled
        self.dots = dots
        self.draggableTrack = draggableTrack
        self.formatter = formatter
        self.getPopupContainer = getPopupContainer
        self.included = included
        self.keyboard = keyboard
        self.marks = marks
        self.max = max
        self.min = min
        self.onChangeComplete = create_callback(
            onChangeComplete, "onChangeComplete", [[0]]
        )
        self.open = open
        self.placement = placement
        self.range = range
        self.reverse = reverse
        self.step = step
        self.styles = styles
        self.tooltip = tooltip
        self.vertical = vertical
