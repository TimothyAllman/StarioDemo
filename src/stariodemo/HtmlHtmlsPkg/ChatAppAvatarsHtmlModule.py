from stario.html import Div


def ChatAppAvatarsHtml(
    *children,
):
    return Div(
        {
            "class": "avatars flex flex-row-reverse",
        },
        children,
    )
