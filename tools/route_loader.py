import os
import importlib


def load_routes(working_dir: str, route_path: str, recursive: bool = True):
    for file in os.listdir(os.path.join(working_dir, route_path)):
        if os.path.isdir(os.path.join(working_dir, route_path, file)) and recursive:
            load_routes(working_dir, os.path.join(route_path, file), recursive)

        if file.endswith(".py"):
            importlib.import_module(
                os.path.join(route_path, file).replace("\\", ".").replace("/", ".").strip(".py"),
            )
