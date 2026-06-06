from stariodemo.DatabasePiccoloFunctionsPkg.WidgetDbModule import WidgetDb
from stariodemo.DatabasePiccoloFunctionsPkg.WidgetDbModule import WidgetDto


async def GetWidgets() -> list[WidgetDto]:
    qry = WidgetDb.select()

    result = await qry.run()

    dtos = [WidgetDto(**item) for item in result]

    return dtos
