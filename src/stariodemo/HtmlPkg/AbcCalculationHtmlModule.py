from stario import datastar
from stario.markup.html import Div

from stariodemo.BasicStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.DemoAppButtonHtmlModule import DemoAppButtonHtml
from stariodemo.HtmlPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml


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
                datastar.data.on("click", datastar.at.get(API_ABC_CALCULATION_URL.href())),
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
