from stario import Context
from stario import Relay
from stario import Writer
from stario import responses
from stario.datastar import SSE

from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.FromTableDatabaseFunctionsPkg import PiccoloChatDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppRelaysModule import CHAT_PRESENCE
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppRelaysModule import CHAT_SUBSCRIBE_PATTERN
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_PAGE_URL
from stariodemo.WebsiteFeatureChatAppPkg.ChatHtmlModule import chat_view
from stariodemo.WebsiteFeatureChatAppPkg.ChatSignalsModule import read_chat_signal


def SubscribeEndpoint(db: PiccoloChatDb, relay: Relay[str]):
    async def handler(c: Context, w: Writer) -> None:
        """GET /rooms/{room_id}/subscribe — SSE patches for this room.

        `c.alive` ends the loop on client disconnect or server shutdown, so the
        presence cleanup below always runs. If the room is deleted mid-stream we
        navigate the client back to the lobby over SSE.
        """
        # redirect if no room exists/if room gets deleted
        # room = room_from_route(c, db)
        # if room is None:
        #     responses.redirect(w, LOBBY.href())
        #     return

        # redirect if no user exists/if user gets deleted
        signals = await read_chat_signal(c)
        if not signals.user_id:
            responses.redirect(w, CHAT_PAGE_URL.href())
            return

        # Add user to database
        user = ChatAppUserDto(
            id=signals.user_id,
            username=signals.username,
            color=signals.color,
        )
        await db.add_user(user)
        c.span.event(
            "Widget connected",
            {"user_id": signals.user_id, "username": signals.username},
        )

        # Subscribe first so this connection's queue exists before we publish
        # presence (avoids a gap where join could be dropped for this client).
        async with relay.subscribe(CHAT_SUBSCRIBE_PATTERN) as live:
            # async with relay.subscribe(subjects.room_events(room.id)) as live:
            sse = SSE(w)
            # Fan-out: every SSE client subscribed to ``chat.*`` wakes and patches.
            relay.publish(CHAT_PRESENCE, "join")

            # First patch: stream has started; ship current db truth (messages, roster).
            sse.patch_elements(
                chat_view(
                    signals.user_id,
                    signals.username,
                    signals.color,
                    messages=await db.get_messages(),
                    users=await db.get_users(),
                ),
            )

            async for subject, _ in c.alive(live):
                c.span.event("relay", {"subject": subject})
                sse.patch_elements(
                    chat_view(
                        signals.user_id,
                        signals.username,
                        signals.color,
                        messages=await db.get_messages(),
                        users=await db.get_users(),
                    ),
                )

            # Disconnect cleanup — not an error path.
            await db.remove_user(signals.user_id)
            relay.publish(CHAT_PRESENCE, "leave")
            c.span.event("Widget disconnected", {"user_id": signals.user_id})

    return handler
