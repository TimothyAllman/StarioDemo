from stario import data
from stario.html import Div

from stariodemo.HtmlHtmlsPkg.MessageHtmlModule import message_view
from stariodemo.PiccoloPkg.MessageDbModule import MessageDto


def messages_view(
    current_user_id: str,
    messages: list[MessageDto],
):
    """
    Message list container.

    The data.on("load", ...) scrolls to bottom when new content loads.
    This runs client-side after Datastar merges the patch into the DOM.
    """
    if not messages:
        return Div(
            {"id": "messages", "class": "messages empty"},
            Div({"class": "empty-state"}, "No messages yet. Say hello!"),
        )

    return Div(
        {"id": "messages", "class": "messages"},
        data.on("load", "setTimeout(() => this.scrollTop = this.scrollHeight, 10)"),
        *[message_view(msg, current_user_id) for msg in messages],
    )
