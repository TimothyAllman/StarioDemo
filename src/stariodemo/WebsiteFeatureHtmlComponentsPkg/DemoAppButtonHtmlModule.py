from stario.markup.html import Button


def DemoAppButtonHtml(
    *children,
    buttoncolor="blue",
):
    return Button(
        {
            "class": " ".join(
                [
                    "text-frontcolor2 font-semibold px-4 py-4 bg-backcolor2",
                    "hover:bg-backcolor2hover transition transform hover:scale-105",
                ]
            )
        },
        *children,
    )
