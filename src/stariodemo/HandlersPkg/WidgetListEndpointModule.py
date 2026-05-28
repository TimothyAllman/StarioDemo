from stario import Context
from stario import Writer
from stario import responses

from stariodemo.PiccoloPkg.GetWidgetsModule import GetWidgets


def WidgetListEndpoint():
    async def handler(c: Context, w: Writer) -> None:

        dtos = await GetWidgets()

        print(dtos)

        responses.empty(w, 204)

    return handler
