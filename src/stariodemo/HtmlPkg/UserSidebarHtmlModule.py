from stariodemo.DataStructsPkg.UrlsModule import USER_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_EDIT_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.CommonSidebarLeftHtmlModule import CommonSidebarLeftHtml
from stariodemo.HtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml


def UserSideBarHtml(
    *children,
):
    """
    docstring
    """

    return CommonSidebarLeftHtml(
        [
            SideBarButtonHtml(name="List Users", url=USER_LIST_PAGE_URL.href()),
            SideBarButtonHtml(name="Add User", url=USER_ADD_PAGE_URL.href()),
            SideBarButtonHtml(name="Edit User", url=USER_EDIT_PAGE_URL.href()),
        ],
        *children,
    )
