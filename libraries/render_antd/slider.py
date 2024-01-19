from render import Component, create_callback, InputComponent


class Slider(InputComponent):
    Module = "antd"
    JSXName = "Slider"
    InputName = "value"
    ChangeEventName = "onAfterChange"
    CALLBACKS = ["onKeyPress", "onClick", "onChange"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoAdjustOverflow",
        "autoFocus",
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
        onAfterChange=None,
        defaultValue=None,
        value=None,
        autoAdjustOverflow=None,
        autoFocus=None,
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
        onChange=None,
        open=None,
        placement=None,
        range=None,
        reverse=None,
        step=None,
        tooltip=None,
        vertical=None,
        controller=None,
    ):
        super().__init__(key, controller, onAfterChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoAdjustOverflow = autoAdjustOverflow
        self.autoFocus = autoFocus
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
        self.onChange = create_callback(onChange, "onChange", [[0]])
        self.open = open
        self.placement = placement
        self.range = range
        self.reverse = reverse
        self.step = step
        self.tooltip = tooltip
        self.vertical = vertical
