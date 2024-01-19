from render import create_callback, Component


class Appear(Component):
    Module = "spectacle"
    JSXName = "Appear"
    ATTRIBUTES = ["style", "className", "activeStyle", "inactiveStyle", "stepIndex", "id"]
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        activeStyle=None,
        inactiveStyle=None,
        stepIndex=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.activeStyle = activeStyle
        self.inactiveStyle = inactiveStyle
        self.stepIndex = stepIndex
        assert id is None or isinstance(id, str)


class Box(Component):
    Module = "spectacle"
    JSXName = "Box"
    ATTRIBUTES = ["style", "className", "id", "border", "color", "layout", "position", "space"]
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        border=None,
        color=None,
        layout=None,
        position=None,
        space=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.border = border
        self.color = color
        self.layout = layout
        self.position = position
        self.space = space
        assert id is None or isinstance(id, str)


class CodePane(Component):
    Module = "spectacle"
    JSXName = "CodePane"
    ATTRIBUTES = ["style", "className", "id", "highlightRanges", "language", "theme"]
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        highlightRanges=None,
        language=None,
        theme=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.highlightRanges = highlightRanges
        self.language = language
        self.theme = theme
        assert id is None or isinstance(id, str)


class CodeSpan(Component):
    Module = "spectacle"
    JSXName = "CodeSpan"
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "color",
        "fontSize",
        "fontFamily",
        "fontSize",
        "space",
        "typography",
    ]
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        color=None,
        fontFamily=None,
        fontSize=None,
        space=None,
        typography=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.space = space
        self.typography = typography
        assert id is None or isinstance(id, str)


class Deck(Component):
    Module = "spectacle"
    JSXName = "Deck"
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
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
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
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.autoPlay = autoPlay
        self.autoPlayInterval = autoPlayInterval
        self.autoPlayLoop = autoPlayLoop
        self.pageOrientation = pageOrientation
        self.pageSize = pageSize
        self.printScale = printScale
        self.template = template
        self.theme = theme
        self.transition = transition
        assert id is None or isinstance(id, str)


class FlexBox(Component):
    Module = "spectacle"
    JSXName = "FlexBox"
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
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        alignItems=None,
        border=None,
        color=None,
        display=None,
        flexDirection=None,
        flexbox=None,
        height=None,
        justifyContent=None,
        layout=None,
        position=None,
        space=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
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
        assert id is None or isinstance(id, str)


class Grid(Component):
    Module = "spectacle"
    JSXName = "Grid"
    ATTRIBUTES = ["style", "className", "id", "display", "grid", "layout", "position"]
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        display=None,
        grid=None,
        layout=None,
        position=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.display = display
        self.grid = grid
        self.layout = layout
        self.position = position
        assert id is None or isinstance(id, str)


class Heading(Component):
    Module = "spectacle"
    JSXName = "Heading"
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
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        color=None,
        fontFamily=None,
        fontSize=None,
        fontWeight=None,
        margin=None,
        textAlign=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontWeight = fontWeight
        self.margin = margin
        self.textAlign = textAlign
        assert id is None or isinstance(id, str)


class ListItem(Component):
    Module = "spectacle"
    JSXName = "ListItem"
    ATTRIBUTES = ["style", "className", "id", "color", "margin", "space", "typography"]
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        color=None,
        margin=None,
        space=None,
        typography=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.color = color
        self.margin = margin
        self.space = space
        self.typography = typography
        assert id is None or isinstance(id, str)


class Slide(Component):
    Module = "spectacle"
    JSXName = "Slide"
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
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
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
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
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
        assert id is None or isinstance(id, str)


class UnorderedList(Component):
    Module = "spectacle"
    JSXName = "UnorderedList"
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
    CALLBACKS = ["onKeyPress"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        color=None,
        fontFamily=None,
        fontSize=None,
        listStyle=None,
        margin=None,
        space=None,
        textAlign=None,
        typography=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.listStyle = listStyle
        self.margin = margin
        self.space = space
        self.textAlign = textAlign
        self.typography = typography
        assert id is None or isinstance(id, str)
