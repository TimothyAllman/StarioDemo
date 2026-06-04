from stario.html import Div


def ChatAppChatBodyHtml(
    *children,
):
    return Div(
        {
            "class": "chat-body flex1 overflow-y-auto flex flex-col relative bg-bg",
        },
        children,
    )
