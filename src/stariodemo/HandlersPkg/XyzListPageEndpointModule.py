from stario import Context
from stario import Writer
from stario import responses

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.HtmlHtmlsPkg.XyzListHtmlModule import XyzListHtml
from stariodemo.HtmlHtmlsPkg.XyzSidebarHtmlModule import XyzSidebarHtml
from stariodemo.PiccoloPkg.GetWidgetsModule import GetWidgets


def XyzListPageEndpoint(
    # Database: list[User],
):
    async def handler(c: Context, w: Writer) -> None:

        items = await GetWidgets()

        # Pass empty collections - user will get real data after subscribing
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    XyzSidebarHtml(
                        XyzListHtml(items),
                    )
                )
            ),
        )

    return handler
