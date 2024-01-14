from render import Component


class PrismCodeFormatter(Component):
    Module = "prism"

    def __init__(
        self,
        code=None,
        language="python",
        theme=None,
        lineNumbers=False,
        style=None,
        debug=False,
        desc=None,
    ):
        super().__init__(key=desc)
        # removing trailing empty line as it usually takes up space unnecessarily
        if isinstance(code, str) and code.endswith("\n"):
            code = code[:-1]
        self.code = code
        self.language = language
        self.theme = theme
        self.lineNumbers = lineNumbers
        self.style = style
