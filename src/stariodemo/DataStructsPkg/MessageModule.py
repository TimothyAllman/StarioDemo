from dataclasses import dataclass


@dataclass
class Message:
    """A chat message with sender info and timestamp."""

    id: str
    user_id: str
    username: str
    color: str
    text: str
    timestamp: float