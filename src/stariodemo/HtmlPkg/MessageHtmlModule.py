import time

from stariodemo.DatabasePiccoloTablesPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.HtmlPkg.ChatAppMessageBubbleHtmlModule import ChatAppMessageBubbleHtml
from stariodemo.HtmlPkg.ChatAppMessageBubbleHtmlModule import ChatAppMessageHeaderHtml
from stariodemo.HtmlPkg.ChatAppMessageUsernameHtmlModule import ChatAppMessageTextHtml
from stariodemo.HtmlPkg.ChatAppMessageUsernameHtmlModule import ChatAppTimestampHtml
from stariodemo.HtmlPkg.ChatAppMessageUsernameHtmlModule import ChatAppUsernameHtml


def message_view(
    msg: ChatAppMessageDto,
    current_user_id: str,
):
    """Single chat message bubble. Own messages get different styling."""
    is_own = msg.user_id == current_user_id
    msg_time = time.strftime("%H:%M", time.localtime(msg.timestamp))

    return ChatAppMessageBubbleHtml(
        ChatAppMessageHeaderHtml(
            ChatAppUsernameHtml(
                username_text=msg.username,
                username_color=msg.color,
            ),
            ChatAppTimestampHtml(
                msg_time,
            ),
            is_own=is_own,
        ),
        ChatAppMessageTextHtml(
            msg.text,
        ),
        is_own=is_own,
        msg_id=msg.id,
    )
