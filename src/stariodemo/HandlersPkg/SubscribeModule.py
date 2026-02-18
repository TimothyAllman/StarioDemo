from stario import Context, Relay, Writer
from stariodemo.DataBasePkg.db import Database
from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.HandlersPkg import ChatSignals
from stariodemo.HtmlViewsPkg.ChatViewModule import chat_view


def subscribe(db: Database, relay: Relay[str]):
    """
    Factory that returns SSE subscription handler with db and relay injected.

    Usage: app.get("/subscribe", subscribe(db, relay))
    """

    async def handler(c: Context, w: Writer) -> None:
        """
        SSE endpoint for real-time updates.

        1. Client connects (triggered by data.init in the HTML)
        2. We register them in the database
        3. We send initial state via w.patch()
        4. We loop, waiting for relay events and sending patches
        5. When client disconnects, the loop exits and we clean up
        """
        signals = await c.signals(ChatSignals)

        if not signals.user_id:
            w.redirect("/")
            return

        # Add user to database
        user = User(
            id=signals.user_id,
            username=signals.username,
            color=signals.color,
        )
        db.add_user(user)
        c("User connected", {"user_id": signals.user_id, "username": signals.username})

        # Tell everyone that someone joined
        relay.publish("update", "presence")

        # Send current state immediately
        w.patch(
            chat_view(
                signals.user_id,
                signals.username,
                signals.color,
                messages=db.get_messages(),
                users=db.get_users(),
            )
        )

        # Main loop: wait for events, send patches
        async for _, event_type in w.alive(relay.subscribe("update")):
            c("event_type", {"event_type": event_type})
            w.patch(
                chat_view(
                    signals.user_id,
                    signals.username,
                    signals.color,
                    messages=db.get_messages(),
                    users=db.get_users(),
                )
            )

        # Cleanup on disconnect
        c("User disconnected", {"user_id": signals.user_id})
        db.remove_user(signals.user_id)
        relay.publish("update", "presence")

    return handler
