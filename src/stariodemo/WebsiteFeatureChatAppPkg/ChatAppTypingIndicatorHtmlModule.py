from stario.markup.html import Div
from stario.markup.html import Span


def ChatAppTypingIndicatorHtml(
    *children,
    hidden: bool = False,
):

    return Div(
        {"id": "typing"},
        {
            "class": " ".join(
                [
                    "typing-indicator px-4 py-2 flex items-center gap-2 text-frontcolor1 tex-[0.8rem] shrink-0",
                    "hidden" if hidden else "",
                ]
            )
        },
        *children,
    )


def ChatAppTypingTextHtml(
    typing_text,
):

    return Span(
        {
            "class": " ".join(
                [
                    "typing-text italic",
                ]
            )
        },
        typing_text,
    )


def ChatAppTypingDotsHtml(
    *children,
):

    return Span(
        {
            "class": " ".join(
                [
                    "typing-dots inline-flex gap-[0.1rem]",
                ]
            )
        },
        *children,
    )


def ChatAppTypingDotHtml(
    dot_text: str,
    animation_delay: str,
):

    return Span(
        {"style": f"animation-delay: {animation_delay};"},
        {
            "class": " ".join(
                [
                    "dot animate-[bounce_1.4s_infinite_ease-inout_both] font-bold text-[1.2rem] text-frontcolor1",
                ]
            )
        },
        dot_text,
    )
