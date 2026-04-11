from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def SetUserTyping(user_id: str, typing: bool) -> bool:
    qry = (
        UserDb.select()
        .where(
            UserDb.id == user_id,
        )
        .first()
    )

    row = await qry.run()

    if row is None:
        return False

    typing = bool(typing)

    if bool(row["typing"]) == typing:
        return False

    row["typing"] = typing

    qry = UserDb.update(
        {UserDb.typing: typing},
    ).where(
        UserDb.id == user_id,
    )
    result = await qry.run()

    return True
