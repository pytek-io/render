from enum import Enum
from itertools import count

from render import (
    Component,
    create_callback,
    register_css_for_module,
)

register_css_for_module("rc-dock", "/static/rc-dock.css", "anonymous")


class DropDirection(Enum):
    LEFT = "left"
    RIGHT = "right"
    BOTTOM = "bottom"
    TOP = "top"
    MIDDLE = "middle"
    REMOVE = "remove"
    BEFORE_TAB = "before-tab"
    AFTER_TAB = "after-tab"
    FLOAT = "float"
    FRONT = "front"
    MAXIMIZE = "maximize"
    NEW_WINDOW = "new-window"
    MOVE = "move"
    ACTIVE = "active"
    UPDATE = "update"


class DockLayout(Component):
    REF_HOOK = "ref"
    Module = "rc-dock"

    def __init__(
        self,
        children=None,
        style=None,
        className=None,
        id=None,
        key=None,
        onKeyPress=None,
        defaultLayout=None,
        desc=None,
        componentDidMount=None,
    ):
        super().__init__(key=desc, componentDidMount=componentDidMount)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress)
        self.defaultLayout = defaultLayout

    async def dockMove(self, *args):
        return await self.call_method("dockMove", args)

    async def saveLayout(self):
        return await self.call_method("saveLayout", ())

    async def loadLayout(self, layout):
        return await self.call_method("loadLayout", (layout,))
