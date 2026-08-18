from stario import datastar
from stario.markup.html import Div

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppChatBodyHtmlModule import ChatAppChatBodyHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppChatContainerHtmlModule import ChatAppChatContainerHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppChatFooterHtmlModule import ChatAppChatFooterHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppChatHeaderHtmlModule import ChatAppChatHeaderHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppChatTitleHtmlModule import ChatAppChatTitleHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_SUBSCRIBE_URL
from stariodemo.WebsiteFeatureChatAppPkg.InputFormHtmlModule import input_form_view
from stariodemo.WebsiteFeatureChatAppPkg.MessagesHtmlModule import messages_view
from stariodemo.WebsiteFeatureChatAppPkg.OnlineUsersHtmlModule import online_users_view
from stariodemo.WebsiteFeatureChatAppPkg.TypingIndicatorHtmlModule import typing_indicator_view


def chat_view(
    user_id: str,
    username: str,
    color: str,
    *,
    messages: list[ChatAppMessageDto],
    users: dict[str, ChatAppUserDto],
):
    """
    Main chat page.

    """
    return Div(
        {"id": "__chat"},  # NB NB NB datastar.data.sse.patch_elements(w,chatview()) does not work if there is no id on the top level div that is returned
        # toy_inspector(),  # Dev tool: shows current signals state
        ChatAppChatContainerHtml(
            datastar.data.signals(
                {"user_id": user_id, "username": username, "color": color, "message": ""},
                if_missing=True,
            ),
            datastar.data.init(datastar.at.get(CHAT_SUBSCRIBE_URL.href())),
            ChatAppChatHeaderHtml(
                ChatAppChatTitleHtml("Stario Chat 🐾"),
                online_users_view(users),
            ),
            ChatAppChatBodyHtml(
                messages_view(user_id, messages),
                typing_indicator_view(user_id, users),
            ),
            ChatAppChatFooterHtml(
                input_form_view(),
            ),
        ),
    )
