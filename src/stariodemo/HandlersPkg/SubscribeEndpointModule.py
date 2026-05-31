from stario import Context
from stario import Relay
from stario import Writer
from stario import datastar
from stario import responses

from stariodemo.DataStructsPkg.RelayTopicsModule import CHAT_PRESENCE
from stariodemo.DataStructsPkg.RelayTopicsModule import CHAT_SUBSCRIBE_PATTERN
from stariodemo.DataStructsPkg.UrlsModule import CHAT_PAGE_URL
from stariodemo.HtmlHtmlsPkg.ChatHtmlModule import chat_view
from stariodemo.PiccoloPkg import PiccoloChatDb
from stariodemo.PiccoloPkg.UserDbModule import UserDto
from stariodemo.SignalsPkg.ChatSignalsModule import read_chat_signal


def SubscribeEndpoint(db: PiccoloChatDb, relay: Relay[str]):
    """``router.get(..., subscribe(db, relay))`` — captures shared deps."""

    async def handler(c: Context, w: Writer) -> None:
        """
        Long-lived SSE handler: **setup**, **while connected**, **cleanup**.

        Same lifecycle as tiles: ``async with relay.subscribe(...)`` first so
        ``publish`` cannot race ahead of this connection's queue, then
        ``async for`` inside ``w.alive(live)``, then teardown before exiting the
        ``async with``.
        """

        signals = await read_chat_signal(c)

        if not signals.user_id:
            responses.redirect(w, CHAT_PAGE_URL)
            return

        # Add user to database
        user = UserDto(
            id=signals.user_id,
            username=signals.username,
            color=signals.color,
        )

        await db.add_user(user)
        c.span.event(
            "User connected",
            {"user_id": signals.user_id, "username": signals.username},
        )

        # Register relay queue before CHAT_PRESENCE publish so this client cannot miss events.
        async with relay.subscribe(CHAT_SUBSCRIBE_PATTERN) as live:
            # Fan-out: every SSE client subscribed to ``chat.*`` wakes and patches.
            relay.publish(CHAT_PRESENCE, "join")

            # First patch: stream has started; ship current db truth (messages, roster).
            datastar.sse.patch_elements(
                w,
                chat_view(
                    signals.user_id,
                    signals.username,
                    signals.color,
                    messages=await db.get_messages(),
                    users=await db.get_users(),
                ),
            )

            async for subject, _ in w.alive(live):
                c.span.event("relay", {"subject": subject})
                datastar.sse.patch_elements(
                    w,
                    chat_view(
                        signals.user_id,
                        signals.username,
                        signals.color,
                        messages=await db.get_messages(),
                        users=await db.get_users(),
                    ),
                )

            # Disconnect cleanup — not an error path.
            c.span.event("User disconnected", {"user_id": signals.user_id})
            await db.remove_user(signals.user_id)
            relay.publish(CHAT_PRESENCE, "leave")

    return handler
