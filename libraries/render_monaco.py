from render import Component


class Editor(Component):
    Module = "monaco"
    JSXName = "Editor"
    REF_HOOK = "onMount"

    def __init__(
        self,
        height=None,
        defaultLanguage="python",
        defaultValue="# some comment",
        style=None,
        options=None,
        desc=None,
        debug=False,
    ):
        super().__init__(desc, debug)
        self.height = height
        self.defaultLanguage = defaultLanguage
        self.defaultValue = defaultValue
        self.options = options
        self.style = style

    async def getValue(self):
        return await self.call_method("getValue", ())
