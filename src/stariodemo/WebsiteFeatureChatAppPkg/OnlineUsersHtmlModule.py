from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppAvatarHtmlModule import ChatAppAvatarHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppAvatarHtmlModule import ChatAppAvatarMoreHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppAvatarsHtmlModule import ChatAppAvatarsHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppOnlineLabelHtmlModule import ChatAppOnlineLabelHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppOnlineUsersHtmlModule import ChatAppOnlineWidgetsHtml


def online_users_view(
    users: dict[str, ChatAppUserDto],
):
    """Shows online user avatars. Caps at 8 with a +N overflow indicator."""
    if not users:
        return ChatAppOnlineWidgetsHtml()

    return ChatAppOnlineWidgetsHtml(
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
