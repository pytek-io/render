import render_antd as antd
import render_antd.icon as antd_icon
import render_html as html
from render_utils import HAMBURGER_MENU, create_icon

import render as r
import json
import pathlib
import os


def encode_url(url, args):
    return f"{url}#{json.dumps(args)}"


def create_absolute_path(module_path, relative_path):
    if not relative_path.startswith(os.sep):
        relative_path = os.sep + str(
            pathlib.Path(os.path.join(pathlib.Path(module_path).parent, relative_path))
            .resolve()
            .relative_to(os.getcwd())
        )
    return relative_path


def create_edit_link(file_path, base_path=None, title=None, css=()):
    kwargs = {"main": file_path}
    if css:
        kwargs["css"] = [create_absolute_path(base_path, path) for path in css]
    return html.a(
        antd_icon.Icon(component=r.js("EditSvg")),
        href=encode_url("/app/demos/online_editor", kwargs),
        title=title or "Edit " + file_path,
        className="edit-button",
        target="_blank",
    )


def make_editable(component, file_path):
    edit_logo = html.span(
        create_edit_link(file_path),
        className="anticon anticon-edit",
        style={
            "position": "absolute",
            "top": "0.2em",
            "right": "1.0em",
            "width": "1em",
            "height": "1em",
            "opacity": ".3",
            "transition": "opacity 0.5s",
            "border": None,
            "userSelect": None,
        },
    )
    return html.div([edit_logo, component], style={"position": "relative"})


def create_settings_window(settings, ok, cancel, menu_visible=False):
    menu_visible = r.ObservableValue(menu_visible, key="settings_visible")

    def create_menu_callback(callback):
        async def result():
            menu_visible.set(False)
            if callback:
                await r.call_maybe_coroutine(callback)

        return result

    return lambda: menu_visible.set(True), antd.Modal(
        settings,
        open=menu_visible,
        onOk=create_menu_callback(ok),
        onCancel=create_menu_callback(cancel),
        width=600,
        cancelButtonProps=None if cancel else {"style": {"display": "none"}},
    )


def create_app(app_class):
    def result(window: r.Window):
        app = app_class(window)
        content = app.content
        if callable(content):
            content = content()
        if title := getattr(app, "title", None):
            window.set_title(title)
        settings = getattr(app, "settings", None)
        if settings:
            toggle_visible, menu_window = create_settings_window(
                settings, ok=getattr(app, "ok", None), cancel=getattr(app, "cancel", None)
            )
            return html.div(
                [
                    html.div(
                        [
                            create_icon(
                                HAMBURGER_MENU,
                                onClick=toggle_visible,
                                style={"cursor": "pointer"},
                            ),
                            menu_window,
                        ],
                        style={"flexGrow": 1, "margin": 5},
                    ),
                    content,
                ],
                style={
                    "height": "100vh",
                    "width": "100%",
                    "display": "flex",
                    "flexFlow": "column",
                },
            )
        return content

    return result
