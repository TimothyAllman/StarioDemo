from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.HtmlPkg.ChatAppAvatarHtmlModule import ChatAppAvatarHtml
from stariodemo.HtmlPkg.ChatAppAvatarHtmlModule import ChatAppAvatarMoreHtml
from stariodemo.HtmlPkg.ChatAppAvatarsHtmlModule import ChatAppAvatarsHtml
from stariodemo.HtmlPkg.ChatAppOnlineLabelHtmlModule import ChatAppOnlineLabelHtml
from stariodemo.HtmlPkg.ChatAppOnlineUsersHtmlModule import ChatAppOnlineUsersHtml


def online_users_view(
    users: dict[str, ChatAppUserDto],
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
