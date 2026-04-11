from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def GetUser(user_id: str) -> User | None:
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

    return User(
        id=row["id"],
        username=row["username"],
        color=row["color"],
        typing=row["typing"],
    )
