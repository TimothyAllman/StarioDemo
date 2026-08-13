from dataclasses import dataclass

from stario import Context
from stario import datastar


@dataclass
class ChatSignals:
    """
    Schema for signals sent from client.

    Datastar automatically sends signals with every request (@get, @post).
    Using a dataclass lets us parse and validate them with c.signals(ChatSignals).
    """

    user_id: str = ""
    username: str = ""
    color: str = ""
    message: str = ""


async def read_chat_signal(c: Context) -> ChatSignals:

    payload = await datastar.read_signals(
        c.req,
    )

    result = ChatSignals(
        user_id=str(payload.get("user_id", "")),
        username=str(payload.get("username", "")),
        color=str(payload.get("color", "")),
        message=str(payload.get("message", "")),
    )

    return result
