from stario.html import Div
from stario.html import Span

from stariodemo.DataStructsPkg.UserModule import UserDto


def online_users_view(
    users: dict[str, UserDto],
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
