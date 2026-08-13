from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarLeftHtmlModule import CommonSidebarLeftHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml
from stariodemo.WebsiteFeatureWidgetPkg.WidgetUrlsModule import WIDGET_ADD_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.WidgetUrlsModule import WIDGET_EDIT_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.WidgetUrlsModule import WIDGET_LIST_PAGE_URL


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
