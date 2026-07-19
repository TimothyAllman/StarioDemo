from stariodemo.DataStructsPkg.UrlsModule import USER_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_EDIT_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.CommonSidebarLeftHtmlModule import CommonSidebarLeftHtml
from stariodemo.HtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml


def WidgetSideBarHtml(
    *children,
):
    """
    docstring
    """

    return CommonSidebarLeftHtml(
        [
            SideBarButtonHtml(name="List Widgets", url=USER_LIST_PAGE_URL.href()),
            SideBarButtonHtml(name="Add Widget", url=USER_ADD_PAGE_URL.href()),
            SideBarButtonHtml(name="Edit Widget", url=USER_EDIT_PAGE_URL.href()),
        ],
        *children,
    )
