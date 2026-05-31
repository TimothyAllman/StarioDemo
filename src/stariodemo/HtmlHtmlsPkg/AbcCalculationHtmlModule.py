from stario import datastar
from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.DemoAppButtonHtmlModule import DemoAppButtonHtml
from stariodemo.HtmlHtmlsPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml


def AbcCalculationHtml():
    """
    docstring
    """

    return CommonMainMiddleSectionHtml(
        BigTitleHtml("abc calc"),
        Div(
            {"class": ""},
            DemoAppButtonHtml(
                {"class": "border"},
                datastar.on("click", datastar.get(API_ABC_CALCULATION_URL)),
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
        rightSidebar=None,
    )
