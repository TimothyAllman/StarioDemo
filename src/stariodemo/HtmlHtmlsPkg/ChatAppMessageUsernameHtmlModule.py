from stario.html import Div
from stario.html import Span


def ChatAppUsernameHtml(
    username_text: str,
    username_color: str,
):

    return Span(
        {
            "class": [
                "username text-xs font-semibold",
            ]
        },
        {"style": {"color": username_color}},
        username_text,
    )


def ChatAppTimestampHtml(
    timestamp_text: str,
):

    return Span(
        {
            "class": [
                "timestamp text-[0.65rem] text-muted",
            ]
        },
        timestamp_text,
    )


def ChatAppMessageTextHtml(
    message_text: str,
):

    return Div(
        {
            "class": [
                "message-text text-[0.9rem] leading-[1.45] break-words text-fg",
            ]
        },
        message_text,
    )
