from stario import datastar
from stario.markup.html import Div

from stariodemo.BasicStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.WebsiteFeatureAbcPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.DemoAppButtonHtmlModule import DemoAppButtonHtml


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
