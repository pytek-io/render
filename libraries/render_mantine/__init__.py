import operator
from enum import Enum

from render import Container as ContainerBase

from ._auto import *
from .grid import Col, Grid
from .list import List, ListItem
from .menu import (
    Menu,
    MenuDivider,
    MenuDropdown,
    MenuItem,
    MenuLabel,
    MenuTarget,
)
from .numberinput import NumberInput as NumberInputBase
from .scrollarea import ScrollArea, ScrollAreaAutosize


class ComparableEnum(Enum):
    def __ge__(self, other) -> bool:
        return operator.ge(self.value, other.value)

    def __gt__(self, other) -> bool:
        return operator.gt(self.value, other.value)

    def __le__(self, other) -> bool:
        return operator.le(self.value, other.value)

    def __lt__(self, other) -> bool:
        return operator.lt(self.value, other.value)


class BreakPoint(ComparableEnum):
    xs = 576
    sm = 768
    md = 992
    lg = 1200
    xl = 1400


BREAKPOINTS = dict(
    xs=BreakPoint.xs.value,
    sm=BreakPoint.sm.value,
    md=BreakPoint.md.value,
    lg=BreakPoint.lg.value,
    xl=BreakPoint.xl.value,
)

BREAKPOINTS_VALUES = [
    BreakPoint.xs.value,
    BreakPoint.sm.value,
    BreakPoint.md.value,
    BreakPoint.lg.value,
    BreakPoint.xl.value,
]


class NavbarSection(ContainerBase):
    Module = "mantine"
    JSXName = "Navbar.Section"


Grid.Col = Col
Menu.Divider = MenuDivider
Menu.Dropdown = MenuDropdown
Menu.Item = MenuItem
Menu.Label = MenuLabel
Menu.Target = MenuTarget
List.Item = ListItem
Navbar.Section = NavbarSection
ScrollArea.Autosize = ScrollAreaAutosize


class NumberInput(NumberInputBase):
    def validate(self, new_value):
        return new_value is not None
