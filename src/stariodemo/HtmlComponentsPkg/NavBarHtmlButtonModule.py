from stario.html import A


def NavBarButtonHtml(
    url,
    name,
):
    return A(
        {
            "class": [
                "text-white font-semibold px-4 py-2 bg-blue-700",
                "hover:bg-blue-800 transition transform hover:scale-105",
            ]
        },
        {"href": url},
        name,
    )
