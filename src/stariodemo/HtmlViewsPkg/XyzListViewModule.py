from stario.html import Div

from stariodemo.HtmlViewsPkg.UserListCardViewModule import WidgetListCardView


def XyzListView(items: list):
    """
    docstring
    """

    return Div(
        Div("xyz list of widgets"),
        *[
            WidgetListCardView(
                x,
            )
            for x in items
        ],
    )
