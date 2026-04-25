from pyhead import Head
from pyhead import elements as e

H_INDEX = Head([
    e.Page(
        title="TF-Stack",
    ),
    e.Stylesheet(href="/compiled.css"),
])

H_FLOWBITE = Head([
    e.Page(
        title="TF-Stack - Flowbite",
    ),
    e.Stylesheet(href="/compiled.css"),
    e.Script(src="https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js"),
])
