from stario import datastar
from stario.markup.html import Div
from stario.markup.html import P
from stario.markup.html import Span
from stario.markup.html import Strong

from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonNothingToShowPlaceholderHtmlModule import CommonNothingToShowPlaceholderHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonRedirectButtonHtmlModule import CommonRedirectButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml
from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDetailsDto
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_DETAILS_API_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL


def WidgetDetailsContainerHtml(
    *children,
):
    """
    Acts as the target DOM container for dynamic SSE element patching.
    """
    return Div(
        {
            "id": "__widget_details_container_id",
        },
        *children,
    )


def WidgetDetailsHtml(
    widget_id: str,
):
    """
    Renders the Widget Details base layout.
    Fetches inner template markup asynchronously via Datastar `data.init()`.
    Passes the ID string into local signals for API request routing.
    """
    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="Widget Details View",
        ),
        Div(
            # Seeds local Datastar state tracking with the target widget ID
            datastar.data.signals(
                {
                    "id": widget_id,
                },
                if_missing=True,
            ),
        ),
        # On load, Datastar executes an SSE GET to pull down the dynamic details layout
        WidgetDetailsContainerHtml(
            datastar.data.init(
                datastar.at.get(
                    WIDGET_DETAILS_API_URL.href(id=widget_id),
                ),
            ),
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )


def WidgetDetailsContentHtml(
    widgetDto: WidgetDetailsDto,
):
    """
    The dynamic SSE block streamed by your details API endpoint.
    Displays individual property elements in an elegant panel layout.
    """
    return WidgetDetailsContainerHtml(
        Div(
            {"class": "border rounded p-6 bg-backcolor1 text-frontcolor1 border-edgecolor1 shadow-sm max-w-xl"},
            Div(
                {"class": "flex items-center justify-between border-b border-edgecolor1 pb-3 mb-4"},
                P(
                    {"class": "text-xl font-bold"},
                    f"Profile: {widgetDto.name}",
                ),
            ),
            Div(
                {"class": "space-y-3 mb-6"},
                P(
                    {"class": "text-sm text-gray-500 font-mono"},
                    f"System ID: {widgetDto.id}",
                ),
                P(
                    {"class": "text-base"},
                    Strong("Operational Name: "),
                    Span(widgetDto.name),
                ),
                P(
                    {"class": "text-base"},
                    Strong("Calculated Age: "),
                    Span(f"{widgetDto.username} cycles"),
                ),
            ),
            Div(
                {"class": "pt-4 border-t border-edgecolor1"},
                CommonRedirectButtonHtml(
                    name="Return to Index",
                    url=WIDGET_LIST_PAGE_URL.href(),
                ),
            ),
        )
    )


def WidgetDetailsNoContentHtml():
    """
    Fallback card display to handle missing or deleted records gracefully.
    """
    noElementCard = CommonNothingToShowPlaceholderHtml(
        message="The requested widget details could not be found or has been removed.",
        callToActionButton=CommonRedirectButtonHtml(
            name="Back to Widget List",
            url=WIDGET_LIST_PAGE_URL.href(),
        ),
    )

    return WidgetDetailsContainerHtml(
        noElementCard,
    )
