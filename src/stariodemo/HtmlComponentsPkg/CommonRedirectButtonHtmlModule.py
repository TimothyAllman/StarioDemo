from stario.html import A


def CommonRedirectButtonHtml(
    name: str,
    url: str,
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
