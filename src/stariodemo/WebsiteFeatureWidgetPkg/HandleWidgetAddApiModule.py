import uuid
from typing import Any

from pydantic import BaseModel
from pydantic import model_validator
from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar

from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.WebsiteFeatureToastNotificationsPkg.SubscribeToastNotificationsEndpointModule import PublishToastNotification
from stariodemo.WebsiteFeatureWidgetPkg.FromWidgetDbTableInsertSingleItemModule import FromWidgetDbTableInsertSingleItem
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL


class WidgetAddSignals(BaseModel):
    """
    docstring
    """

    name: str
    age: int

    @model_validator(mode="before")
    @classmethod
    def handle_empty_age(cls, data: Any) -> Any:
        # If age arrives as an empty string or whitespace, turn it into 0
        if isinstance(data, dict):
            age_val = data.get("age")
            if isinstance(age_val, str) and not age_val.strip():
                data["age"] = 0
        return data


async def ReadWidgetAddSignals(
    c: Context,
) -> WidgetAddSignals:
    """
    docstring
    """
    # Read the full raw payload dictionary from Datastar's signals
    raw = await datastar.read_signals(
        c.req,
    )

    # Validate and parse via Pydantic model rules
    signals = WidgetAddSignals.model_validate(raw)

    return signals


def WidgetAddEndpoint(
    relay: Relay[str],
):
    """
    docstring
    """

    async def handler(c: Context, w: Writer) -> None:

        payload = await ReadWidgetAddSignals(c)

        await FromWidgetDbTableInsertSingleItem(
            id=uuid.uuid7(),
            name=payload.name,
            age=payload.age,
        )

        PublishToastNotification(
            relay=relay,
            message_box=MessageBoxSuccessHtml(messageText="Widget added"),
        )

        sse = datastar.SSE(w)
        sse.navigate(WIDGET_LIST_PAGE_URL.href())

    return handler
