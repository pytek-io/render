from contextvars import ContextVar


def create_app(app_class):
    from render_html import div
    from render_utils import (HAMBURGER_MENU, create_icon,
                              create_settings_window)

    from render import get_window

    window = get_window()
    if not hasattr(app_class, "_instance"):
        app_class._instance = ContextVar("_instance")
        app_class.instance = app_class._instance.get
    app = app_class(*((window,) if app_class.__init__.__code__.co_argcount > 1 else ()))
    app_class._instance.set(app)
    window.user_data["app"] = app
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
        return div(
            [
                div(
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
