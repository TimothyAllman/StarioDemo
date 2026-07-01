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
                    "border rounded p-6 bg-white shadow-sm flex flex-col items-center justify-center text center",
                ]
            )
        },
        P(
            {"class": "text-sm text-gray-600"},
            message,
        ),
        Div(
            {"class": "mt-3 flex justify-center"},
            callToActionButton,
        ),
    )
