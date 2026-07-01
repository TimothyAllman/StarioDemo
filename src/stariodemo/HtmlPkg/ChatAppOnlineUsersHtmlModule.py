from stario.markup.html import Span


def ChatAppOnlineUsersHtml(
    *children,
):

    return Span(
        {"id": "online"},
        {
            "class": " ".join(
                [
                    "online-users flex items-center gap-3",
                ]
            )
        },
        *children,
    )
