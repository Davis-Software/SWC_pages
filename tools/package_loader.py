import os
import json
import shutil
from time import sleep
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


def load_packages(keep_watching=False):
    print("\n--- Loading packages... ---")
    for package in dict(**PACKAGES):
        print("Removing package: " + package)
        del PACKAGES[package]

    sleep(.1)
    
    print("Removing package cache...")
    for cached_package in os.listdir(PACKAGE_CACHE_FOLDER):
        print("Removing package cache: " + cached_package)
        shutil.rmtree(os.path.join(PACKAGE_CACHE_FOLDER, cached_package))

    sleep(.1)

    print("Loading packages...")
    for package in filter(lambda x: x.endswith(".zip"), os.listdir(PACKAGE_FOLDER)):
        with ZipFile(os.path.join(PACKAGE_FOLDER, package), "r") as zip_file:
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

    print("Loaded packages:")
    for package in PACKAGES:
        print("Package: " + package)
        print("Routes: " + str(PACKAGES[package]["routes"]))

    print("--- Packages loaded ---\n")

    if keep_watching:
        from threading import Thread
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        class PackageWatcher(FileSystemEventHandler):
            def __call(self):
                def wrapper():
                    print("Reloading packages in 5 seconds...")
                    sleep(5)
                    print("Reloading packages...")
                    load_packages(keep_watching=False)

                Thread(target=wrapper).start()

            def on_created(self, event):
                self.__call()

            def on_deleted(self, event):
                self.__call()

        observer = Observer()
        observer.schedule(PackageWatcher(), PACKAGE_FOLDER, recursive=False)
        observer.start()

        PACKAGE_WATCHER = observer
