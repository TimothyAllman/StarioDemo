from stario import at
from stario import data
from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import API_WIDGET_SEED_URL
from stariodemo.HtmlComponentsPkg.DemoAppButtonHtmlModule import DemoAppButtonHtml
from stariodemo.HtmlHtmlsPkg.WidgetListCardHtmlModule import WidgetListCardHtml


def XyzListHtml(items: list):
    """
    docstring
    """

    return Div(
        DemoAppButtonHtml(
            data.on(
                "click",
                at.get(url=API_WIDGET_SEED_URL),
            ),
            "Press Me For Data",
        ),
        Div("xyz list of widgets"),
        *[
            WidgetListCardHtml(
                x,
            )
            for x in items
        ],
    )
