from piccolo.columns import Boolean
from piccolo.columns import Date
from piccolo.columns import Integer
from piccolo.columns import Text
from piccolo.columns import Varchar
from piccolo.table import Table
from pydantic import BaseModel


class WidgetDb(Table):
    # id = Varchar(length=64, primary_key=True)
    title = Varchar(length=200, null=False)
    description = Text(null=True)
    is_completed = Boolean(default=False)
    due_date = Date(null=True)
    priority = Integer(default=1)
    category = Varchar(length=100, default="General")
    created_at = Date()
    modified_at = Date()

    class Meta:
        tablename = "widgets"


class WidgetDto(BaseModel):
    """
    A connected user with their display info and typing state.
    """

    id: int
    title: str
    description: str
    is_completed: bool
    priority: int
    category: str
