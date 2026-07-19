from stario.markup.html import Div

from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_ADD_PAGE_URL
from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetListDto
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.HtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.HtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.HtmlPkg.WidgetCardHtmlModule import WidgetCardHtml


async def WidgetListHtml():
    """
    docstring
    """

    # widgets = await FromWidgetDbTableSelectAllItems()
    dtos = [
        WidgetListDto(
            id="asd",
            username="asd",
            name="Asd",
        ),
        WidgetListDto(
            id="asd",
            username="asd",
            name="Asd",
        ),
        WidgetListDto(
            id="asd",
            username="asd",
            name="Asd",
        ),
    ]

    cards = [
        WidgetCardHtml(
            widgetDto=dto,
        )
        for dto in dtos
    ]

    noElementsCard = CommonNothingToShowPlaceholderHtml(
        message="No user found. add your first user.",
        callToActionButton=CommonRedirectButtonHtml(
            name="Add New Widget",
            url=WIDGET_ADD_PAGE_URL.href(),
        ),
    )

    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="Widget List",
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
