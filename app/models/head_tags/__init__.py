from pyhead import HeadClass
from pyhead import elements as e


class IndexHead(HeadClass):
    elements = [
        e.Page(
            title="TF-Stack",
        ),
        e.Stylesheet(href="/compiled.css"),
    ]


class FlowbiteHead(HeadClass):
    elements = [
        e.Page(
            title="TF-Stack - Flowbite",
        ),
        e.Stylesheet(href="/compiled.css"),
        e.Script(src="https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js"),
    ]
