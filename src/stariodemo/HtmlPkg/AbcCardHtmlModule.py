from stario.markup.html import Div
from stario.markup.html import P


def AbcCardHtml(
    name,
    age,
    address,
    number,
    status,
):
    return Div(
        {"class": "border rounded p-4 bg-white shadow-sm mb-3"},
        Div(
            {"class:": "flex items center justify-between"},
            P(
                {"class": "text-lg font-semibold"},
                f"{name} - {age}",
            ),
            P(
                {"class": "text-lg font-semibold"},
                f"{status}",
            ),
        ),
        Div(
            {"class": "grid grid-cols-1 md:grid-cols-3 gap-2 mt-3"},
            P(
                {"class": "text-sm"},
                f"Address: {address}",
            ),
            P(
                {"class": "text-sm"},
                f"number: {number}",
            ),
        ),
        Div(
            {"class": "flex items-center justify-between mt-3"},
            # RedirectButtonHtml(
            #     name=,
            #     url=details_url
            # )
            "GoToView",
        ),
    )
