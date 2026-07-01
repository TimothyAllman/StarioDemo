from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto


async def AddUser(user: ChatAppUserDto) -> None:
    trsc = ChatAppUserDb.insert(
        ChatAppUserDb(
            **user.model_dump(),
        )
    ).on_conflict(
        target=ChatAppUserDb.id,
        action="DO UPDATE",
        values=[
            ChatAppUserDb.username,
            ChatAppUserDb.color,
            ChatAppUserDb.typing,
        ],
    )
    result = await trsc.run()
