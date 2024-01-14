from render import Component


class Icon(Component):
    Module = "iconify"

    def __init__(
        self,
        desc=None,
        debug=False,
        icon=None,
        width=None,
        height=None,
        color=None,
        style=None,
    ):
        super().__init__(desc, debug)
        self.icon = icon
        self.width = width
        self.height = height
        self.color = color
        self.style = style


class InlineIcon(Icon):
    pass
