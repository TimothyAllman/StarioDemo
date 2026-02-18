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


def typing_indicator_view(current_user_id: str, users: dict[str, User]):
    """
    Shows who's typing.

    Filters out the current user - you don't need to see your own typing indicator.
    Returns hidden div when nobody is typing (preserves element for patching).
    """
    typing_users = [user for user in users.values() if user.typing and user.id != current_user_id]

    if not typing_users:
        return Div({"id": "typing", "class": "typing-indicator hidden"})

    if len(typing_users) == 1:
        text = f"{typing_users[0].username} is typing"
    elif len(typing_users) == 2:
        text = f"{typing_users[0].username} and {typing_users[1].username} are typing"
    else:
        text = f"{typing_users[0].username} and {len(typing_users) - 1} others are typing"

    return Div(
        {"id": "typing", "class": "typing-indicator"},
        Span({"class": "typing-text"}, text),
        Span(
            {"class": "typing-dots"},
            Span({"class": "dot"}, "."),
            Span({"class": "dot"}, "."),
            Span({"class": "dot"}, "."),
        ),
    )
