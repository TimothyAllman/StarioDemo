from stario import datastar
from stario.html import Div

from stariodemo.DataStructsPkg.UrlsModule import CHAT_SUBSCRIBE_URL
from stariodemo.HtmlHtmlsPkg.ChatAppChatBodyHtmlModule import ChatAppChatBodyHtml
from stariodemo.HtmlHtmlsPkg.ChatAppChatContainerHtmlModule import ChatAppChatContainerHtml
from stariodemo.HtmlHtmlsPkg.ChatAppChatFooterHtmlModule import ChatAppChatFooterHtml
from stariodemo.HtmlHtmlsPkg.ChatAppChatHeaderHtmlModule import ChatAppChatHeaderHtml
from stariodemo.HtmlHtmlsPkg.ChatAppChatTitleHtmlModule import ChatAppChatTitleHtml
from stariodemo.HtmlHtmlsPkg.InputFormHtmlModule import input_form_view
from stariodemo.HtmlHtmlsPkg.MessagesHtmlModule import messages_view
from stariodemo.HtmlHtmlsPkg.OnlineUsersHtmlModule import online_users_view
from stariodemo.HtmlHtmlsPkg.TypingIndicatorHtmlModule import typing_indicator_view
from stariodemo.PiccoloPkg.MessageDbModule import MessageDto
from stariodemo.PiccoloPkg.UserDbModule import UserDto


def chat_view(
    user_id: str,
    username: str,
    color: str,
    *,
    messages: list[MessageDto],
    users: dict[str, UserDto],
):
    """
    Main chat page.

    This view is rendered on initial load AND on every SSE patch.
    Datastar efficiently diffs and updates only changed parts of the DOM.

    Args:
        user_id: Current user's ID
        username: Current user's display name
        color: Current user's avatar color
        messages: List of chat messages to display
        users: Dict of online users

    Key setup:
    - datastar.signals({...}, ifmissing=True): initializes client state (only if not set)
    - datastar.init(at.get("/subscribe")): opens SSE connection on page load
    """
    return Div(
        {"id": "__chat"},  # NB NB NB datastar.sse.patch_elements(w,chatview()) does not work if there is no id on the top level div that is returned
        # toy_inspector(),  # Dev tool: shows current signals state
        ChatAppChatContainerHtml(
            datastar.signals(
                {"user_id": user_id, "username": username, "color": color, "message": ""},
                ifmissing=True,
            ),
            datastar.init(datastar.get(CHAT_SUBSCRIBE_URL)),
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
