from render import Component, create_callback, InputComponent


class Slider(InputComponent):
    Module = "antd"
    JSXName = "Slider"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onAfterChange"]
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
        onChange=None,
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
        onAfterChange=None,
        open=None,
        placement=None,
        range=None,
        reverse=None,
        step=None,
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
        self.onAfterChange = create_callback(onAfterChange, "onAfterChange", [[0]])
        self.open = open
        self.placement = placement
        self.range = range
        self.reverse = reverse
        self.step = step
        self.tooltip = tooltip
        self.vertical = vertical
