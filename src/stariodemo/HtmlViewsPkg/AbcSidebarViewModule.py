from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.SideBarButtonModule import SideBarButton
from stariodemo.HtmlViewsPkg.LeftSidebarAndContentViewModule import LeftSidebarAndContentView


def AbcSideBarView(
    *children,
    # username: str,
    # color: str,
    # *,
    # messages: list[Message],
    # users: dict[str, User],
):
    """
    docstring
    """

    return Div(
        LeftSidebarAndContentView(
            [
                SideBarButton(name="List", url=ABC_LIST_PAGE_URL),
                SideBarButton(name="Add", url=ABC_ADD_PAGE_URL),
                SideBarButton(name="Calculation", url=ABC_CALCULATION_PAGE_URL),
            ],
            *children,
        ),
    )
