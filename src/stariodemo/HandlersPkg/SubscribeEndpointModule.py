from stario import Context
from stario import Relay
from stario import Writer

from stariodemo.DataStructsPkg.UrlsModule import CHAT_PAGE_URL
from stariodemo.HandlersPkg import ChatSignals
from stariodemo.HtmlViewsPkg.ChatViewModule import chat_view
from stariodemo.PiccoloPkg import PiccoloChatDb
from stariodemo.PiccoloPkg.UserDbModule import UserDto


def SubscribeEndpoint(db: PiccoloChatDb, relay: Relay[str]):
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
            w.redirect(CHAT_PAGE_URL)
            return

        # Add user to database
        user = UserDto(
            id=signals.user_id,
            username=signals.username,
            color=signals.color,
        )

        await db.add_user(user)
        c(
            "User connected",
            {"user_id": signals.user_id, "username": signals.username},
        )

        # Tell everyone that someone joined
        relay.publish("update", "presence")

        # Send current state immediately
        w.patch(
            chat_view(
                signals.user_id,
                signals.username,
                signals.color,
                messages=await db.get_messages(),
                users=await db.get_users(),
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
                    messages=await db.get_messages(),
                    users=await db.get_users(),
                )
            )

        # Cleanup on disconnect
        c(
            "User disconnected",
            {"user_id": signals.user_id},
        )

        await db.remove_user(signals.user_id)
        relay.publish("update", "presence")

    return handler
