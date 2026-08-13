from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_ADD_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_EDIT_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_LIST_PAGE_URL
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarLeftHtmlModule import CommonSidebarLeftHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml


def WidgetSideBarHtml(
    *children,
):
    """
    docstring
    """

    return CommonSidebarLeftHtml(
        [
            SideBarButtonHtml(name="List Widgets", url=WIDGET_LIST_PAGE_URL.href()),
            SideBarButtonHtml(name="Add Widget", url=WIDGET_ADD_PAGE_URL.href()),
            SideBarButtonHtml(name="Edit Widget", url=WIDGET_EDIT_PAGE_URL.href()),
        ],
        *children,
    )
