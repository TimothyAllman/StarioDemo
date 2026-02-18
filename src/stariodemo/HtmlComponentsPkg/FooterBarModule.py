from stario.html import H1
from stario.html import Div


def FooterBar():
    return Div(
        {"class": "bg-blue-600 p-4 flex items center justify-between min-h-60"},
        {"id": "idFooter"},
        Div(
            {"class": "flex items-center space-x-6"},
            H1(
                {"class": "text-white text-2xl font-bold"},
                "Thanks",
            ),
        ),
    )
