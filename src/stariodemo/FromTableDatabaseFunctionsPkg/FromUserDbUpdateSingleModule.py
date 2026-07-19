from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetDb
from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetListDto


async def FromWidgetDbUpdateSingle(
    id,
) -> list[WidgetListDto] | None:
    qry = WidgetDb.update().where(WidgetDb.id == id)

    rows = await qry.run()

    dtos = [WidgetListDto(**x) for x in rows]

    return dtos
