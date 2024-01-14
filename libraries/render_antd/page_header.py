from render import create_callback, Component, InputComponent


class PageHeader(Component):
    Module = "ant"
    JSXName = "PageHeader"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        avatar=None,
        backIcon=None,
        breadcrumb=None,
        breadcrumbRender=None,
        extra=None,
        footer=None,
        ghost=None,
        onBack=None,
        subTitle=None,
        tags=None,
        title=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.onClick = create_callback(onClick)
        self.avatar = avatar
        self.backIcon = backIcon
        self.breadcrumb = breadcrumb
        self.breadcrumbRender = create_callback(breadcrumbRender)
        self.extra = extra
        self.footer = footer
        self.ghost = ghost
        self.onBack = create_callback(onBack)
        self.subTitle = subTitle
        self.tags = tags
        self.title = title
        assert id is None or isinstance(id, str)
