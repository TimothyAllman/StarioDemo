from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.AbcAddHtmlModule import AbcAddHtml
from stariodemo.HtmlHtmlsPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def AbcAddPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.html(
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcAddHtml(),
                    )
                )
            )
        )

    return handler
