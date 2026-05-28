from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml
from stariodemo.HtmlHtmlsPkg.LeftSidebarAndContentHtmlModule import LeftSidebarAndContentHtml


def AbcSideBarHtml(
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
        LeftSidebarAndContentHtml(
            [
                SideBarButtonHtml(name="List", url=ABC_LIST_PAGE_URL),
                SideBarButtonHtml(name="Add", url=ABC_ADD_PAGE_URL),
                SideBarButtonHtml(name="Calculation", url=ABC_CALCULATION_PAGE_URL),
            ],
            *children,
        ),
    )
