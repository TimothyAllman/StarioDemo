from stario.markup.html import Div

from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.HtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.HtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.HtmlPkg.AbcCardHtmlModule import AbcCardHtml


def AbcListHtml():
    """
    docstring
    """

    cards = [
        AbcCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
        AbcCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
        AbcCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
    ]

    noElements = CommonNothingToShowPlaceholderHtml(
        message="No abcxya list items found. add your first abcxyz.",
        callToActionButton=CommonRedirectButtonHtml(
            name="add thing",
            url=ABC_ADD_PAGE_URL,
        ),
    )

    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="List Abc",
        ),
        Div(
            {"class": "mt-3"},
            *cards if cards else [noElements],
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )
