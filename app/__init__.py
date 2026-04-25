from flask import Flask
# from werkzeug.middleware.proxy_fix import ProxyFix

from app.config import IMP_CONFIG, FLASK_CONFIG
from app.extensions import imp


def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(FLASK_CONFIG.as_object())
    # app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    imp.init_app(app, IMP_CONFIG)
    imp.import_resources()

    return app
