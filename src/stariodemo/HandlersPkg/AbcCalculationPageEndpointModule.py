from stario import Context, responses
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlPkg.AbcCalculationHtmlModule import AbcCalculationHtml
from stariodemo.HtmlPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.HtmlPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def AbcCalculationPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(w,
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcCalculationHtml(),
                    )
                )
            )
        )

    return handler
