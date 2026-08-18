from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDb


async def FromWidgetDbTableDeleteSingleItem(
    id,
) -> bool:

    qry = (
        WidgetDb.select()
        .where(
            WidgetDb.id == id,
        )
        .first()
    )
    row = await qry.run()

    if row is None:
        return False

    instr = WidgetDb.delete().where(
        WidgetDb.id == id,
    )
    await instr.run()

    return True
