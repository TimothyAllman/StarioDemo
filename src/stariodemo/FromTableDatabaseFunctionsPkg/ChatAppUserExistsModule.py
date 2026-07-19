from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb


async def ChatAppUserExists(user_id: str) -> bool:
    qry = (
        ChatAppUserDb.select(
            ChatAppUserDb.id,
        )
        .where(
            ChatAppUserDb.id == user_id,
        )
        .first()
    )

    result = await qry.run()

    return result is not None
