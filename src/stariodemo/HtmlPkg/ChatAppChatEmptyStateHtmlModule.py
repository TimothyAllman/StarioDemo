from stario.markup.html import Div


def ChatAppChatEmptyStateHtml():
    return Div(
        {
            "class": " ".join(
                [
                    "empty-state text-frontcolor1 text-[0.9rem] p-8 text-center bg-backcolor1 rounded-[10px] border border-edgecolor1",
                ]
            )
        },
        "No messages yet. Say hello!",
    )
