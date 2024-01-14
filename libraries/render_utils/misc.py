import os
import pathlib
from itertools import chain


def list_all_files(folder, filter=None):
    return chain.from_iterable(
        (
            os.path.join(root, name)
            for name in files
            if not filter or filter(os.path.join(root, name))
        )
        for root, _dirs, files in os.walk(folder)
    )





def get_module_name(module_path: str):
    return module_path.replace(os.sep, ".")[:-3]


def increment_observable_bounded(value, min_value, max_value, increment):
    def result():
        current_value = value()
        new_value = min(max(value() + increment, min_value), max_value)
        if new_value != current_value:
            value.set(new_value)

    return result



