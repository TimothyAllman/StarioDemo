import time
import uuid

from stario import Context
from stario import Relay
from stario import Writer

from stariodemo.DataStructsPkg.MessageModule import MessageDto
from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.HandlersPkg import ChatSignals
from stariodemo.PiccoloPkg import PiccoloChatDb


def send_message(db: PiccoloChatDb, relay: Relay[str]):
    """
    Factory that returns message send handler with db and relay injected.

    Usage: app.post("/send", send_message(db, relay))
    """

    async def handler(c: Context, w: Writer) -> None:
        """Handle new message submission."""
        signals = await c.signals(ChatSignals)

        if not signals.user_id or not await db.user_exists(signals.user_id):
            w.redirect(HOME_PAGE_URL)
            return

        text = signals.message.strip()
        if not text:
            w.empty(204)
            return

        msg = MessageDto(
            id=str(uuid.uuid4())[:8],
            user_id=signals.user_id,
            username=signals.username,
            color=signals.color,
            text=text,
            timestamp=time.time(),
        )
        await db.add_message(msg)
        await db.set_user_typing(signals.user_id, False)

        c("Message sent", {"user_id": signals.user_id, "text": text[:50]})

        w.empty(204)
        relay.publish("update", "message")

    return handler
