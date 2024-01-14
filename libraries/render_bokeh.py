from render import Component
from bokeh.embed import json_item


class Figure(Component):
    Module = "bokeh"

    def __init__(
        self,
        figure,
        desc=None,
    ):
        super().__init__(key=desc)
        self.options = json_item(figure, "myplot")
