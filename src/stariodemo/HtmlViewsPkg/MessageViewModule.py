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

from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.DataStructsPkg.MessageModule import Message


def message_view(
    msg: Message,
    current_user_id: str,
):
    """Single chat message bubble. Own messages get different styling."""
    is_own = msg.user_id == current_user_id
    bubble_class = "message own" if is_own else "message"
    msg_time = time.strftime("%H:%M", time.localtime(msg.timestamp))

    return Div(
        {"class": bubble_class, "data-msg-id": msg.id},
        Div(
            {"class": "message-header"},
            Span(
                {"class": "username", "style": {"color": msg.color}},
                msg.username,
            ),
            Span({"class": "timestamp"}, msg_time),
        ),
        Div({"class": "message-text"}, msg.text),
    )
