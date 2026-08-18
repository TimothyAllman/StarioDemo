from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetDetailsModule import WidgetDetailsHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetSidebarModule import WidgetSideBarHtml


def WidgetDetailsPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    WidgetSideBarHtml(
                        WidgetDetailsHtml(),
                    )
                )
            ),
        )

    return handler
