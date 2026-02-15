from flask import Flask
from flask import render_template


def include(app: Flask):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/flowbite")
    def flowbite():
        return render_template("flowbite.html")
