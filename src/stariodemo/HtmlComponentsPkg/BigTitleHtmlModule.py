from stario.markup.html import H2


def BigTitleHtml(title: str):
    return H2(
        {
            "class": [
                "text-3xl font-bold tracking-tight text-slate-900",
                "mb-4",
            ]
        },
        title,
    )
