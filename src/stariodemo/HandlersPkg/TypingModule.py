from stario import Context, Relay, Writer
from stariodemo.DataBasePkg.db import Database
from stariodemo.HandlersPkg import ChatSignals


def typing(db: Database, relay: Relay[str]):
    """
    Factory that returns typing indicator handler with db and relay injected.

    Usage: app.post("/typing", typing(db, relay))
    """

    async def handler(c: Context, w: Writer) -> None:
        """Update typing indicator status."""
        signals = await c.signals(ChatSignals)

        if not signals.user_id or not db.user_exists(signals.user_id):
            w.empty(204)
            return

        is_typing = bool(signals.message.strip())

        if db.set_user_typing(signals.user_id, is_typing):
            relay.publish("update", "typing")

        w.empty(204)

    return handler
