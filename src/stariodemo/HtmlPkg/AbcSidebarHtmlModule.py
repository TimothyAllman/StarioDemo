from stariodemo.BasicStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.CommonSidebarLeftHtmlModule import CommonSidebarLeftHtml
from stariodemo.HtmlComponentsPkg.SideBarButtonHtmlModule import SideBarButtonHtml


def AbcSideBarHtml(
    *children,
):
    """
    docstring
    """

    return CommonSidebarLeftHtml(
        [
            SideBarButtonHtml(
                name="List",
                url=ABC_LIST_PAGE_URL.href(),
            ),
            SideBarButtonHtml(
                name="Add",
                url=ABC_ADD_PAGE_URL.href(),
            ),
            SideBarButtonHtml(
                name="Calculation",
                url=ABC_CALCULATION_PAGE_URL.href(),
            ),
        ],
        *children,
    )
