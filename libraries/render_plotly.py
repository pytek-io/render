from render import create_callback, Component


class Plot(Component):
    Module = "plotly"
    ATTRIBUTES = ["data", "layout", "style", "config", "useResizeHandler", "onUpdate"]
    CALLBACKS = ["onUpdate"]

    def __init__(
        self,
        data=None,
        layout=None,
        onUpdate=None,
        style=None,
        config=None,
        useResizeHandler=None,
        desc=None,
    ):
        super().__init__(key=desc)
        self.data = data
        self.layout = layout
        self.style = style
        self.config = config
        self.useResizeHandler = useResizeHandler
        self.onUpdate = create_callback(onUpdate)


class Graph(Plot):
    Module = "plotly"
    JSXName = "Plot"

    def __init__(self, figure, desc=None):
        super().__init__(desc=desc, **(figure.to_dict() if hasattr(figure, "to_dict") else {}))
