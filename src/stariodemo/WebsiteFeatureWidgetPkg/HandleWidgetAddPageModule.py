from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetAddModule import WidgetAddHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetSidebarModule import WidgetSideBarHtml


def WidgetAddPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    WidgetSideBarHtml(
                        WidgetAddHtml(),
                    )
                )
            ),
        )

    return handler
