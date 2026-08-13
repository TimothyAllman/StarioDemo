from stario.markup.html import Div

from stariodemo.BasicStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.WebsiteFeatureAbcPkg.AbcCardHtmlModule import AbcCardHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml


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
            url=ABC_ADD_PAGE_URL.href(),
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
