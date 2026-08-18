from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDb


async def FromWidgetDbTableInsertSingleItem(
    name: str,
    age: int,
    id: str,  # or uuid.UUID depending on your column type
):
    # 1. Instantiate the row object with the correct variables
    row = WidgetDb(
        id=id,
        name=name,
        age=age,
    )

    # 2. Run the insert with the targeted conflict resolution structure
    trsc = WidgetDb.insert(
        row,
    ).on_conflict(
        target=WidgetDb.id,
        action="DO UPDATE",
        values=[
            WidgetDb.name,
            WidgetDb.age,
        ],
    )

    result = await trsc.run()
    return result
