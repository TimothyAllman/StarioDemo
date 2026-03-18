from stario import asset
from stario.html import Body
from stario.html import Head
from stario.html import Html
from stario.html import Link
from stario.html import Meta
from stario.html import Script
from stario.html import Title
from stario.toys import toy_inspector


def page(*children):
    """
    Base HTML shell with Datastar loaded.

    asset() returns fingerprinted filenames (e.g., style.a1b2c3.css)
    for automatic cache busting when files change.
    """
    return Html(
        {"lang": "en"},
        Head(
            Meta({"charset": "UTF-8"}),
            Meta({"name": "viewport", "content": "width=device-width, initial-scale=1"}),
            Title("Template - Stario"),
            Link({"rel": "stylesheet", "href": "/static/" + asset("css/style.css")}),
            Script({"type": "module", "src": "/static/" + asset("js/datastar.js")}),
            Script({"src": "https://cdn.tailwindcss.com"}),
        ),
        Body(
            toy_inspector(),  # Dev tool: shows current signals state
            *children,
        ),
    )
