import uuid

from stario import datastar
from stario.markup.html import Button
from stario.markup.html import Div

from stariodemo.DataStructsPkg.UrlsModule import SUBSCRIBE_TO_TOAST_NOTIFICATIONS_URL


def ToastNotificationsHtml():
    return Div(
        {
            "id": "toast-notifications-container",
            "class": "fixed right-4 bottom-4 top-1/2 z-[2147483647] w-[60vw] max-w-[60vw] flex flex-col justify-end gap-2 pointer-events-none",
        },
        datastar.data.init(
            datastar.at.get(SUBSCRIBE_TO_TOAST_NOTIFICATIONS_URL.href()),
        ),
        Div(
            {
                "id": "toast-messages-holder",
                "class": "space-y-2",
                "data-merge": "prepend",
            }
        ),
    )


def ToastNotificationItemHtml(
    message_box,
    toast_id: str | None = None,
):
    toast_dom_id = toast_id or f"toast-item-{uuid.uuid4().hex[:10]}"

    return Div(
        {
            "id": toast_dom_id,
            "data-toast-id": "1",
            "class": "pointer-events-auto-relative",
        },
        Button(
            {
                "type": "button",
                "class": "absolute top-1 right-1 h-6 w-6 rounded text-sm leading-none bg-backcolor1 border border-edgecolor1 text-frontcolor1",
                "aria-label": "Close Notification",
                "onclick": "(function(btn){var el=btn.closest('[data-toast-item]'); if(el){el.remove();}})(this)",
            },
            "x",
        ),
        message_box,
    )
