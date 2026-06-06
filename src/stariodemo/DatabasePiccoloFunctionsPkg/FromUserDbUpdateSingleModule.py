from stariodemo.DatabasePiccoloTablesPkg.UserDbModule import UserDb
from stariodemo.DatabasePiccoloTablesPkg.UserDbModule import UserListDto


async def FromUserDbUpdateSingle(id,) -> list[UserListDto] | None:
    qry = UserDb.update(
       
    ).where(
        UserDb.id==id
    )

    rows = await qry.run()

    dtos = [UserListDto(**x) for x in rows]

    return dtos
