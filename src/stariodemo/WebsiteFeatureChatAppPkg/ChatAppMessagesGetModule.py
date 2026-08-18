from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDto


async def GetMessages(limit: int = 100) -> list[ChatAppMessageDto]:
    qry = (
        ChatAppMessageDb.select()
        .order_by(
            ChatAppMessageDb.timestamp,
            ascending=True,
        )
        .limit(limit)
    )

    result = await qry.run()

    dtos = [ChatAppMessageDto(**item) for item in result]

    return dtos
