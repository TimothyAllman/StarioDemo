from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def UserExists(user_id: str) -> bool:
    qry = (
        UserDb.select(
            UserDb.id,
        )
        .where(
            UserDb.id == user_id,
        )
        .first()
    )

    result = await qry.run()

    return result is not None
