from dataclasses import dataclass

from stario import Context
from stario import Relay
from stario import UrlPath
from stario import Writer
from stario import datastar

from stariodemo.WebsiteFeatureWidgetPkg.FromWidgetDbTableDeleteSingleItemModule import FromWidgetDbTableDeleteSingleItem
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.WebsiteFeatureToastNotificationsPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL

WIDGET_DELETE_URL = UrlPath("/widget-delete/{id}")


@dataclass
class WidgetDeleteSignals:
    """
    docstring
    """

    widgetId: str


async def ReadWidgetDeleteSignals(
    c: Context,
) -> WidgetDeleteSignals:

    parsedId = c.route.params.get("id", "").strip()

    signals = WidgetDeleteSignals(
        widgetId=parsedId,
    )

    return signals


def WidgetDeleteEndpoint(
    relay: Relay[str],
):
    """
    Serve abc list page
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

        PublishToastNotification(relay=relay, message_box=MessageBoxSuccessHtml(messageText="Widget deleted"))

        sse = datastar.SSE(w)
        sse.navigate(WIDGET_LIST_PAGE_URL.href())

    return handler
