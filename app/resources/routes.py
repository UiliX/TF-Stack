from flask import Flask
from flask import render_template

from app.models.head_tags import H_INDEX, H_FLOWBITE


def include(app: Flask):
    @app.route("/")
    def index():
        return render_template("index.html", head=H_INDEX)

    @app.route("/flowbite")
    def flowbite():
        return render_template("flowbite.html", head=H_FLOWBITE)
