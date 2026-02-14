from stario.html import H1
from stario.html import Div

from stariodemo.ViewsPkg.NavBarButtonModule import NavBarButton


def NavBarFragment():
    return Div(
        {"class": "bg-blue-600 p-4 flex items center"},
        Div(
            {"class": "flex items-center space-x-6 px-2"},
            H1(
                {"class": "text-white text-2xl font-bold"},
                "Stario With Tailwind",
            ),
        ),
        *[NavBarButton(name="hahah", url="#") for _ in range(4)],
        NavBarButton(name="hehehe", url="#"),
    )
