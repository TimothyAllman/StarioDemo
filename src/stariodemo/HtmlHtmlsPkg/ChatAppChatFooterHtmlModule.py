from stario.html import Div


def ChatAppChatFooterHtml(
    *children,
):
    return Div(
        {
            "class": [
                "chat-footer bg-surface py-3 px-4 border-t border-border-light shrink 0 max-[480px]:py-2 max[480px]:px-3",
            ]
        },
        *children,
    )
