from stario.html import Div

from stariodemo.HtmlComponentsPkg.SideBarModule import SideBar


def LeftSidebarAndContentView(
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
            SideBar(
                [item for item in buttons],
            ),
        ),
        Div(
            {"class": "ml-2"},
            *children,
        ),
    )
