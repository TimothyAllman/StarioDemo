from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDb
from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDetailsDto


async def FromWidgetDbTableSelectSingleItem(
    id: str,
) -> WidgetDetailsDto | None:
    """
    Selects a single widget by its primary key ID
    and returns it mapped as a verified DTO.
    """
    # 1. Query the database selecting all fields filtered by ID
    qry = WidgetDb.select().where(
        WidgetDb.id == id,
    )

    rows = await qry.run()

    # 2. Return None gracefully if no matching record was found
    if not rows:
        return None

    # 3. Extract the first matching row dictionary and unpack it into the DTO
    first_row = rows[0]
    dto = WidgetDetailsDto(
        **first_row,
    )

    return dto
