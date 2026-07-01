from stario.markup.html import Div

from stariodemo.HtmlComponentsPkg.FooterBarHtmlModule import FooterBarHtml
from stariodemo.HtmlComponentsPkg.NavBarHtmlModule import NavBarHtml


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
