from stario.html import Div

from stariodemo.HtmlViewsPkg.UserListCardViewModule import UserListCardView


def XyzListView(items: list):
    """
    docstring
    """

    return Div(
        Div("xyz listy"),
        *[
            UserListCardView(
                x,
            )
            for x in items
        ],
    )
