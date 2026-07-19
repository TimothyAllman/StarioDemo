from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto


async def GetWidget(user_id: str) -> ChatAppUserDto | None:
    qry = (
        ChatAppUserDb.select()
        .where(
            ChatAppUserDb.id == user_id,
        )
        .first()
    )

    row = await qry.run()

    if row is None:
        return None

    return ChatAppUserDto(**row)
