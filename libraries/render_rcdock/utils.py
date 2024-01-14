import render_html as html
import render as r
from render_utils import create_icon, MORE_MENU
import render_antd.utils as antd_utils
from itertools import count

from render import Component, get_window
from .components import DockLayout, DropDirection


COUNTER = count()
LIGHT_GREY = "#dddddd"


DEFAULT_ICON_STYLE = {
    "display": "inline-block",
    "lineHeight": "1",
    "textAlign": "center",
    "fontStyle": "normal",
    "textTransform": "none",
    "display": "inline-block",
    "verticalAlign": "-0.125em",
    "cursor": "pointer",
}


def find_first_tab_panel(description):
    if "tabs" in description:
        return description["id"]
    for child in description["children"]:
        result = find_first_tab_panel(child)
        if result:
            return result


class TabWithSettings(r.Window):
    def __init__(
        self,
        window: r.Window,
        title,
        content,
        settings,
        settings_visible,
        ok,
        cancel,
    ):
        self.window = window
        self.content = content(self) if callable(content) else content
        if settings:
            toggle_visible, menu_window = antd_utils.create_settings_window(
                settings, ok=ok, cancel=cancel, menu_visible=settings_visible
            )

            self.title = html.div(
                [
                    create_icon(
                        MORE_MENU,
                        onClick=toggle_visible,
                        style=DEFAULT_ICON_STYLE,
                        className="dock-tab-settings-btn",
                    ),
                    title,
                ],
            )
            self.content = html.div(
                [menu_window, self.content], style={"height": "100%", "width": "100%"}
            )
        else:
            self.title = title


class DockLayoutRender(DockLayout):
    JSXName = "DockLayout"

    def __init__(
        self,
        children=None,
        style=None,
        className=None,
        id=None,
        key=None,
        onKeyPress=None,
        defaultLayout=None,
    ):
        self._counter = count()
        self._contents = []
        self._window = get_window

        def create_layout(component):
            if not isinstance(component, dict):
                return self.create_tab(component)
            result = component
            for name in ["children", "tabs"]:
                elements = result.get(name, None)
                if elements:
                    result[name] = [create_layout(element) for element in elements]
            return result

        super().__init__(
            children=children,
            style=style,
            className=className,
            id=id,
            key=key,
            onKeyPress=onKeyPress,
            defaultLayout={"dockbox": create_layout(defaultLayout["dockbox"])},
        )

    def wrap_content(self, content, title, className=None, cached=True, closable=True):
        """
        Parameters:
        cached: Will cause the rc dock not to dismount a component when it becomes no longer visible.
        """
        return {
            "id": str(next(self._counter)),
            "title": title,
            "content": html.div(
                content,
                style={
                    "height": "inherit",
                    "width": "inherit",
                },
                className=className,
            ),
            "cached": cached,
            "closable": closable,
        }

    def create_tab(
        self,
        component,
        settings_visible=False,
        closeable=True,
    ):
        title, content, settings = [
            getattr(component, name, None)
            for name in (
                "title",
                "content",
                "settings",
            )
        ]
        if settings:
            tab_with_settings = TabWithSettings(
                self._window(),
                title,
                content,
                settings,
                settings_visible,
                getattr(component, "ok", None),
                getattr(component, "cancel", None),
            )
            content, title = tab_with_settings.content, tab_with_settings.title
        else:
            if content is None or title is None:
                title, content = component
            title = html.div(title) if not isinstance(title, Component) else title
            content = html.div(content, style={"height": "inherit", "width": "inherit"})
        # keeping those objects alive
        self._contents.append((title, content))
        return self.wrap_content(content, title, closable=closeable)

    async def insert_component(
        self,
        content,
        settings_visible=False,
    ):
        # rmk: saveLayout is a bit of a misnomer as it only dumps a text representation of the layout
        # (which can be restored later on obviously)
        await self.dockMove(
            self.create_tab(content, settings_visible),
            find_first_tab_panel((await self.saveLayout())["dockbox"]),
            DropDirection.MIDDLE,
        )


def create_tab(title, content):
    return {
        "id": str(next(COUNTER)),
        "title": title,
        "content": content,
        "cached": True,
        "closable": True,
        "minWidth": 300,
        "minHeight": 400,
    }


def create_tab_inserter(dock_layout):
    async def result(title, content):
        # rmk: saveLayout is a bit of a misnomer as it only dumps a text representation of the layout
        # (which can be restored later on obviously)
        panel_id = (await dock_layout.saveLayout())["dockbox"]["children"][0]["id"]
        await dock_layout.dockMove(create_tab(title, content), panel_id, DropDirection.MIDDLE)

    return result
