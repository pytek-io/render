from render import Component, create_callback


class Appear(Component):
    Module = "spectacle"
    JSXName = "Appear"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "activeStyle",
        "inactiveStyle",
        "stepIndex",
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
        activeStyle=None,
        inactiveStyle=None,
        stepIndex=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.activeStyle = activeStyle
        self.inactiveStyle = inactiveStyle
        self.stepIndex = stepIndex


class Box(Component):
    Module = "spectacle"
    JSXName = "Box"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "border",
        "color",
        "layout",
        "position",
        "space",
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
        border=None,
        color=None,
        layout=None,
        position=None,
        space=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.border = border
        self.color = color
        self.layout = layout
        self.position = position
        self.space = space


class CodePane(Component):
    Module = "spectacle"
    JSXName = "CodePane"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "highlightRanges", "language", "theme"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        highlightRanges=None,
        language=None,
        theme=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.highlightRanges = highlightRanges
        self.language = language
        self.theme = theme


class CodeSpan(Component):
    Module = "spectacle"
    JSXName = "CodeSpan"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "fontFamily",
        "fontSize",
        "space",
        "typography",
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
        color=None,
        fontFamily="monospace",
        fontSize="text",
        space=None,
        typography=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.space = space
        self.typography = typography


class Deck(Component):
    Module = "spectacle"
    JSXName = "Deck"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "autoPlay",
        "autoPlayInterval",
        "autoPlayLoop",
        "pageOrientation",
        "pageSize",
        "printScale",
        "template",
        "theme",
        "transition",
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
        autoPlay=None,
        autoPlayInterval=None,
        autoPlayLoop=None,
        pageOrientation=None,
        pageSize=None,
        printScale=None,
        template=None,
        theme=None,
        transition=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.autoPlay = autoPlay
        self.autoPlayInterval = autoPlayInterval
        self.autoPlayLoop = autoPlayLoop
        self.pageOrientation = pageOrientation
        self.pageSize = pageSize
        self.printScale = printScale
        self.template = template
        self.theme = theme
        self.transition = transition


class FlexBox(Component):
    Module = "spectacle"
    JSXName = "FlexBox"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "alignItems",
        "border",
        "color",
        "display",
        "flexDirection",
        "flexbox",
        "height",
        "justifyContent",
        "layout",
        "position",
        "space",
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
        alignItems="center",
        border=None,
        color=None,
        display="flex",
        flexDirection="column",
        flexbox=None,
        height=None,
        justifyContent="center",
        layout=None,
        position=None,
        space=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.alignItems = alignItems
        self.border = border
        self.color = color
        self.display = display
        self.flexDirection = flexDirection
        self.flexbox = flexbox
        self.height = height
        self.justifyContent = justifyContent
        self.layout = layout
        self.position = position
        self.space = space


class Grid(Component):
    Module = "spectacle"
    JSXName = "Grid"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "display", "grid", "layout", "position"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        display="grid",
        grid=None,
        layout=None,
        position=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.display = display
        self.grid = grid
        self.layout = layout
        self.position = position


class Heading(Component):
    Module = "spectacle"
    JSXName = "Heading"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "fontFamily",
        "fontSize",
        "fontWeight",
        "margin",
        "textAlign",
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
        color="secondary",
        fontFamily="header",
        fontSize="h1",
        fontWeight="bold",
        margin=1,
        textAlign="center",
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight
        self.margin = margin
        self.textAlign = textAlign


class ListItem(Component):
    Module = "spectacle"
    JSXName = "ListItem"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = ["style", "className", "id", "color", "margin", "space", "typography"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        color=None,
        margin=0,
        space=None,
        typography=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.margin = margin
        self.space = space
        self.typography = typography


class Slide(Component):
    Module = "spectacle"
    JSXName = "Slide"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "backgroundColor",
        "backgroundImage",
        "backgroundOpacity",
        "backgroundPosition",
        "backgroundRepeat",
        "backgroundSize",
        "scaleRatio",
        "slideNum",
        "template",
        "textColor",
        "transition",
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
        backgroundColor=None,
        backgroundImage=None,
        backgroundOpacity=None,
        backgroundPosition=None,
        backgroundRepeat=None,
        backgroundSize=None,
        scaleRatio=None,
        slideNum=None,
        template=None,
        textColor=None,
        transition=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.backgroundColor = backgroundColor
        self.backgroundImage = backgroundImage
        self.backgroundOpacity = backgroundOpacity
        self.backgroundPosition = backgroundPosition
        self.backgroundRepeat = backgroundRepeat
        self.backgroundSize = backgroundSize
        self.scaleRatio = scaleRatio
        self.slideNum = slideNum
        self.template = template
        self.textColor = textColor
        self.transition = transition


class UnorderedList(Component):
    Module = "spectacle"
    JSXName = "UnorderedList"
    CALLBACKS = ["onKeyPress", "onClick"]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "fontFamily",
        "fontSize",
        "listStyle",
        "margin",
        "space",
        "textAlign",
        "typography",
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
        color="primary",
        fontFamily="text",
        fontSize="text",
        listStyle=None,
        margin=0,
        space=None,
        textAlign="left",
        typography=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.listStyle = listStyle
        self.margin = margin
        self.space = space
        self.textAlign = textAlign
        self.typography = typography
