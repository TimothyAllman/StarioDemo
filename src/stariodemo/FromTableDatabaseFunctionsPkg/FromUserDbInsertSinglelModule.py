from stariodemo.DatabasePiccoloTablesPkg.UserDbModule import UserDb
from stariodemo.DatabasePiccoloTablesPkg.UserDbModule import UserListDto


async def FromUsersSelectAll() -> list[UserListDto] | None:
    qry = UserDb.select()

    rows = await qry.run()

    dtos = [UserListDto(**x) for x in rows]

    return dtos
