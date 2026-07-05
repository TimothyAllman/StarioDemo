from stario.markup.html import Div


def ChatAppChatHeaderHtml(
    *children,
):
    return Div(
        {
            "class": " ".join(
                [
                    "chat-header bg-backcolor1 py-3 px-4 flex items-center justify-between border-b border-edgecolor1 shrink-0",
                ]
            )
        },
        *children,
    )
