from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def RemoveUser(user_id: str) -> None:
    qry = UserDb.delete().where(
        UserDb.id == user_id,
    )

    result = await qry.run()

    return None
