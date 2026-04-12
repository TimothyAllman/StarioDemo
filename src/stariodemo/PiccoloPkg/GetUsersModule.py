from stariodemo.PiccoloPkg.UserDbModule import UserDb
from stariodemo.PiccoloPkg.UserDbModule import UserDto


async def GetUsers() -> dict[str, UserDto]:
    qry = UserDb.select()

    result = await qry.run()

    dtos = [UserDto(**row) for row in result]

    dtosDict = {item.id: item for item in dtos}

    return dtosDict
