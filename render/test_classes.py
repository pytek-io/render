import anyio
import sys
import os
import importlib
from functools import partial
import inspect
import traceback


async def main():
    import render as r
    from render import Component, InputComponent
    from render.common import CURRENT_CONTROLLER
    from render.props import Container
    import render.common

    render.common.OUT_OF_SESSION = True

    render_attributes = set(
        [
            "_nb",
            "_cached_children",
            "_props_values",
            "_callbacks_holder",
            "_value",
            "children",
            "onChange",
            "defaultValue",
            "on_didmount",
            "children_counter",
            "has_dependencies",
            "parent_relationship",
            "weak_ref",
            "key",
            "is_stale",
            "mount_status",
            "custom_attributes",
            "parent",
            "controller",
            "on_unmount",
            "_displayed_value",
            "input_value_update",
            "onAfterChange",
        ]
    )

    CURRENT_CONTROLLER.set(r.Controller())

    klasses = [Component, InputComponent, Container]

    for name in os.listdir("libraries"):
        if name in ["__pycache__", "build"]:
            continue
        print(name)
        module = importlib.import_module("libraries." + name[:-3] if name.endswith(".py") else name)
        for symbol in map(partial(getattr, module), dir(module)):
            if (
                inspect.isclass(symbol)
                and issubclass(symbol, Component)
                and not any(symbol is klass for klass in klasses)
            ):
                try:
                    declared_attributes = (
                        symbol.ATTRIBUTES
                        + symbol.CALLBACKS
                        + (symbol.DATA if hasattr(symbol, "DATA") else [])
                    )
                    instance = symbol(None, **dict.fromkeys(symbol.CALLBACKS, None))
                    attributes = [
                        name
                        for name in instance.__dict__
                        if not (name.endswith("__staticSelector") or name in render_attributes)
                    ]
                    undeclared_attributes = set(attributes).difference(declared_attributes)
                    missing_attributes = [
                        name
                        for name in set(declared_attributes).difference(attributes)
                        if not (name.endswith("__staticSelector") or name in render_attributes)
                    ]
                    if undeclared_attributes:
                        print("undeclared attributes", symbol.__name__, undeclared_attributes)
                    if missing_attributes:
                        print("missing attributes", symbol.__name__, missing_attributes)
                except Exception as e:
                    traceback.print_exc()
                    print(symbol, e)


if __name__ == "__main__":
    sys.path.append("libraries")
    anyio.run(main)
