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


def online_users_view(
    users: dict[str, User],
):
    """Shows online user avatars. Caps at 8 with a +N overflow indicator."""
    if not users:
        return Div({"id": "online", "class": "online-users"})

    return Div(
        {"id": "online", "class": "online-users"},
        Span({"class": "online-label"}, f"{len(users)} online"),
        Div(
            {"class": "avatars"},
            *[
                Span(
                    {
                        "class": "avatar",
                        "style": {"background-color": user.color},
                        "title": user.username,
                    },
                    user.username[0].upper(),
                )
                for user in list(users.values())[:8]
            ],
            *([Span({"class": "avatar more"}, f"+{len(users) - 8}")] if len(users) > 8 else []),
        ),
    )
