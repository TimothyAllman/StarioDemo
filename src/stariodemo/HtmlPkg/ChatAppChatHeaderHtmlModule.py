from stario.markup.html import Div


def ChatAppChatHeaderHtml(
    *children,
):
    return Div(
        {
            "class": " ".join(
                [
                    "chat-header bg-surface py-3 px-4 flex items-center justify-between border-b border-border-light shrink-0",
                ]
            )
        },
        *children,
    )
