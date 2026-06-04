from stario.html import Span


def ChatAppOnlineLabelHtml(
    label_text: str,
):

    return Span(
        {
            "class": [
                "online-label text-xs text-muted font-medium",
                "max-[480px]:hidden",
            ]
        },
        label_text,
    )
