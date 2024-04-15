"""Miscellaneous functionality to be used by Render apps"""
import contextlib
import inspect
import itertools
import os

import sys
import time
import traceback

import render_antd as antd
import render_html as html


import render as r
from render.observability import ObservableValue
from render.utils import apartial, decode_url, import_module, modify_attribute


MORE_MENU = "M456 231a56 56 0 10112 0 56 56 0 10-112 0zm0 280a56 56 0 10112 0 56 56 0 10-112 0zm0 280a56 56 0 10112 0 56 56 0 10-112 0z"
HAMBURGER_MENU = "M904 160H120c-4.4 0-8 3.6-8 8v64c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-64c0-4.4-3.6-8-8-8zm0 624H120c-4.4 0-8 3.6-8 8v64c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-64c0-4.4-3.6-8-8-8zm0-312H120c-4.4 0-8 3.6-8 8v64c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-64c0-4.4-3.6-8-8-8z"


def add_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d.items())
    return result


def create_icon(
    path_d,
    onClick=None,
    style={},
    height="1rem",
    width="1rem",
    className=None,
    viewBox="64 64 896 896",
):
    return html.span(
        html.svg(
            html.path(d=path_d),
            viewBox=viewBox,
            width=width,
            height=height,
            fill="currentColor",
        ),
        onClick=onClick,
        style=style,
        className=className,
    )


def responsive_margins(content, xs=None, sm=None, md=None, lg=None, xl=None, xxl=None, **kwargs):
    """Adapt horizontal margins to screen size"""
    xs = xs or 0
    sm = xs if sm is None else sm
    md = sm if md is None else md
    lg = md if lg is None else lg
    xl = lg if xl is None else xl
    xxl = xl if xxl is None else xxl
    return antd.Row(
        antd.Col(
            content,
            xs=24 - xs,
            sm=24 - sm,
            md=22 - md,
            lg=20 - lg,
            xl=18 - xl,
            xxl=16 - xxl,
        ),
        justify="space-around",
        **kwargs,
    )


COLUMNS_BREAKS = {
    "xs": dict(span=23),
    "sm": dict(span=23),
    "md": dict(span=21),
    "lg": dict(span=20),
    "xl": dict(span=18),
}


def load_module(code_or_file_path):
    window = r.get_window()
    file_path, hash_argument = decode_url(code_or_file_path)
    module = import_module(file_path)
    css = getattr(module, "CSS", [])
    if css:
        window.add_css(css)
    with modify_attribute(window, "hash", ObservableValue(hash_argument)):
        args = ()
        if module.app.__code__.co_argcount == 1:
            args = (window,)
        return module.app(*args)


@contextlib.contextmanager
def timeit():
    start = time.perf_counter()
    yield
    print(f"elapsed time {time.perf_counter() - start}")


def application_frame(title, content):
    return antd.Row(
        [antd.Col([html.h1(title), content], **COLUMNS_BREAKS)],
        justify="center",
        align="middle",
        gutter=[0, 20],
        className="todos-container",
    )


def folder_to_be_ignored(entry):
    return entry.startswith(".") or entry in ["__pycache__", "__init__.py"]


def create_file_explorer(base_path=None, folder_filter=None, file_filter=None):
    if base_path is None:
        base_path = "."
        root_name = os.path.split(os.getcwd())[1]
    else:
        if not os.path.exists(base_path):
            raise RuntimeError(f"Folder {base_path} cannot be found.")
        root_name = base_path
    current_path = ObservableValue()
    counter = itertools.count()
    nodes = {}

    def node_path(node_id):
        node = nodes[node_id[0] if isinstance(node_id, list) else node_id]
        path = []
        while node["pId"] is not None:
            path.append(node["title"])
            node = nodes[node["pId"]]
        return reversed(path)

    def populate_children(node_id):
        children = []
        path = os.path.join(base_path, *node_path(node_id))
        _, dirs, files = next(os.walk(path))
        for names, filter_method, isLeaf in [
            (dirs, folder_filter, False),
            (files, file_filter, True),
        ]:
            for entry in sorted(names):
                if filter_method and filter_method(entry):
                    continue
                child_id = next(counter)
                child = {
                    "id": child_id,
                    "pId": node_id,
                    "value": child_id,
                    "key": child_id,
                    "title": entry,
                    "isLeaf": isLeaf,
                }
                nodes[child_id] = child
                children.append(child)
        nodes[node_id]["children"] = children

    root_id = next(counter)
    root = nodes[root_id] = {
        "id": root_id,
        "key": root_id,
        "pId": None,
        "title": root_name,
    }
    populate_children(root_id)
    tree_data = ObservableValue(root["children"], key="root")

    async def onLoadData(node_id):
        populate_children(node_id)
        tree_data.notify()

    def onSelect(value):
        if value:
            path = list(node_path(value))
            if path:
                current_path.set(os.path.join(*path))

    return current_path, html.div(
        antd.Tree(
            style={"width": "100%"},
            showLine={"showLeafIcon": False},
            loadData=onLoadData,
            onSelect=onSelect,
            treeData=tree_data,
            defaultExpandedKeys=[root_id],
        ),
        style={"overflow": "auto", "maxHeight": "100%"},
    )


def create_file_chooser(
    base_path=None, title=None, on_ok=None, folder_filter=None, file_filter=None
):
    select_file_visible = ObservableValue(False, key="select_file_visible")
    current_path, tree = create_file_explorer(base_path, folder_filter, file_filter)

    async def onOk():
        select_file_visible.set(False)
        await r.call_maybe_coroutine(on_ok, (current_path(),))

    return antd.Modal(
        html.div(tree, style={"overflow": "scroll", "height": 500}),
        title=title,
        open=select_file_visible,
        onOk=onOk,
        onCancel=lambda: select_file_visible.set(False),
    ), lambda: select_file_visible.set(True)


class WindowProxy:
    def __init__(self, hash_argument: str) -> None:
        self.actual_window = r.get_window()
        self.hash = ObservableValue(hash_argument)
        for attribute in ["start_soon", "update_title", "call_js_method", "size", "client_connection"]:
            setattr(self, attribute, getattr(self.actual_window, attribute))

    def set_title(self, _title):
        pass


def evaluate_demo_module(module_path, hash_argument=None):
    try:
        module = import_module(module_path)
        css = getattr(module, "CSS", [])
        title = getattr(module, "TITLE", None)
        app = getattr(module, "app", None)
        if not app:
            return False, css, "Error", html.div("No app method found.")
        args = ()
        if type(app).__name__ == "type" or app.__code__.co_argcount == 1:
            args = (WindowProxy(hash_argument),)
        if inspect.iscoroutinefunction(app):
            transformed_app = r.AsyncCachedEvaluation(
                apartial(app, *args),
                task_group=r.get_window().task_group,
                loading_value=html.div(f"Loading {module_path}..."),
                error_constructor=lambda x: html.div([html.div(line) for line in x.split("\n")]),
            )
        else:
            transformed_app = app(*args)
        return True, css, title, transformed_app
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        return (
            False,
            [],
            "Error",
            html.div(
                [f"Failed to load {module_path}.py"]
                + [
                    html.p(line[:-1])
                    for line in traceback.format_exception(exc_type, exc_value, exc_traceback)
                ]
            ),
        )


def toggle_observable(observable: ObservableValue):
    return lambda: observable.set(not observable())
