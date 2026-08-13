from stario.markup.html import Button


def ChatAppSendButtonHtml(
    *children,
):

    return Button(
        {"type": "button"},
        {
            "class": " ".join(
                [
                    "send-button w-[42px] h-[42px] rounded-full border-0 bg-linear-to-br from-backcolor1 to-backcolor1 text-frontcolor2 cursor-pointer flex items-center justify-center",
                    "transition duration-150 shadow-backcolor5 shrink-0",
                    "hover:enabled:scale-105 hover:enabled:shadow-backcolor4",
                    "active:enabled:scale-95 disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none",
                ]
            )
        },
        *children,
    )
