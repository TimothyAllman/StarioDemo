from pydantic import BaseModel
from stario import UrlPath

WIDGET_LIST_PAGE_URL = UrlPath("/widget-list")
WIDGET_LIST_API_URL = UrlPath("/widget-list-api")
WIDGET_ADD_PAGE_URL = UrlPath("/widget-add")
WIDGET_ADD_API_URL = UrlPath("/widget-add-api")
WIDGET_EDIT_PAGE_URL = UrlPath("/widget-edit")
WIDGET_DETAILS_PAGE_URL = UrlPath("/widget-details")


class WidgetAddSignals(BaseModel):
    """
    docstring
    """

    name: str
    age: int
