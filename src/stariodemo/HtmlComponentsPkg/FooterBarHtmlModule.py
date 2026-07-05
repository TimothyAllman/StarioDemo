from stario.markup.html import H1
from stario.markup.html import Div

from stariodemo.HtmlComponentsPkg.ThemeSelectorHtmlModule import ThemeSelectorHtml


def FooterBarHtml():
    return Div(
        {"class": "bg-backcolor1 p-4 flex items center justify-between min-h-60"},
        {"id": "idFooter"},
        ThemeSelectorHtml(),
        ThemeSelectorHtml(),
        Div(
            {"class": "flex items-center space-x-6"},
            H1(
                {"class": "text-frontcolor1 text-2xl font-bold"},
                "Thanks",
            ),
        ),
        ThemeSelectorHtml(),
    )
