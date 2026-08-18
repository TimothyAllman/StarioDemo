from pydantic import BaseModel
from pydantic import Field
from stario import Context
from stario import UrlPath
from stario import Writer
from stario import datastar

# 1. FIXED: Point to your Single Item SELECT module instead of your UPDATE module
from stariodemo.WebsiteFeatureWidgetPkg.FromWidgetDbTableSelectSingleItemModule import FromWidgetDbTableSelectSingleItem
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetDetailsModule import WidgetDetailsContentHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetDetailsModule import WidgetDetailsNoContentHtml

WIDGET_DETAILS_API_URL = UrlPath(
    "/widget-details-api/{id}",
)


class WidgetDetailsApiSignals(BaseModel):
    """
    Parses the target widget ID out of the active Datastar client signals.
    """

    widgetId: str = Field(alias="id")

    class Config:
        populate_by_name = True


async def ReadWidgetDetailsApiSignals(
    c: Context,
) -> WidgetDetailsApiSignals:
    # Read the active reactive signals payload transmitted by Datastar
    raw = await datastar.read_signals(c.req)
    return WidgetDetailsApiSignals.model_validate(raw)


def WidgetDetailsApiEndpoint():
    """
    Handles streaming specific single-widget details down to a
    reactive component container using Server-Sent Events (SSE).
    """

    async def handler(c: Context, w: Writer) -> None:
        signals = await ReadWidgetDetailsApiSignals(c)

        # 2. FIXED: Perform a clean query lookup using your select function
        widget_data = await FromWidgetDbTableSelectSingleItem(
            id=signals.widgetId,
        )

        sse = datastar.SSE(w)

        # 3. Stream the populated layout panel or the missing placeholder card
        if widget_data:
            sse.patch_elements(
                WidgetDetailsContentHtml(
                    widgetDto=widget_data,
                )
            )
        else:
            sse.patch_elements(WidgetDetailsNoContentHtml())

    return handler
