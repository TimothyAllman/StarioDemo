import time
import uuid

from stario import Context
from stario import Relay
from stario import Writer
from stario import responses

from stariodemo.DataStructsPkg.RelayTopicsModule import CHAT_MESSAGE
from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.PiccoloPkg import PiccoloChatDb
from stariodemo.PiccoloPkg.MessageDbModule import MessageDto
from stariodemo.SignalsPkg.ChatSignalsModule import read_chat_signal


def SendMessageEndpoint(db: PiccoloChatDb, relay: Relay[str]):
    """
    Factory that returns message send handler with db and relay injected.

    Usage: app.post("/send", send_message(db, relay))
    """

    async def handler(c: Context, w: Writer) -> None:
        """Handle new message submission."""
        signals = await read_chat_signal(c)

        if not signals.user_id or not await db.user_exists(signals.user_id):
            responses.redirect(w, HOME_PAGE_URL)
            return

        text = signals.message.strip()
        if not text:
            responses.empty(w, 204)
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

        c.span.event(
            "Message sent",
            {"user_id": signals.user_id, "text": text[:50]},
        )

        responses.empty(w, 204)
        relay.publish(CHAT_MESSAGE, "new")

    return handler
