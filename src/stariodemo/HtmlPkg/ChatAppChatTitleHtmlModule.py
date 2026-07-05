from stario.markup.html import Div


def ChatAppChatTitleHtml(
    title_text,
):
    return Div(
        {
            "class": " ".join(
                [
                    "chat-title text-[1.1rem] font-bold bg-linear-to-br from-backcolor2 via-backcolor3 to-backcolor4 bg-clip-text text text-frontcolor2",
                ]
            )
        },
        title_text,
    )
