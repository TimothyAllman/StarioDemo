from stario.html import Div


def ChatAppChatContainerHtml(
    *children,
):
    return Div(
        {
            "class": [
                "chat-container flex flex-col hscreen max-w-full mx-auto bg-bg",
                "md:max-w-[700px]",
            ]
        },
        *children,
    )
