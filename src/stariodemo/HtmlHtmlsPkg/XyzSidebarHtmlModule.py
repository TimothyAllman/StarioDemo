from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import XYZ_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import XYZ_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml
from stariodemo.HtmlHtmlsPkg.LeftSidebarAndContentHtmlModule import LeftSidebarAndContentHtml


def XyzSidebarHtml(
    *children,
):
    """
    docstring
    """

    return Div(
        LeftSidebarAndContentHtml(
            [
                SideBarButtonHtml(name="List", url=XYZ_LIST_PAGE_URL),
                SideBarButtonHtml(name="Add", url=XYZ_ADD_PAGE_URL),
            ],
            *children,
        ),
    )
