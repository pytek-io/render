from .components import Component, create_callback

DEFAULT_ARGS_NO_CHILDREN_NAMES = ["style", "className", "id", "onKeyPress"]


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
            componentDidMount=componentDidMount,
            componentWillUnmount=componentWillUnmount,
        )
        self.className = className
        self.style = style
        assert self.CHILDREN_CAN_BE_EMPTY or children, "Containers must have one child at least"
        self.children = children
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
