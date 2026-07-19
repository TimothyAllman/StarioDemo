from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb


async def RemoveWidget(user_id: str) -> None:
    qry = ChatAppUserDb.delete().where(
        ChatAppUserDb.id == user_id,
    )

    result = await qry.run()

    return None
