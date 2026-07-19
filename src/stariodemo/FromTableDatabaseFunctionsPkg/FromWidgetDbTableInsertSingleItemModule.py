from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetDb
from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetListDto


async def FromWidgetDbTableInsertSingleItem() -> list[WidgetListDto] | None:
    qry = WidgetDb.select()

    rows = await qry.run()

    dtos = [WidgetListDto(**x) for x in rows]

    return dtos
