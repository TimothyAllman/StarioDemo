from dataclasses import dataclass


@dataclass
class User:
    """A connected user with their display info and typing state."""

    id: str
    username: str
    color: str
    typing: bool = False


# class User(models.Model):
#     """
#     A connected user with their display info and typing state.
#     """

#     id = fields.TextField(pk=True)
#     username = fields.TextField(nullable=False)
#     color = fields.TextField(nullable=False)
#     typing = fields.TextField(nullable=False)
