from stariodemo.HtmlHtmlsPkg.ChatAppAvatarHtmlModule import ChatAppAvatarHtml, ChatAppAvatarMoreHtml
from stariodemo.HtmlHtmlsPkg.ChatAppAvatarsHtmlModule import ChatAppAvatarsHtml
from stariodemo.HtmlHtmlsPkg.ChatAppOnlineLabelHtmlModule import ChatAppOnlineLabelHtml
from stariodemo.HtmlHtmlsPkg.ChatAppOnlineUsersHtmlModule import ChatAppOnlineUsersHtml
from stariodemo.PiccoloPkg.UserDbModule import UserDto


def online_users_view(
    users: dict[str, UserDto],
):
    """Shows online user avatars. Caps at 8 with a +N overflow indicator."""
    if not users:
        return ChatAppOnlineUsersHtml()

    return ChatAppOnlineUsersHtml(
        ChatAppOnlineLabelHtml(
            f"{len(users)} online",
        ),
        ChatAppAvatarsHtml(
            *[
                ChatAppAvatarHtml(
                    avatar_text=user.username[0].upper(),
                    avatar_title=user.username,
                    avatar_color=user.color,
                )
                for user in list(users.values())[:8]
            ],
            *(
                [
                    ChatAppAvatarMoreHtml(
                        f"+{len(users) - 8}",
                    )
                ]
                if len(users) > 8
                else []
            ),
        ),
    )
