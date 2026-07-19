from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.BasicStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.HandlersPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml


def ToastSuccessEndpoint(
    relay: Relay[str],
):
    """
    docstring
    """

    async def handler(c: Context, w: Writer) -> None:

        # do some stuff

        # do more stuff

        # publish notifications
        PublishToastNotification(
            relay=relay,
            message_box=MessageBoxSuccessHtml(
                messageText="yay success",
            ),
        )

        # redirect
        sse = datastar.SSE(w)
        sse.navigate(HOME_PAGE_URL.href())

    return handler
