from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureAbcPkg.AbcListHtmlModule import AbcListHtml
from stariodemo.WebsiteFeatureAbcPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml


def AbcListPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
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
