from flask import Flask
from flask import render_template

from app.models.head_tags import IndexHead, FlowbiteHead


def include(app: Flask):
    @app.route("/")
    def index():
        return render_template("index.html", head=IndexHead())

    @app.route("/flowbite")
    def flowbite():
        return render_template("flowbite.html", head=FlowbiteHead())
