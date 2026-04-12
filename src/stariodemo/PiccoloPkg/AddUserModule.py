from stariodemo.PiccoloPkg.UserDbModule import UserDb
from stariodemo.PiccoloPkg.UserDbModule import UserDto


async def AddUser(user: UserDto) -> None:
    trsc = UserDb.insert(
        UserDb(
            **user.model_dump(),
        )
    ).on_conflict(
        target=UserDb.id,
        action="DO UPDATE",
        values=[
            UserDb.username,
            UserDb.color,
            UserDb.typing,
        ],
    )
    result = await trsc.run()
