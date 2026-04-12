from stariodemo.PiccoloPkg.MessageDbModule import MessageDb
from stariodemo.PiccoloPkg.MessageDbModule import MessageDto


async def GetMessages(limit: int = 100) -> list[MessageDto]:
    qry = (
        MessageDb.select(
            MessageDb.id,
            MessageDb.user_id,
            MessageDb.username,
            MessageDb.color,
            MessageDb.text,
            MessageDb.timestamp,
        )
        .order_by(
            MessageDb.timestamp,
            ascending=True,
        )
        .limit(limit)
    )

    result = await qry.run()

    dtos = [MessageDto(**item) for item in result]

    return dtos
