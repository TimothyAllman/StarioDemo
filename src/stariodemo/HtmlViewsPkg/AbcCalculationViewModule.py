from stario import at
from stario import data
from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.HtmlComponentsPkg.DemoAppButtonModule import DemoAppButton
from stariodemo.HtmlViewsPkg.CalculationResultBoxViewModule import CalculationResultBoxView


def AbcCalculationView(
    # user_id: str,
    # username: str,
    # color: str,
    # *,
    # messages: list[Message],
    # users: dict[str, User],
):
    """
    docstring
    """

    return Div(
        Div("abc calc"),
        Div(
            {"class": ""},
            DemoAppButton(
                {"class": "border"},
                data.on("click", at.get(API_ABC_CALCULATION_URL)),
                "press me",
            ),
        ),
        Div(
            {"class": "mt-3"},
            CalculationResultBoxView(
                result=" initialised",
            ),
        ),
    )
