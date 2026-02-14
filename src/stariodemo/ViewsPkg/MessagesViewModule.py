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
from stariodemo.ViewsPkg.MessageViewModule import message_view


def messages_view(
    current_user_id: str,
    messages: list[Message],
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
