from stariodemo.PiccoloPkg.MessageDbModule import MessageDb
from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def InitPiccoloDb() -> None:
    await UserDb.create_table(if_not_exists=True)
    await MessageDb.create_table(if_not_exists=True)
