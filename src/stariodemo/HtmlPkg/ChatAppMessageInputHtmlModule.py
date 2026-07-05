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
            "class": " ".join(
                [
                    "message-input flex-1 bg-backcolor1 border border-edgecolor1 rounded-[10px] px-4 py-[0.7rem] text-[0.9rem] text-frontcolor1 outline-non transition-[border-color,box-shadow] duration-150",
                    "focus:border-edgecolor5 focus:ring-[3px] focus:ring-backcolor5",
                    "placeholder:text-frontcolor5",
                ]
            )
        },
        {"placeholder": "Type a message..."},
        {"autocomplete": "off"},
        {"autofocus": True},
        *children,
    )
