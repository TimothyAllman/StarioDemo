from stario.markup.html import A


def CommonRedirectButtonHtml(
    name: str,
    url: str,
):
    return A(
        {
            "class": " ".join(
                [
                    "text-frontcolor1 font-semibold px-4 py-2 bg-backcolor1",
                    "hover:bg-backcolor1hover transition transform hover:scale-105",
                ]
            )
        },
        {"href": url},
        name,
    )
