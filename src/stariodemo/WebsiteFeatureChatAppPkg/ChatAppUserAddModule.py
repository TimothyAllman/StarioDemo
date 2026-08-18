from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDto


async def ChatAppUserAdd(user: ChatAppUserDto) -> None:
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
