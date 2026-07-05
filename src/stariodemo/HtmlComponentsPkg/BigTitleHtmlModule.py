from stario.markup.html import H2


def BigTitleHtml(title: str):
    return H2(
        {
            "class": " ".join(
                [
                    "text-3xl font-bold tracking-tight text-frontcolor4",
                    "mb-4",
                ]
            )
        },
        title,
    )
