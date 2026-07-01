from stario.markup.html import Div


def ChatAppChatTitleHtml(
    title_text,
):
    return Div(
        {
            "class": " ".join(
                [
                    "chat-title tex-[1.1rem] font-bold bg-linear-to-br from-amber-500 via-amber-400 to-amber-300 bg-clip-text text text-transparent",
                ]
            )
        },
        title_text,
    )
