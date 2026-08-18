from pydantic import BaseModel
from pydantic import Field
from stario import Context
from stario import Relay
from stario import UrlPath
from stario import Writer
from stario import datastar

from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.WebsiteFeatureToastNotificationsPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.WebsiteFeatureWidgetPkg.FromWidgetDbTableDeleteSingleItemModule import FromWidgetDbTableDeleteSingleItem
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL

WIDGET_DELETE_API_URL = UrlPath("/widget-delete/{id}")


class WidgetDeleteSignals(BaseModel):
    """
    docstring
    """

    # Using Field alias to map the path variable 'id' directly to 'widgetId'
    widgetId: str = Field(alias="id")

    class Config:
        # Allows populating by field name or alias
        populate_by_name = True


async def ReadWidgetDeleteSignals(
    c: Context,
) -> WidgetDeleteSignals:
    # 1. Grab the raw routing parameters dictionary from the context
    raw_params = c.route.params

    # 2. Use Pydantic's official dictionary validation entry point
    signals = WidgetDeleteSignals.model_validate(raw_params)

    return signals


def WidgetDeleteEndpoint(
    relay: Relay[str],
):
    """
    docstring
    """

    async def handler(c: Context, w: Writer) -> None:

        payload = await ReadWidgetDeleteSignals(c)

        if payload.widgetId:
            c.span.event(
                "widget.being.deleted",
                {
                    "widget.id": payload.widgetId,
                },
            )

        await FromWidgetDbTableDeleteSingleItem(
            id=payload.widgetId,
        )

        PublishToastNotification(
            relay=relay,
            message_box=MessageBoxSuccessHtml(messageText="Widget deleted"),
        )

        sse = datastar.SSE(w)
        sse.navigate(WIDGET_LIST_PAGE_URL.href())

    return handler
