from stario import datastar
from stario.markup.html import Div

from stariodemo.DatabasePiccoloTablesPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.DataStructsPkg.UrlsModule import CHAT_SUBSCRIBE_URL
from stariodemo.HtmlPkg.ChatAppChatBodyHtmlModule import ChatAppChatBodyHtml
from stariodemo.HtmlPkg.ChatAppChatContainerHtmlModule import ChatAppChatContainerHtml
from stariodemo.HtmlPkg.ChatAppChatFooterHtmlModule import ChatAppChatFooterHtml
from stariodemo.HtmlPkg.ChatAppChatHeaderHtmlModule import ChatAppChatHeaderHtml
from stariodemo.HtmlPkg.ChatAppChatTitleHtmlModule import ChatAppChatTitleHtml
from stariodemo.HtmlPkg.InputFormHtmlModule import input_form_view
from stariodemo.HtmlPkg.MessagesHtmlModule import messages_view
from stariodemo.HtmlPkg.OnlineUsersHtmlModule import online_users_view
from stariodemo.HtmlPkg.TypingIndicatorHtmlModule import typing_indicator_view


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
