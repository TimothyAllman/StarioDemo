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
                    "flex items-center px-2 py-1.5 text-body text-frontcolor1 rounded-base bg-backcolor1",
                    "hover:bg-backcolor1hover hover:scale-105",
                ]
            )
        },
        {"href": url},
        Span(
            {"class": "ms-3"},
            name,
        ),
    )
