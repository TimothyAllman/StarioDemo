from stario.markup.html import Span


def ChatAppOnlineLabelHtml(
    label_text: str,
):

    return Span(
        {
            "class": " ".join(
                [
                    "online-label text-xs text-frontcolor1 font-medium",
                    "max-[480px]:hidden",
                ]
            )
        },
        label_text,
    )
