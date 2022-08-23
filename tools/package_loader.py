import os
import json
import shutil
from zipfile import ZipFile

from __init__ import working_dir


PACKAGE_FOLDER = os.path.join(working_dir, "packages")
PACKAGE_CACHE_FOLDER = os.path.join(working_dir, "package_cache")

PACKAGES = {}


def discover_routes(package):
    location = os.path.join(PACKAGE_CACHE_FOLDER, package)

    routes = []
    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(".html"):
                routes.append(file)
    return routes


def load_packages():
    for package in PACKAGES:
        del PACKAGES[package]
    for cached_package in os.listdir(PACKAGE_CACHE_FOLDER):
        shutil.rmtree(os.path.join(PACKAGE_CACHE_FOLDER, cached_package))

    for package in filter(lambda x: x.endswith(".zip"), os.listdir(PACKAGE_FOLDER)):
        with ZipFile(os.path.join(PACKAGE_FOLDER, package)) as zip_file:
            if "manifest.json" not in [zip_f.filename for zip_f in zip_file.infolist()]:
                continue

            with zip_file.open("manifest.json") as manifest:
                manifest = json.loads(manifest.read().decode("utf-8"))
                zip_file.extractall(
                    os.path.join(
                        PACKAGE_CACHE_FOLDER,
                        manifest["id"]
                    )
                )
                PACKAGES[manifest["id"]] = manifest
                PACKAGES[manifest["id"]]["routes"] = discover_routes(manifest["id"])
