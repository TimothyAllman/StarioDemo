from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto


async def GetChatAppUsers() -> dict[str, ChatAppUserDto]:
    qry = ChatAppUserDb.select()

    result = await qry.run()

    dtos = [ChatAppUserDto(**row) for row in result]

    dtosDict = {item.id: item for item in dtos}

    return dtosDict
