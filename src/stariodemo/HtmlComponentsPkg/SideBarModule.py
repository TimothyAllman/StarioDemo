from stario.html import H1
from stario.html import Div

from stariodemo.HtmlComponentsPkg.NavBarButtonModule import NavBarButton
from stariodemo.HtmlComponentsPkg.SideBarButtonModule import SideBarButton


def SideBar(*buttons):
    return Div(
        {"class": "flex flex-col"},
        [item for item in buttons],
    )
