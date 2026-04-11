from stariodemo.DataStructsPkg.UserModule import UserDto
from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def GetUser(user_id: str) -> UserDto | None:
    qry = (
        UserDb.select(
            UserDb.id,
            UserDb.username,
            UserDb.color,
            UserDb.typing,
        )
        .where(UserDb.id == user_id)
        .first()
    )

    row = await qry.run()

    if row is None:
        return None

    return UserDto(
        id=row["id"],
        username=row["username"],
        color=row["color"],
        typing=row["typing"],
    )
