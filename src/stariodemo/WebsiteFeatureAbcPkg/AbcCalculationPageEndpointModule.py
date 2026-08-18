from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureAbcPkg.AbcCalculationHtmlModule import AbcCalculationHtml
from stariodemo.WebsiteFeatureAbcPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml


def AbcCalculationPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    AbcSideBarHtml(
                        AbcCalculationHtml(),
                    )
                )
            ),
        )

    return handler
