from stario.markup.html import A


def NavBarButtonHtml(
    url,
    name,
):
    return A(
        {
            "class": " ".join(
                [
                    "text-frontcolor1 font-semibold px-4 py-2 bg-color1",
                    "hover:bg-backcolor1hover transition transform hover:scale-105",
                ]
            )
        },
        {"href": url},
        name,
    )
