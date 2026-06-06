from piccolo.columns import Float
from piccolo.columns import Text
from piccolo.columns import Varchar
from piccolo.table import Table
from pydantic import BaseModel


class ChatAppMessageDb(Table):
    id = Varchar(length=64, primary_key=True)
    user_id = Varchar(length=64)
    username = Varchar(length=255)
    color = Varchar(length=64)
    text = Text()
    timestamp = Float()

    # class Meta:
    #     tablename = "messages"


class ChatAppMessageDto(BaseModel):
    """
    A chat message with sender info and timestamp.
    """

    id: str
    user_id: str
    username: str
    color: str
    text: str
    timestamp: float
