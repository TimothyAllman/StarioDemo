from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDb
from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDto


async def AddWidget(widget: WidgetDto) -> None:
    trsc = WidgetDb.insert(
        WidgetDb(
            **widget.model_dump(),
        )
    )
    result = await trsc.run()
