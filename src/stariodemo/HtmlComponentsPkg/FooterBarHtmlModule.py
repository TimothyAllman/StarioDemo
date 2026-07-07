from stario.markup.html import H1
from stario.markup.html import A
from stario.markup.html import Div

from stariodemo.HtmlComponentsPkg.ThemeSelectorHtmlModule import ThemeSelectorHtml


def FooterBarHtml():
    return Div(
        {"class": "bg-backcolor1 p-4 flex items center justify-between min-h-60"},
        {"id": "idFooter"},
        FooterOtherLinks(),
        FooterColumn(
            *[
                "About",
                "Contact Us",
            ],
            title="Thanks",
        ),
        FooterColumn(
            ThemeSelectorHtml(),
            title="Theme",
        ),
    )


def FooterColumn(*children, title):
    return Div(
        {"class": "flex flex-col"},
        H1(
            {"class": "text-frontcolor1 text-2xl font-bold"},
            title,
        ),
        *children,
    )


def FooterOtherLinks():
    return FooterColumn(
        H1(
            "OtherLinks",
        ),
        [
            A("link 1"),
            A("link 4"),
            A("link 3"),
        ],
        title="Other Links",
    )
