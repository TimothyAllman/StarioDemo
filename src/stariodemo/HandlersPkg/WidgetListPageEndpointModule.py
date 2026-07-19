from stario import Context
from stario import Writer
from stario import responses

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.HtmlPkg.WidgetListHtmlModule import WidgetListHtml
from stariodemo.HtmlPkg.WidgetSidebarHtmlModule import WidgetSideBarHtml


def WidgetListPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    WidgetSideBarHtml(
                        await WidgetListHtml(),
                    )
                )
            ),
        )

    return handler
