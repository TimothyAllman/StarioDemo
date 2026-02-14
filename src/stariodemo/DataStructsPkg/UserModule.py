
from dataclasses import dataclass


@dataclass
class User:
    """A connected user with their display info and typing state."""

    id: str
    username: str
    color: str
    typing: bool = False