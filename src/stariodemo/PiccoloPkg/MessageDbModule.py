from piccolo.columns import Float
from piccolo.columns import Text
from piccolo.columns import Varchar
from piccolo.table import Table


class MessageDb(Table):
    id = Varchar(length=64, primary_key=True)
    user_id = Varchar(length=64)
    username = Varchar(length=255)
    color = Varchar(length=64)
    text = Text()
    timestamp = Float()

    class Meta:
        tablename = "messages"
