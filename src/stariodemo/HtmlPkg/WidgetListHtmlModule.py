from stario.markup.html import Div

from stariodemo.BasicStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.HtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.HtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.HtmlPkg.WidgetCardHtmlModule import WidgetCardHtml


def WidgetListHtml():
    """
    docstring
    """

    cards = [
        WidgetCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
        WidgetCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
        WidgetCardHtml(
            name="user",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
    ]

    noElementsCard = CommonNothingToShowPlaceholderHtml(
        message="No user found. add your first user.",
        callToActionButton=CommonRedirectButtonHtml(
            name="Add New Widget",
            url=ABC_ADD_PAGE_URL.href(),
        ),
    )

    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="Widgets",
        ),
        Div(
            {"class": "mt-3"},
            *cards
            if cards
            else [
                noElementsCard,
            ],
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )
