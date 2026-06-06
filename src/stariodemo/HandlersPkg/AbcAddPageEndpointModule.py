from stario import Context
from stario import Writer
from stario import responses

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlPkg.AbcAddHtmlModule import AbcAddHtml
from stariodemo.HtmlPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.HtmlPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def AbcAddPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcAddHtml(),
                    )
                )
            ),
        )

    return handler
