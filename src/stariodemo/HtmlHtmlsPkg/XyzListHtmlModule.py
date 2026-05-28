from stario import datastar
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
            datastar.on("click", datastar.get(url=API_WIDGET_SEED_URL)),
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
