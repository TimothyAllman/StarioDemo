from stario.markup.html import Button


def DemoAppButtonHtml(
    *children,
    buttoncolor="blue",
):
    return Button(
        {
            "class": [
                f"text-white font-semibold px-4 py-4 bg-{buttoncolor}-700",
                f"hover:bg-{buttoncolor}-800 transition transform hover:scale-105",
            ]
        },
        *children,
    )
