from stario.markup.html import Div


def ChatAppInputFormHtml(
    *children,
):
    return Div(
        {"id": "input-form"},
        {
            "class": [
                "input-form flex gap-2 items-center",
            ]
        },
        *children,
    )
