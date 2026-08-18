from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDb
from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetListDto


async def FromWidgetDbTableUpdateSingleItem(
    id,
) -> list[WidgetListDto] | None:

    qry = WidgetDb.update().where(WidgetDb.id == id)

    rows = await qry.run()

    dtos = [WidgetListDto(**x) for x in rows]

    return dtos
