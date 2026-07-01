from stario.markup.html import Button


def ChatAppSendButtonHtml(
    *children,
):

    return Button(
        {"type": "button"},
        {
            "class": " ".join(
                [
                    "send-button w-[42px] h-[42px] rounded-full border-0 bg-linear-to-br from-amber-500 to-amber-400 text-white cursor-pointer flex items-center justify-center",
                    "transition duration-150 shadow-blue-600 shrink-0",
                    "hover:enabled:scale-105 hover:enabled:shadow-blue-900",
                    "active:enabled:scale-95 disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none",
                ]
            )
        },
        *children,
    )
