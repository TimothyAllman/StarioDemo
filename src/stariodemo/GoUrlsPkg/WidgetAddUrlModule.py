from pydantic import BaseModel
from stario import Context
from stario import UrlPath

WIDGET_ADD_URL = UrlPath("/widget-add")


class WidgetAddSignals(BaseModel):
    """
    docstring
    """

    name: str
    age: int


async def ReadWidgetAddSignals(
    c: Context,
) -> WidgetAddSignals:
    """
    docstring
    """

    parsedName = c.route.params.get("name", "").strip()
    parseAge = c.route.params.get("age", "").strip()

    signals = WidgetAddSignals(
        name=parsedName,
        age=int(parseAge),
    )

    return signals
