from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetEditModule import WidgetEditHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetSidebarModule import WidgetSideBarHtml


def WidgetEditPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    WidgetSideBarHtml(
                        WidgetEditHtml(),
                    )
                )
            ),
        )

    return handler
