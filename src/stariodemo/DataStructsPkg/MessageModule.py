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


# class Message(models.Model):
#     """
#     A chat message with sender info and timestamp.
#     """

#     id = fields.TextField(pk=True)
#     user_id = fields.TextField(nullable=False)
#     username = fields.TextField(nullable=False)
#     color = fields.TextField(nullable=False)
#     text = fields.TextField(nullable=False)
#     timestamp = fields.FloatField()
