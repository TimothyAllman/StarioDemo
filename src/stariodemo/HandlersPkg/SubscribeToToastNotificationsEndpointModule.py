import uuid
from collections import deque
from typing import Any

from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.DataStructsPkg.RelayTopicsModule import RELAY_TOAST_NOTIFICATIONS_SUBSCRIBE_PATTERN
from stariodemo.HtmlComponentsPkg.ToastNotificationsHtmlModule import ToastNotificationItemHtml

_PENDING_TOAST_NOTIFICATIONS: deque[object] = deque()


def PublishToastNotification(
    relay: Relay[Any],
    message_box,
) -> None:
    _PENDING_TOAST_NOTIFICATIONS.append(message_box)

    relay.publish(
        RELAY_TOAST_NOTIFICATIONS_SUBSCRIBE_PATTERN,
        message_box,
    )


def SubscribeToToastNotificationsEndpoint(
    relay: Relay[str],
):
    """
    docstring
    """

    async def handler(c: Context, w: Writer) -> None:

        sse = datastar.SSE(w)

        def patch_toast(message_box) -> None:
            toast_id = f"toast-item-{uuid.uuid4().hex[:10]}"
            sse.patch_elements(
                ToastNotificationItemHtml(
                    message_box=message_box,
                    toast_id=toast_id,
                ),
                mode="append",
                selector="#toast-messages-holder",
            )
            sse.execute_script(
                f"setTimeout(()=> document.getElementById('{toast_id}')?.remove(),4000);",
            )

        while _PENDING_TOAST_NOTIFICATIONS:
            patch_toast(
                _PENDING_TOAST_NOTIFICATIONS.popleft(),
            )

        async with relay.subscribe(RELAY_TOAST_NOTIFICATIONS_SUBSCRIBE_PATTERN) as live:
            async for _, payload in c.alive(live):
                patch_toast(
                    payload,
                )

    return handler
