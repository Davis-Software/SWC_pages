import os

from __init__ import app
from flask import make_response, session, redirect, send_file

from tools.package_loader import PACKAGES, PACKAGE_CACHE_FOLDER
from utils.request_codes import RequestCode


@app.route("/")
@app.route("/<path:path>")
def route_index(path=None):
    if not session.get("joined_page"):
        return make_response("", RequestCode.ClientError.Forbidden)

    package = session.get("joined_page")
    if package not in PACKAGES:
        return make_response("", RequestCode.ClientError.BadRequest)

    if path is None:
        return send_file(os.path.join(PACKAGE_CACHE_FOLDER, package, PACKAGES[package]["entry"]))

    elif path in PACKAGES[package]["routes"] or f"{path}.html" in PACKAGES[package]["routes"]:
        return send_file(os.path.join(PACKAGE_CACHE_FOLDER, package, f"{path}.html" if not path.endswith(".html") else path))

    else:
        path = os.path.join(PACKAGE_CACHE_FOLDER, package, path)
        if os.path.exists(path):
            return send_file(path)
        return make_response("", RequestCode.ClientError.NotFound)


@app.route("/join/<page>")
def route_join(page):
    if page in PACKAGES:
        session["joined_page"] = page
        session.permanent = True
        return redirect("/")
    else:
        return make_response("", RequestCode.ClientError.NotFound)
