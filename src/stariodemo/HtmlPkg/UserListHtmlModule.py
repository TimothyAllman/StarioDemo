from stario.markup.html import Div

from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.HtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.HtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.HtmlPkg.UserCardHtmlModule import UserCardHtml


def UserListHtml():
    """
    docstring
    """

    cards = [
        UserCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
        UserCardHtml(
            name="Unknown",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
        UserCardHtml(
            name="user",
            age="Unknown",
            address="Unknown",
            number="Unknown",
            status="Unknown",
        ),
    ]

    noElements = CommonNothingToShowPlaceholderHtml(
        message="No user found. add your first user.",
        callToActionButton=CommonRedirectButtonHtml(
            name="Add New User",
            url=ABC_ADD_PAGE_URL,
        ),
    )

    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="Users",
        ),
        Div(
            {"class": "mt-3"},
            *cards if cards else [noElements],
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )
