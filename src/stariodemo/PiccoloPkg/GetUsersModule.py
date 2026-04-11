from stariodemo.DataStructsPkg.UserModule import UserDto
from stariodemo.PiccoloPkg.UserDbModule import UserDb


async def GetUsers() -> dict[str, UserDto]:
    qry = UserDb.select(
        UserDb.id,
        UserDb.username,
        UserDb.color,
        UserDb.typing,
    )

    result = await qry.run()

    dtos = {
        row["id"]: UserDto(
            id=row["id"],
            username=row["username"],
            color=row["color"],
            typing=bool(row["typing"]),
        )
        for row in result
    }

    return dtos
