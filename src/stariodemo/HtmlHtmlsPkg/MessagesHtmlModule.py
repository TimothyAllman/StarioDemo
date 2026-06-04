from stario import datastar

from stariodemo.HtmlHtmlsPkg.ChatAppChatEmptyStateHtmlModule import ChatAppChatEmptyStateHtml
from stariodemo.HtmlHtmlsPkg.ChatAppMessagesHtmlModule import ChatAppMessagesHtml
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
        return ChatAppMessagesHtml(
            ChatAppChatEmptyStateHtml(),
            extra_classes="empty justify-center items-center",
        )

    return ChatAppMessagesHtml(
        datastar.on("load", "setTimeout(() => this.scrollTop = this.scrollHeight, 10)"),
        *[message_view(msg, current_user_id) for msg in messages],
    )
