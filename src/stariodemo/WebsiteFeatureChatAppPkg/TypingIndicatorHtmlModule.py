from stario.markup.html import Div
from stario.markup.html import Span

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDto


def typing_indicator_view(
    current_user_id: str,
    users: dict[str, ChatAppUserDto],
):
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
        Span(
            {"class": "typing-text"},
            text,
        ),
        Span(
            {"class": "typing-dots"},
            Span({"class": "dot"}, "."),
            Span({"class": "dot"}, "."),
            Span({"class": "dot"}, "."),
        ),
    )
