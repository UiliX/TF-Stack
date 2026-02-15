from flask import Flask
from flask_imp import Imp

from app.config import IMP_CONFIG, FLASK_CONFIG


def create_app():
    app = Flask(
        __name__,
        static_url_path="/",
        static_folder="static",
        template_folder="templates",
    )
    app.config.from_object(FLASK_CONFIG.as_object())

    imp = Imp(app, IMP_CONFIG)
    imp.import_resources()

    return app
