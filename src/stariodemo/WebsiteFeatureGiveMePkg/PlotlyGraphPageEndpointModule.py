from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureGiveMePkg.PlotlyGraphHtmlModule import PlotlyGraphHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml


def PlotlyGraphPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
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
