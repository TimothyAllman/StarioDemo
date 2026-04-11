from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def GetUsers() -> dict[str, User]:
    qry = UserDb.select(
        UserDb.id,
        UserDb.username,
        UserDb.color,
        UserDb.typing,
    )

    result = await qry.run()

    dtos = {
        row["id"]: User(
            id=row["id"],
            username=row["username"],
            color=row["color"],
            typing=bool(row["typing"]),
        )
        for row in result
    }

    return dtos
