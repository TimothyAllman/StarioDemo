from stariodemo.FromTableDatabaseFunctionsPkg.WidgetDbModule import WidgetDb
from stariodemo.FromTableDatabaseFunctionsPkg.WidgetDbModule import WidgetDto


async def GetWidgets() -> list[WidgetDto]:
    qry = WidgetDb.select()

    result = await qry.run()

    dtos = [WidgetDto(**item) for item in result]

    return dtos
