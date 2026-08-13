from stario.markup.html import Div

from stariodemo.WebsiteFeatureHtmlComponentsPkg.FooterBarHtmlModule import FooterBarHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.NavBarHtmlModule import NavBarHtml


def NavBarAndFooterHtml(
    *children,
):
    """
    docstring
    """

    return Div(
        NavBarHtml(),
        *children,
        FooterBarHtml(),
    )
