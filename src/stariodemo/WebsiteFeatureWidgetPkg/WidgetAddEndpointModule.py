from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_LIST_PAGE_URL
from stariodemo.FromTableDatabaseFunctionsPkg.FromWidgetDbTableInsertSingleItemModule import FromWidgetDbTableInsertSingleItem
from stariodemo.GoUrlsPkg.WidgetAddUrlModule import ReadWidgetAddSignals
from stariodemo.WebsiteFeatureToastNotificationsPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml


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
