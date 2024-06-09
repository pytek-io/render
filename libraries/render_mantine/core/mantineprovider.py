from render import Component, create_callback


class MantineProvider(Component):
    Module = "mantine/core"
    JSXName = "MantineProvider"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "theme",
        "colorSchemeManager",
        "defaultColorScheme",
        "forceColorScheme",
        "cssVariablesSelector",
        "withCssVariables",
        "deduplicateCssVariables",
        "classNamesPrefix",
        "getStyleNonce",
        "cssVariablesResolver",
        "withStaticClasses",
        "withGlobalClasses",
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
        theme=None,
        colorSchemeManager=None,
        defaultColorScheme=None,
        forceColorScheme=None,
        cssVariablesSelector=None,
        withCssVariables=None,
        deduplicateCssVariables=None,
        classNamesPrefix=None,
        getStyleNonce=None,
        cssVariablesResolver=None,
        withStaticClasses=None,
        withGlobalClasses=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.theme = theme
        self.colorSchemeManager = colorSchemeManager
        self.defaultColorScheme = defaultColorScheme
        self.forceColorScheme = forceColorScheme
        self.cssVariablesSelector = cssVariablesSelector
        self.withCssVariables = withCssVariables
        self.deduplicateCssVariables = deduplicateCssVariables
        self.classNamesPrefix = classNamesPrefix
        self.getStyleNonce = getStyleNonce
        self.cssVariablesResolver = cssVariablesResolver
        self.withStaticClasses = withStaticClasses
        self.withGlobalClasses = withGlobalClasses
