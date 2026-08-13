from stario.markup.html import Div

from stariodemo.WebsiteFeatureHtmlComponentsPkg.SideBarHtmlModule import SideBarHtml


def LeftSidebarAndContentHtml(
    buttons: list,
    *children,
):
    """
    docstring
    """

    return Div(
        {"class": "grid grid-cols-1 lg:grid-cols-[200px_1fr]"},
        Div(
            {"class": "min-h-screen bg-red-500 w-full"},
            SideBarHtml(
                [item for item in buttons],
            ),
        ),
        Div(
            {"class": "ml-2"},
            *children,
        ),
    )
