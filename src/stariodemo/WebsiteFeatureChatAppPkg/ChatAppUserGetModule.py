from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDto


async def GetChatAppUser(user_id: str) -> ChatAppUserDto | None:
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
