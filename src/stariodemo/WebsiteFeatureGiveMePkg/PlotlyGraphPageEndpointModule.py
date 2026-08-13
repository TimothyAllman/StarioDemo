from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureGiveMePkg.PlotlyGraphHtmlModule import PlotlyGraphHtml


def PlotlyGraphPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    PlotlyGraphHtml(),
                )
            ),
        )

    return handler
