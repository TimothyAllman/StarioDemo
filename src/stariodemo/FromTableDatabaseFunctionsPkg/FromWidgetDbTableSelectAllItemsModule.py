from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetDb
from stariodemo.DatabasePiccoloTablesPkg.WidgetDbModule import WidgetListDto


async def FromWidgetDbTableSelectAllItems(
    name_filter: str | None = None,
    status_filter: str | None = None,
) -> list[WidgetListDto]:

    qry = WidgetDb.select()

    if name_filter:
        qry = qry.where(
            WidgetDb.name.like(f"%{name_filter}%"),
        )

    if status_filter:
        qry = qry.where(
            WidgetDb.name.like(f"%{status_filter}%"),
        )

    rows = await qry.run()

    dtos = [
        WidgetListDto(
            **x,
        )
        for x in rows
    ]

    return dtos
