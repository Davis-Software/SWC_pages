import os

from __init__ import app, config
from flask import make_response, session, redirect, send_file, render_template_string, abort

from tools.package_loader import PACKAGES, PACKAGE_CACHE_FOLDER
from utils.request_codes import RequestCode


@app.route("/")
@app.route("/<path:path>")
def route_index(path=None):
    if not session.get("joined_page"):
        if config["DEFAULT_PAGE"] is not None and path is None:
            session["joined_page"] = config["DEFAULT_PAGE"]
            session.permanent = True
        else:
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


@app.route("/d")
def route_default():
    if config["DEFAULT_PAGE"] is not None:
        package = config["DEFAULT_PAGE"]

        session["joined_page"] = package
        session.permanent = True

        return redirect("/")
    else:
        return make_response("", RequestCode.ClientError.Forbidden)


@app.route("/j/<page>")
@app.route("/join/<page>")
def route_join(page):
    if page in PACKAGES:
        session["joined_page"] = page
        session.permanent = True
        return redirect("/")
    else:
        return make_response("", RequestCode.ClientError.NotFound)


@app.route("/list")
def route_list():
    if config.get_bool("ALLOW_LIST"):
        links = map(lambda x: f"<a href='/j/{x}'>{x}</a><br/>", PACKAGES.keys())
        return render_template_string("".join(links))
    abort(RequestCode.ClientError.NotFound)
