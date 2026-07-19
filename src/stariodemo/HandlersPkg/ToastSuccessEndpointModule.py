from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.HandlersPkg.SubscribeToToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxErrorHtml


def ToastSuccessEndpoint(
    relay: Relay[str],
):
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """

        # do some stuff

        # do more stuff

        # publish notifications
        PublishToastNotification(
            relay=relay,
            message_box=MessageBoxErrorHtml(
                messageText="yay success",
            ),
        )

        # redirect
        sse = datastar.SSE(w)
        sse.navigate(HOME_PAGE_URL.href())

    return handler
