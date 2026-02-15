from flask import Flask

from flask_imp import Imp
from flask_imp.config import ImpConfig, FlaskConfig


def create_app():
    app = Flask(
        __name__,
        static_url_path="/",
        static_folder="static",
        template_folder="templates",
    )

    FlaskConfig(
        secret_key="02f65a5c46cf19b06833ad85cc7eab5f3d87e5c91164325f",
        app_instance=app
    )

    imp = Imp(app, ImpConfig())
    imp.import_resources()

    return app
