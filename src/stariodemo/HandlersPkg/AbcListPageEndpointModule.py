from stario import Context
from stario import Writer
from stario import responses

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.AbcListHtmlModule import AbcListHtml
from stariodemo.HtmlHtmlsPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def AbcListPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcListHtml(),
                    )
                )
            ),
        )

    return handler
