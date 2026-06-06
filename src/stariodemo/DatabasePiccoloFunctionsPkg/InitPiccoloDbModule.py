from stariodemo.DatabasePiccoloFunctionsPkg.WidgetDbModule import WidgetDb
from stariodemo.DatabasePiccoloTablesPkg.ChatAppMessageDbModule import ChatAppMessageDb
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb


async def InitPiccoloDb() -> None:
    await ChatAppUserDb.create_table(if_not_exists=True)
    await ChatAppMessageDb.create_table(if_not_exists=True)
    await WidgetDb.create_table(if_not_exists=True)
