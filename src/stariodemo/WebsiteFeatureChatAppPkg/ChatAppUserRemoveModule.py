from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDb


async def RemoveUser(user_id: str) -> None:
    qry = ChatAppUserDb.delete().where(
        ChatAppUserDb.id == user_id,
    )

    result = await qry.run()

    return None
