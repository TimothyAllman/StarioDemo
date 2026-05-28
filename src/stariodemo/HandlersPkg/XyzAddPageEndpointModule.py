from stario import Context, responses
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.HtmlHtmlsPkg.XyzAddHtmlModule import XyzAddHtml
from stariodemo.HtmlHtmlsPkg.XyzSidebarHtmlModule import XyzSidebarHtml


def XyzAddPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:

        # Pass empty collections - user will get real data after subscribing
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    XyzSidebarHtml(
                        XyzAddHtml(),
                    )
                )
            ),
        )

    return handler
