from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.WebsiteFeatureHomePkg.HomeUrlsModule import HOME_PAGE_URL
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxErrorHtml
from stariodemo.WebsiteFeatureToastNotificationsPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification


def ToastErrorEndpoint(
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
                messageText="oh no",
            ),
        )

        # redirect
        sse = datastar.SSE(w)
        sse.navigate(HOME_PAGE_URL.href())

    return handler
