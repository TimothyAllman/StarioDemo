from stario import at
from stario import data
from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.HtmlComponentsPkg.DemoAppButtonHtmlModule import DemoAppButtonHtml
from stariodemo.HtmlHtmlsPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml


def AbcCalculationHtml(
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
            DemoAppButtonHtml(
                {"class": "border"},
                data.on("click", at.get(API_ABC_CALCULATION_URL)),
                "press me",
                buttoncolor="green",
            ),
        ),
        Div(
            {"class": "mt-3"},
            CalculationResultBoxHtml(
                result=" initialised",
            ),
        ),
    )
