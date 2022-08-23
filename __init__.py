import os

from flask import Flask
from tools.config import Config

working_dir = os.path.dirname(os.path.realpath(__name__))
config = Config(os.path.join(working_dir, 'config.ini'))

app = Flask(__name__)
app.secret_key = config["SECRET_KEY"]

with app.app_context():
    from tools.route_loader import load_routes
    from tools.package_loader import load_packages

    load_routes(working_dir, "routes")
    load_packages()
