from datetime import datetime

from flask import Flask


def include(app: Flask):
    @app.template_filter('uncache')
    def uncache(val):
        ts = datetime.now().timestamp()
        return f"{val}?{int(ts)}"
