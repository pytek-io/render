from render import Component


class Chart(Component):
    Module = "altair"
    ATTRIBUTES = ["spec", "actions", "style", "signalListeners"]

    def __init__(
        self,
        spec,
        desc=None,
        actions=False,
        signalListeners=None,
        style=None,
    ):
        super().__init__(desc)
        if callable(spec):
            original_spec = spec
            spec = lambda: original_spec().to_dict()
        elif hasattr(spec, "to_dict"):
            spec = spec.to_dict()
        self.spec = spec
        self.actions = actions
        self.style = style
        self.signalListeners = signalListeners
