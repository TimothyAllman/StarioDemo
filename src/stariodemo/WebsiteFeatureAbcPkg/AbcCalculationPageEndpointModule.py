from stario import Context, responses
from stario import Writer

from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureAbcPkg.AbcCalculationHtmlModule import AbcCalculationHtml
from stariodemo.WebsiteFeatureAbcPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


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
