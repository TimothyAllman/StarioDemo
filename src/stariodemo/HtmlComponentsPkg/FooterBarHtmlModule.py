from stario.markup.html import H1
from stario.markup.html import Div


def FooterBarHtml():
    return Div(
        {"class": "bg-color11 p-4 flex items center justify-between min-h-60"},
        {"id": "idFooter"},
        Div(
            {"class": "flex items-center space-x-6"},
            H1(
                {"class": "text-white text-2xl font-bold"},
                "Thanks",
            ),
        ),
    )
