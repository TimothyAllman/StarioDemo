from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureAbcPkg.AbcListHtmlModule import AbcListHtml
from stariodemo.WebsiteFeatureAbcPkg.AbcSidebarHtmlModule import AbcSideBarHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


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
