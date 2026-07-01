from stario.markup.html import Div


def ChatAppChatContainerHtml(
    *children,
):
    return Div(
        {
            "class": [
                "chat-container flex flex-col h-screen max-w-full mx-auto bg-bg",
                "md:max-w-[700px]",
            ]
        },
        *children,
    )
