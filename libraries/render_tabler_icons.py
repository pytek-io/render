from render import Component


class Icon(Component):
    Module = "tabler_icons"
    ATTRIBUTES = ["style", "className", "id", "size", "stroke"]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        size=None,
        id=None,
        stroke=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.size = size
        self.stroke = stroke
        assert id is None or isinstance(id, str)


class IconCheck(Icon):
    pass


class IconGauge(Icon):
    pass


class IconCookie(Icon):
    pass


class IconUser(Icon):
    pass


class IconMessage2(Icon):
    pass


class IconLock(Icon):
    pass


class TablerIcon(Icon):
    pass


class IconChevronDown(Icon):
    pass


class IconTimeline(Icon):
    pass


class IconDeviceDesktop(Icon):
    pass


class IconChartInfographic(Icon):
    pass


class IconSettings(Icon):
    pass


class IconApps(Icon):
    pass


class IconCloudComputing(Icon):
    pass


class IconArrowLeft(Icon):
    pass


class IconArrowRight(Icon):
    pass


class IconPuzzle2(Icon):
    pass


class IconExternalLink(Icon):
    pass
