from stario import datastar
from stario.markup.html import Div
from stario.markup.html import Input
from stario.markup.html import P

from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonActionButtonHtmlModule import CommonActionButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetListDto
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetDeleteModule import WIDGET_DELETE_API_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_DETAILS_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_API_URL


def WidgetListContainerHtml(
    *children,
):
    return Div(
        {
            "id": "__widget_cards_id",
        },
        *children,
    )


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
        WidgetListContainerHtml(
            datastar.data.init(
                datastar.at.get(WIDGET_LIST_API_URL.href()),
            ),
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )


def WidgetListContentHtml(
    widgets: list[WidgetListDto],
):
    """
    This is the SSE section, so will take dtos in from an endpoint.
    Will be used on initial load.
    And when users filter the list
    """
    cards = [
        WidgetListCardHtml(
            widgetDto=dto,
        )
        for dto in widgets
    ]

    return WidgetListContainerHtml(
        cards,
    )


def WidgetListNoContentHtml():
    noElementsCard = CommonNothingToShowPlaceholderHtml(
        message="No widget found. add your first widget.",
        callToActionButton=CommonRedirectButtonHtml(
            name="Add New Widget",
            url=WIDGET_ADD_PAGE_URL.href(),
        ),
    )

    return WidgetListContainerHtml(
        noElementsCard,
    )


def WidgetListCardHtml(
    widgetDto,
):
    return Div(
        {"class": "border rounded p-4 bg-backcolor1 text-frontcolor1 border-edgecolor1 shadow-sm mb-3"},
        Div(
            {"class:": "flex items center justify-between"},
            P(
                {"class": "text-lg font-semibold"},
                f"{widgetDto.id} - {widgetDto.name}",
            ),
            P(
                {"class": "text-lg font-semibold"},
                f"{widgetDto.name}",
            ),
        ),
        Div(
            {"class": "grid grid-cols-1 md:grid-cols-3 gap-2 mt-3"},
            P(
                {"class": "text-sm"},
                f"Address: {widgetDto.name}",
            ),
            P(
                {"class": "text-sm"},
                f"number: {widgetDto.username}",
            ),
        ),
        # Div(
        #     {"class": "flex items-center justify-between mt-3"},
        #     # RedirectButtonHtml(
        #     #     name=,
        #     #     url=details_url
        #     # )
        #     "GoToView",
        # ),
        CommonActionButtonHtml(
            buttonText="delete",
            buttonHref=WIDGET_DELETE_API_URL.href(id=widgetDto.id),
        ),
        CommonRedirectButtonHtml(
            name="details",
            url=WIDGET_DETAILS_PAGE_URL.href(id=widgetDto.id),
        ),
    )
