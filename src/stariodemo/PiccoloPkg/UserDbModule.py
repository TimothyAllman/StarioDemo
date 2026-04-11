from piccolo.columns import Boolean
from piccolo.columns import Varchar
from piccolo.table import Table


class UserDb(Table):
    id = Varchar(length=64, primary_key=True)
    username = Varchar(length=255)
    color = Varchar(length=64)
    typing = Boolean(default=False)

    class Meta:
        tablename = "users"
