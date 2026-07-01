from stario.markup.html import A
from stario.markup.html import Span


def SideBarButtonHtml(
    url,
    name,
):
    return A(
        {
            "class": " ".join(
                [
                    "flex items-center px-2 py-1.5 text-body text-white rounded-base bg-blue-700",
                    "hover:bg-blue-800 hover:scale-105",
                ]
            )
        },
        {"href": url},
        Span(
            {"class": "ms-3"},
            name,
        ),
    )
