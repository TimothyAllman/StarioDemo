from stario.html import Div

from stariodemo.HtmlComponentsPkg.FooterBarModule import FooterBar
from stariodemo.HtmlComponentsPkg.NavBarModule import NavBar


def NavBarAndFooterView(
    *children,
):
    """
    docstring
    """

    return Div(
        NavBar(),
        *children,
        FooterBar(),
    )
