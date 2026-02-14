import uuid

from stario import Context
from stario import Writer

from stariodemo.DataStructsPkg.GenerateColorModule import generate_color
from stariodemo.DataStructsPkg.GenerateUserNameModule import generate_username
from stariodemo.ViewsPkg.ChatViewModule import chat_view


def HomeEndpoint(noDeps: None):
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve the initial chat page.

        Each visitor gets a fresh identity (user_id, username, color).
        The identity is stored in Datastar signals on the client side,
        and sent with every subsequent request.
        """
        user_id = str(uuid.uuid4())[:8]
        username = generate_username()
        color = generate_color()

        # Pass empty collections - user will get real data after subscribing
        w.html(chat_view(user_id, username, color, messages=[], users={}))

    return handler
