import os
from datetime import timedelta

from flask import Flask
from tools.config import Config

working_dir = os.path.dirname(os.path.realpath(__file__))
config = Config(os.path.join(working_dir, 'config.ini'))

app = Flask(__name__)
app.secret_key = config["SECRET_KEY"]
app.permanent_session_lifetime = timedelta(days=9999)

with app.app_context():
    from tools.route_loader import load_routes
    from tools.package_loader import load_packages

    load_routes(working_dir, "routes")
    load_packages(
        keep_watching=config["WATCH_FOR_CHANGES"]
    )
