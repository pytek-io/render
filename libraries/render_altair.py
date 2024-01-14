from render import Component


class Chart(Component):
    Module = "altair"

    def __init__(
        self,
        spec,
        desc=None,
        debug=False,
        actions=False,
        signalListeners=None,
        style=None,
    ):
        super().__init__(desc, debug)
        self.spec = (lambda: spec().to_dict()) if callable(spec) else spec.to_dict()
        self.actions = actions
        self.style = style
        self.signalListeners = signalListeners
