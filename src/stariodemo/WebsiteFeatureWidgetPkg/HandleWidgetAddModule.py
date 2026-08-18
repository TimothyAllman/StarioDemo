from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.WebsiteFeatureWidgetPkg.FromWidgetDbTableInsertSingleItemModule import FromWidgetDbTableInsertSingleItem
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.WebsiteFeatureToastNotificationsPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WidgetAddSignals


async def ReadWidgetAddSignals(
    c: Context,
) -> WidgetAddSignals:
    """
    docstring
    """

    parsedName = c.route.params.get("name", "").strip()
    parseAge = c.route.params.get("age", "").strip()

    signals = WidgetAddSignals(
        name=parsedName,
        age=int(parseAge),
    )

    return signals


def WidgetAddEndpoint(
    relay: Relay[str],
):
    """
    Serve abc list page
    """

    async def handler(c: Context, w: Writer) -> None:

        payload = await ReadWidgetAddSignals(c)

        await FromWidgetDbTableInsertSingleItem(
            widgetAddSignal=payload,
        )

        PublishToastNotification(
            relay=relay,
            message_box=MessageBoxSuccessHtml(messageText="Widget added"),
        )

        sse = datastar.SSE(w)
        sse.navigate(WIDGET_LIST_PAGE_URL.href())

    return handler
