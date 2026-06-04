from stario.html import A


def NavBarButtonHtml(
    url,
    name,
):
    return A(
        {
            "class": [
                "text-white font-semibold px-4 py-2 bg-color222",
                "hover:bg-color22 transition transform hover:scale-105",
            ]
        },
        {"href": url},
        name,
    )
