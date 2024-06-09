from render import Component


class Prism(Component):
    Module = "mantine_prism"
    ATTRIBUTES = ["language", "withLineNumbers", "className", "style"]

    def __init__(
        self,
        children=None,
        language="python",
        withLineNumbers=False,
        desc=None,
        className=None,
        style=None,
    ):
        super().__init__(key=desc, children=children)
        # removing trailing empty line as it usually takes up space unnecessarily
        if isinstance(children, str) and children.endswith("\n"):
            children = children[:-1]
        self.language = language
        self.withLineNumbers = withLineNumbers
        self.className = className
        self.style = style
