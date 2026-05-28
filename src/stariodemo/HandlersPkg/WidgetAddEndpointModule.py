from stario import Context, responses
from stario import Writer

from stariodemo.PiccoloPkg.AddWidgetModule import AddWidget
from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDto


def WidgetAddEndpoint():
    async def handler(c: Context, w: Writer) -> None:

        dto = WidgetDto(
            title="asdas",
            description="asasd",
        )

        print(dto)

        await AddWidget(dto)

        responses.empty(w, 204)

    return handler
