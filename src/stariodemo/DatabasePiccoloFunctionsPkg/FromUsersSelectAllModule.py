from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto


async def FromUsersSelectAll() -> ChatAppUserDto | None:
    qry = (
        ChatAppUserDb.select()
    )

    row = await qry.run()

    return ChatAppUserDto(**row)
