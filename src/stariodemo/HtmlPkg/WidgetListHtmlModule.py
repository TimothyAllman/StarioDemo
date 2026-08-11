from stario import datastar
from stario.markup.html import Div
from stario.markup.html import Input

from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_ADD_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_LIST_API_URL
from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetListDto
from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.HtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.HtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.HtmlPkg.WidgetCardHtmlModule import WidgetCardHtml


def WidgetListHtml(
    name_filter: str,
    status_filter: str,
):
    """
    Render Widget list html
    first filters then cards below.
    fetches cards via datastar `data.init()` on page load.
    initial filter values seed signals from url query params for bookmarkable urls.
    """

    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="Widget List",
        ),
        Div(
            {"class": "mt-4 p-4 bg-backcolor1 border border-edgecolor1 rounded-lg"},
            datastar.data.signals(
                {
                    "widget_name_filter": name_filter,
                    "widget_status_filter": status_filter,
                },
                if_missing=True,
            ),
            Div(
                Input(
                    {
                        "class": "form-control",
                        "type": "text",
                        "placeholder": "filter by name...",
                    },
                    datastar.data.bind("widget_name_filter"),
                    datastar.data.on(
                        "input",
                        datastar.at.get(WIDGET_LIST_API_URL.href()),
                    ),
                )
            ),
            Div(
                Input(
                    {
                        "class": "form-control",
                        "type": "text",
                        "placeholder": "filter by status...",
                    },
                    datastar.data.bind("widget_status_filter"),
                    datastar.data.on(
                        "input",
                        datastar.at.get(WIDGET_LIST_API_URL.href()),
                    ),
                )
            ),
        ),
        Div(
            {
                "id": __WIDGET_CARDS_ID,
            },
            datastar.data.init(
                datastar.at.get(WIDGET_LIST_API_URL.href()),
            ),
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )


__WIDGET_CARDS_ID = "__widget_cards_id"


def WidgetListCardsHtml(
    widgets: list[WidgetListDto],
):
    """
    This is the SSE section, so will take dtos in from an endpoint.
    Will be used on initial load.
    And when users filter the list
    """
    cards = [
        WidgetCardHtml(
            widgetDto=dto,
        )
        for dto in widgets
    ]

    noElementsCard = CommonNothingToShowPlaceholderHtml(
        message="No widget found. add your first widget.",
        callToActionButton=CommonRedirectButtonHtml(
            name="Add New Widget",
            url=WIDGET_ADD_PAGE_URL.href(),
        ),
    )

    return Div(
        {"id": __WIDGET_CARDS_ID},
        *cards
        if cards
        else [
            noElementsCard,
        ],
    )
