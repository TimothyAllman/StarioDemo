from stario.markup.html import Div
from stario.markup.html import Span


def ChatAppUsernameHtml(
    username_text: str,
    username_color: str,
):

    return Span(
        {
            "class": " ".join(
                [
                    "username text-xs font-semibold",
                ]
            )
        },
        {"style": f"color: {username_color};"},
        username_text,
    )


def ChatAppTimestampHtml(
    timestamp_text: str,
):

    return Span(
        {
            "class": " ".join(
                [
                    "timestamp text-[0.65rem] text-muted",
                ]
            )
        },
        timestamp_text,
    )


def ChatAppMessageTextHtml(
    message_text: str,
):

    return Div(
        {
            "class": " ".join(
                [
                    "message-text text-[0.9rem] leading-[1.45] break-words text-fg",
                ]
            )
        },
        message_text,
    )
