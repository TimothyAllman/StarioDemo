from stario.html import Span


def ChatAppOnlineUsersHtml(
    *children,
):

    return Span(
        {"id": "online"},
        {
            "class": [
                "online-users flex items-center gap-3",
            ]
        },
        *children,
    )
