from stario.html import Div


def ChatAppMessagesHtml(
    *children,
    extra_classes: str = "",
):

    return Div(
        {"id": "message"},
        {
            "class": [
                "messages flex-1 p-4 flex flex-col gap-2 overflow-y-auto",
                extra_classes if extra_classes else "",
            ]
        },
        *children,
    )
