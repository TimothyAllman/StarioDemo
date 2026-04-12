from piccolo.columns import Boolean
from piccolo.columns import Varchar
from piccolo.table import Table
from pydantic import BaseModel


class UserDb(Table):
    id = Varchar(length=64, primary_key=True)
    username = Varchar(length=255)
    color = Varchar(length=64)
    typing = Boolean(default=False)

    class Meta:
        tablename = "users"


class UserDto(BaseModel):
    """A connected user with their display info and typing state."""

    id: str
    username: str
    color: str
    typing: bool = False
