from stario import Context
from stario import Relay
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppRelaysModule import CHAT_TYPING
from stariodemo.WebsiteFeatureChatAppPkg.ChatSignalsModule import read_chat_signal


def TypingEndpoint(
    relay: Relay[str],
):
    """
    Factory that returns typing indicator handler with db and relay injected.
    Update typing indicator status.
    Usage: app.post("/typing", typing(db, relay))

    """

    async def handler(c: Context, w: Writer) -> None:

        signals = await read_chat_signal(c)

        if not signals.user_id or not await db.user_exists(signals.user_id):
            responses.empty(w, 204)
            return

        is_typing = bool(signals.message.strip())

        if await db.set_user_typing(signals.user_id, is_typing):
            relay.publish(CHAT_TYPING, "changed")

        responses.empty(w, 204)

    return handler
