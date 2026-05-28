from stario import at
from stario import data
from stario.html import Div

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
    - data.signals({...}, ifmissing=True): initializes client state (only if not set)
    - data.init(at.get("/subscribe")): opens SSE connection on page load
    """
    return Div(
        {"id": "__chat"},  # NB NB NB w.patch(chatview()) does not work if there is no id on the top level div that is returned
        # toy_inspector(),  # Dev tool: shows current signals state
        Div(
            {"class": "chat-container"},
            data.signals(
                {"user_id": user_id, "username": username, "color": color, "message": ""},
                ifmissing=True,
            ),
            data.init(at.get("/subscribe")),
            Div(
                {"class": "chat-header"},
                Div({"class": "chat-title"}, "Stario Chat 🐾"),
                online_users_view(users),
            ),
            Div(
                {"class": "chat-body"},
                messages_view(user_id, messages),
                typing_indicator_view(user_id, users),
            ),
            Div(
                {"class": "chat-footer"},
                input_form_view(),
            ),
        ),
    )
