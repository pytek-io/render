from render import Component, create_callback


class Progress(Component):
    Module = "ant"
    JSXName = "Progress"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "format",
        "gapDegree",
        "gapPosition",
        "percent",
        "showInfo",
        "size",
        "status",
        "steps",
        "strokeColor",
        "strokeLinecap",
        "strokeWidth",
        "success",
        "trailColor",
        "type",
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
        format=None,
        gapDegree=None,
        gapPosition=None,
        percent=None,
        showInfo=None,
        size=None,
        status=None,
        steps=None,
        strokeColor=None,
        strokeLinecap=None,
        strokeWidth=None,
        success=None,
        trailColor=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.format = format
        self.gapDegree = gapDegree
        self.gapPosition = gapPosition
        self.percent = percent
        self.showInfo = showInfo
        self.size = size
        self.status = status
        self.steps = steps
        self.strokeColor = strokeColor
        self.strokeLinecap = strokeLinecap
        self.strokeWidth = strokeWidth
        self.success = success
        self.trailColor = trailColor
        self.type = type
