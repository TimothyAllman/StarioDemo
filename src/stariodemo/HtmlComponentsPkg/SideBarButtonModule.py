from stario.html import A
from stario.html import Span


def SideBarButton(url, name):
    return A(
        {
            "class": [
                "flex items-center px-2 py-1.5 text-body text-white rounded-base bg-blue-700",
                "hover:bg-blue-800 hover:scale-105",
            ]
        },
        {"href": url},
        Span(
            {"class": "ms-3"},
            name,
        ),
    )
