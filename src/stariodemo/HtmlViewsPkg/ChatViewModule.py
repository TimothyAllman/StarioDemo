import time

from stario import asset
from stario import at
from stario import data
from stario.html import Body
from stario.html import Button
from stario.html import Div
from stario.html import Form
from stario.html import Head
from stario.html import Html
from stario.html import Input
from stario.html import Link
from stario.html import Meta
from stario.html import SafeString
from stario.html import Script
from stario.html import Span
from stario.html import Title
from stario.toys import toy_inspector

from stariodemo.DataStructsPkg.MessageModule import Message
from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.HtmlComponentsPkg.FooterBarModule import FooterBar
from stariodemo.HtmlViewsPkg.InputFormViewModule import input_form_view
from stariodemo.HtmlViewsPkg.MessagesViewModule import messages_view
from stariodemo.HtmlComponentsPkg.NavBarModule import NavBar
from stariodemo.HtmlViewsPkg.OnlineUsersViewModule import online_users_view
from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.TypingIndicatorViewModule import typing_indicator_view


def chat_view(
    user_id: str,
    username: str,
    color: str,
    *,
    messages: list[Message],
    users: dict[str, User],
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
    return page(
        NavBar(),
        toy_inspector(),  # Dev tool: shows current signals state
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
        FooterBar(),
    )
