from piccolo.columns import Boolean
from piccolo.columns import Integer
from piccolo.columns import Varchar
from piccolo.table import Table
from pydantic import BaseModel


class UserDb(Table):
    id = Varchar(length=64, primary_key=True)
    username = Varchar(length=255)
    name = Varchar(length=64)
    surname = Varchar(length=64)
    address = Varchar(length=64)
    age = Integer()
    isAdmin = Boolean(default=False)

    # class Meta:
    #     tablename = "users"


class UserListDto(BaseModel):
    """
    A connected user with their display info and typing state.
    """

    id: str
    username: str
    name: str

class UserUpdateDto(BaseModel):
    """
    A connected user with their display info and typing state.
    """

    id: str
    username: str
    name: str