from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureWidgetPkg.WidgetEditHtmlModule import WidgetEditHtml
from stariodemo.WebsiteFeatureWidgetPkg.WidgetSidebarHtmlModule import WidgetSideBarHtml


def WidgetEditPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
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
