from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.AbcCalculationHtmlModule import AbcCalculationHtml
from stariodemo.HtmlHtmlsPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def AbcCalculationPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.html(
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcCalculationHtml(),
                    )
                )
            )
        )

    return handler
