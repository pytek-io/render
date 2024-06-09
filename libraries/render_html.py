from render import Component, create_callback, add_data_namespace


class Container(Component):
    Module = "html"
    REF_HOOK = "ref"
    CHILDREN_CAN_BE_EMPTY = True
    ATTRIBUTES = ["id", "className", "style", "size", "role", "ariaLabel"]
    CALLBACKS = ["onClick", "onScroll"]

    def __init__(
        self,
        children=None,
        key=None,
        id=None,
        className=None,
        style=None,
        size=None,
        onClick=None,
        onScroll=None,
        role=None,
        ariaLabel=None,
        custom_attributes=None,
        componentDidMount=None,
        componentWillUnmount=None,
    ):
        super().__init__(
            key=key,
            children=children,
            componentDidMount=componentDidMount,
            componentWillUnmount=componentWillUnmount,
        )
        self.className = className
        self.style = style
        assert self.CHILDREN_CAN_BE_EMPTY or children, "Containers must have one child at least"
        assert not isinstance(id, int), id
        self.id = id
        self.onClick = create_callback(onClick)
        self.onScroll = create_callback(onScroll)
        self.role = role
        self.ariaLabel = ariaLabel
        self.size = size
        self.custom_attributes = custom_attributes

    async def scrollIntoView(self):
        return await self.call_method("scrollIntoView", ())

    async def scrollTo(self, x, y):
        return await self.call_method("scrollTo", (x, y))


class Tag(Component):
    def __init__(
        self,
        children=None,
        id=None,
        className=None,
        style=None,
        onClick=None,
        role=None,
        ariaLabel=None,
    ):
        super().__init__()
        self.className = className
        self.style = style
        assert not children, "Tags cannot have children"
        self.id = id
        self.onClick = create_callback(onClick)
        self.role = role
        self.ariaLabel = ariaLabel


class ServerErrorTraceback(Component):
    Module = "html"

    def __init__(self, traceback):
        super().__init__()
        self.traceback = traceback


class label(Container):
    Module = "html"


class Link(Component):
    Module = "html"
    ATTRIBUTES = ["style", "className", "id", "href", "target", "rel", "title", "download"]
    CALLBACKS = ["onClick"]

    def __init__(
        self,
        children=None,
        style=None,
        className=None,
        id=None,
        href=None,
        target=None,
        onClick=None,
        rel=None,
        title=None,
        download=None,
        key=None,
    ):
        super().__init__(key, children=children)
        self.style = style
        self.className = className
        self.id = id
        self.href = href
        self.target = target
        self.rel = rel
        self.title = title
        self.download = download
        self.onClick = create_callback(onClick)


# rmk: we should factor out those two classes
class svg(Component):
    Module = "html"
    ATTRIBUTES = ["width", "height", "fill", "viewBox", "style", "preserveAspectRatio"]
    CALLBACKS = ["onClick"]

    def __init__(
        self,
        children=None,
        width=None,
        height=None,
        fill=None,
        viewBox=None,
        key=None,
        style=None,
        onClick=None,
        preserveAspectRatio=None,
    ):
        super().__init__(key=key, children=children)
        self.width = width
        self.height = height
        self.fill = fill
        self.viewBox = viewBox
        self.style = style
        self.preserveAspectRatio = (preserveAspectRatio,)
        self.onClick = create_callback(onClick)


class img(Component):
    Module = "html"
    ATTRIBUTES = ["src", "dataSrc", "className", "width", "alt", "onClick", "style"]
    CALLBACKS = ["onClick"]

    def __init__(
        self,
        src=None,
        dataSrc=None,
        className=None,
        width=None,
        alt=None,
        onClick=None,
        style=None,
        desc=None,
        custom_attributes=None,
    ):
        super().__init__(desc)
        self.className = className
        self.alt = alt
        self.src = add_data_namespace(src)
        self.dataSrc = add_data_namespace(dataSrc)
        self.width = width
        self.style = style
        self.onClick = create_callback(onClick)
        self.custom_attributes = custom_attributes


class path(Component):
    Module = "html"
    ATTRIBUTES = ["d", "fill", "p_id", "style"]

    def __init__(self, d=None, fill=None, p_id=None, desc=None, style=None):
        super().__init__(desc)
        self.d = d
        self.fill = fill
        self.p_id = p_id
        self.style = style


class circle(Component):
    Module = "html"
    ATTRIBUTES = ["cx", "cy", "r", "fill", "onClick"]

    def __init__(
        self,
        key=None,
        cx=None,
        cy=None,
        r=None,
        fill=None,
        controller=None,
        componentDidMount=None,
        componentWillUnmount=None,
        onClick=None,
    ):
        super().__init__(key, controller, componentDidMount=componentDidMount, componentWillUnmount=componentWillUnmount)
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = fill
        self.onClick = create_callback(onClick)


class inline_svg(Container):
    Module = "html"

    def __init__(
        self,
        children=None,
        key=None,
        id=None,
        className=None,
        style=None,
        size=None,
        onClick=None,
        onScroll=None,
        role=None,
        ariaLabel=None,
        custom_attributes=None,
        componentDidMount=None,
        componentWillUnmount=None,
        **kwargs
    ):
        super().__init__(
            children,
            key,
            id,
            className,
            style,
            size,
            onClick,
            onScroll,
            role,
            ariaLabel,
            custom_attributes,
            componentDidMount,
            componentWillUnmount,
            **kwargs
        )


class inline_png(Container):
    Module = "html"

    def __init__(
        self,
        children=None,
        key=None,
        id=None,
        className=None,
        style=None,
        size=None,
        onClick=None,
        onScroll=None,
        role=None,
        ariaLabel=None,
        custom_attributes=None,
        componentDidMount=None,
        componentWillUnmount=None,
        **kwargs
    ):
        super().__init__(
            children,
            key,
            id,
            className,
            style,
            size,
            onClick,
            onScroll,
            role,
            ariaLabel,
            custom_attributes,
            componentDidMount,
            componentWillUnmount,
            **kwargs
        )


class del_(Container):
    JSXName = "del"


class iframe(Container):
    pass


class h1(Container):
    pass


class h2(Container):
    pass


class h3(Container):
    pass


class h4(Container):
    pass


class h5(Container):
    pass


class h6(Container):
    pass


class div(Container):
    pass


class section(Container):
    pass


class article(Container):
    pass


class br(Container):
    pass


class ul(Container):
    pass


class li(Container):
    pass


class ol(Container):
    pass


class a(Link):
    JSXName = "a"


class b(Link):
    pass


class i(Link):
    pass


class p(Link):
    pass


class span(Container):
    pass


class code(Container):
    pass


class header(Container):
    pass


class strong(Container):
    pass


class blockquote(Container):
    pass


class pre(Container):
    pass


class style(Container):
    pass


class tr(Container):
    pass


class hr(Container):
    pass


class td(Container):
    pass


class th(Container):
    pass


class thead(Container):
    pass


class tbody(Container):
    pass


class head(Container):
    pass


class body(Container):
    pass


class em(Container):
    pass


class html(Container):
    pass


class u(Container):
    pass
