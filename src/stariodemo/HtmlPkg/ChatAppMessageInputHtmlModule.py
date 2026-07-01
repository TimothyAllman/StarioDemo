from stario.markup.html import Input


def ChatAppMessageInputHtml(
    *children,
    is_own: bool = False,
    msg_id: str = "",
):

    return Input(
        {"id": "message-input"},
        {"type": "text"},
        {
            "class": [
                "message-input flex-1 bg-bg border border-border-light rounded-[10px] px-4 py-[0.7rem] text-[0.9rem] text-fg outline-non transition-[border-color,box-shadow] duration-150",
                "focus:border-amber-300 focus:ring-[3px] focus:ring-blue-600",
                "placeholder:text-muted",
            ]
        },
        {"placeholder": "Type a message..."},
        {"autocomplete": "off"},
        {"autofocus": True},
        *children,
    )
