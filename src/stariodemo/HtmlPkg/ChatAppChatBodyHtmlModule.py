from stario.markup.html import Div


def ChatAppChatBodyHtml(
    *children,
):
    return Div(
        {
            "class": "chat-body flex-1 overflow-y-auto flex flex-col relative bg-bg",
        },
        *children,
    )
