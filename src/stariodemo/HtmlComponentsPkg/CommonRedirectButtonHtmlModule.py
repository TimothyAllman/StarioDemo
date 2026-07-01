from stario.markup.html import A


def CommonRedirectButtonHtml(
    name: str,
    url: str,
):
    return A(
        {
            "class": [
                "text-white font-semibold px-4 py-2 bg-color11",
                "hover:bg-color111 transition transform hover:scale-105",
            ]
        },
        {"href": url},
        name,
    )
