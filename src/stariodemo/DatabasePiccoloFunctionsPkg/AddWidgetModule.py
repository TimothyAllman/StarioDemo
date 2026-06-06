from stariodemo.DatabasePiccoloFunctionsPkg.WidgetDbModule import WidgetDb
from stariodemo.DatabasePiccoloFunctionsPkg.WidgetDbModule import WidgetDto


async def AddWidget(widget: WidgetDto) -> None:
    trsc = WidgetDb.insert(
        WidgetDb(
            **widget.model_dump(),
        )
    )
    
    result = await trsc.run()
