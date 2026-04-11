import time

from stario.html import Div
from stario.html import Span

from stariodemo.DataStructsPkg.MessageModule import MessageDto


def message_view(
    msg: MessageDto,
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
