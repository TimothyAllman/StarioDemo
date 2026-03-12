from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import XYZ_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import XYZ_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.SideBarButtonModule import SideBarButton
from stariodemo.HtmlViewsPkg.LeftSidebarAndContentViewModule import LeftSidebarAndContentView


def XyzSidebarView(
    *children,
):
    """
    docstring
    """

    return Div(
        LeftSidebarAndContentView(
            [
                SideBarButton(name="List", url=XYZ_LIST_PAGE_URL),
                SideBarButton(name="Add", url=XYZ_ADD_PAGE_URL),
            ],
            *children,
        ),
    )
