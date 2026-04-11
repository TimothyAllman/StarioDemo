from stariodemo.DataStructsPkg.MessageModule import MessageDto
from stariodemo.PiccoloPkg.MessageDbModule import MessageDb


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

    dtos = [
        MessageDto(
            id=row["id"],
            user_id=row["user_id"],
            username=row["username"],
            color=row["color"],
            text=row["text"],
            timestamp=row["timestamp"],
        )
        for row in result
    ]

    return dtos
