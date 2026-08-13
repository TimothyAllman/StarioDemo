from stario.markup.html import Div
from stario.markup.html import P


def CommonNothingToShowPlaceholderHtml(
    message: str,
    callToActionButton,
):
    return Div(
        {
            "class": " ".join(
                [
                    "border rounded p-6 bg-backcolor1 shadow-sm flex flex-col items-center justify-center text center",
                ]
            )
        },
        P(
            {"class": "text-sm text-frontcolor1"},
            message,
        ),
        Div(
            {"class": "mt-3 flex justify-center"},
            callToActionButton,
        ),
    )
