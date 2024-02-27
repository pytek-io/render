from render import Component, create_callback, InputComponent, Props


class RangeSlider(InputComponent):
    Module = "mantine"
    JSXName = "RangeSlider"
    InputName = "value"
    CALLBACKS = ["onKeyPress", "onClick", "onChangeEnd"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "disabled",
        "hiddenInputProps",
        "inverted",
        "label",
        "labelAlwaysOn",
        "labelTransitionProps",
        "marks",
        "max",
        "maxRange",
        "min",
        "minRange",
        "name",
        "precision",
        "radius",
        "scale",
        "showLabelOnHover",
        "size",
        "step",
        "thumbChildren",
        "thumbFromLabel",
        "thumbSize",
        "thumbToLabel",
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
        color=None,
        disabled=None,
        hiddenInputProps=None,
        inverted=None,
        label=None,
        labelAlwaysOn=None,
        labelTransitionProps=None,
        marks=None,
        max=None,
        maxRange=None,
        min=None,
        minRange=None,
        name=None,
        onChangeEnd=None,
        precision=None,
        radius=None,
        scale=None,
        showLabelOnHover=None,
        size=None,
        step=None,
        thumbChildren=None,
        thumbFromLabel=None,
        thumbSize=None,
        thumbToLabel=None,
        controller=None,
    ):
        super().__init__(key, controller, onChange, value, defaultValue)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.disabled = disabled
        self.hiddenInputProps = hiddenInputProps
        self.inverted = inverted
        self.label = label
        self.labelAlwaysOn = labelAlwaysOn
        self.labelTransitionProps = labelTransitionProps
        self.marks = marks
        self.max = max
        self.maxRange = maxRange
        self.min = min
        self.minRange = minRange
        self.name = name
        self.onChangeEnd = create_callback(onChangeEnd, "onChangeEnd")
        self.precision = precision
        self.radius = radius
        self.scale = scale
        self.showLabelOnHover = showLabelOnHover
        self.size = size
        self.step = step
        self.thumbChildren = thumbChildren
        self.thumbFromLabel = thumbFromLabel
        self.thumbSize = thumbSize
        self.thumbToLabel = thumbToLabel
