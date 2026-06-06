from stario.html import Div


def ChatAppMessageBubbleHtml(
    *children,
    is_own: bool = False,
    msg_id: str = "",
):

    return Div(
        {"data-msg-id": msg_id} if msg_id else None,
        {
            "class": [
                "message max-w-[70%] px-[0.85rem] py-[0.6rem] rounded-[10px] border border-amber-300 rounded-tl-[10-px] rounded-tr-[4px] shadow-[0_1px_2px_rgba(0,0,0,0.04)] animate-[slideIn_0.15s_ease-out]",
                "bg-bubble-own self-end" if is_own else "bg-bubble-other self-start",
            ]
        },
        *children,
    )


def ChatAppMessageHeaderHtml(
    *children,
    is_own: bool = False,
):

    return Div(
        {
            "class": [
                "message-header flex items-baseline gap-2 mb-[0.2rem]",
                "flex-row-reverse" if is_own else "",
            ]
        },
        *children,
    )
