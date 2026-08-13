from stario.markup.html import Div


def ChatAppChatContainerHtml(
    *children,
):
    return Div(
        {
            "class": " ".join(
                [
                    "chat-container flex flex-col h-screen max-w-full mx-auto bg-backcolor1",
                    "md:max-w-[700px]",
                ]
            )
        },
        *children,
    )
