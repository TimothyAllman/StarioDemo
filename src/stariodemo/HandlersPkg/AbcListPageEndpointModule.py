from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.AbcListHtmlModule import AbcListHtml
from stariodemo.HtmlHtmlsPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def AbcListPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.html(
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcListHtml(),
                    )
                )
            )
        )

    return handler
