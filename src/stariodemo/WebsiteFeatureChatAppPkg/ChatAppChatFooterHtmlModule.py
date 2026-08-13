from stario.markup.html import Div


def ChatAppChatFooterHtml(
    *children,
):
    return Div(
        {
            "class": " ".join(
                [
                    "chat-footer bg-backcolor1 py-3 px-4 border-t border-edgecolor1 shrink-0 max-[480px]:py-2 max[480px]:px-3",
                ]
            )
        },
        *children,
    )
