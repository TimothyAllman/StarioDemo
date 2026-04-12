from stariodemo.PiccoloPkg.UserDbModule import UserDb
from stariodemo.PiccoloPkg.UserDbModule import UserDto


async def GetUser(user_id: str) -> UserDto | None:
    qry = (
        UserDb.select()
        .where(
            UserDb.id == user_id,
        )
        .first()
    )

    row = await qry.run()

    if row is None:
        return None

    return UserDto(**row)
