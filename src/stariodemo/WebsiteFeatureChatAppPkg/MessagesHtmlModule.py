from stario import datastar

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppChatEmptyStateHtmlModule import ChatAppChatEmptyStateHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessagesHtmlModule import ChatAppMessagesHtml
from stariodemo.WebsiteFeatureChatAppPkg.MessageHtmlModule import message_view


def messages_view(
    current_user_id: str,
    messages: list[ChatAppMessageDto],
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
        datastar.data.on("load", "setTimeout(() => this.scrollTop = this.scrollHeight, 10)"),
        *[message_view(msg, current_user_id) for msg in messages],
    )
