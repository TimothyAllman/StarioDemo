from stario import at
from stario import data
from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import API_WIDGET_SEED_URL
from stariodemo.HtmlComponentsPkg.DemoAppButtonModule import DemoAppButton
from stariodemo.HtmlViewsPkg.WidgetListCardViewModule import WidgetListCardView


def XyzListView(items: list):
    """
    docstring
    """

    return Div(
        DemoAppButton(
            data.on(
                "click",
                at.get(url=API_WIDGET_SEED_URL),
            ),
            "Press Me For Data",
        ),
        Div("xyz list of widgets"),
        *[
            WidgetListCardView(
                x,
            )
            for x in items
        ],
    )
