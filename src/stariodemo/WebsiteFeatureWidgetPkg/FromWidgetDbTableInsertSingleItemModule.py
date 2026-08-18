from stariodemo.WebsiteFeatureWidgetPkg.DbWidgetModule import WidgetDb
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WidgetAddSignals


async def FromWidgetDbTableInsertSingleItem(widgetAddSignal: WidgetAddSignals):
    trsc = WidgetDb.insert(
        WidgetDb(
            **widgetAddSignal.model_dump(),
        )
    ).on_conflict(
        target=WidgetDb.id,
        action="DO UPDATE",
        values=[
            WidgetDb.name,
            WidgetDb.age,
        ],
    )

    result = await trsc.run()
