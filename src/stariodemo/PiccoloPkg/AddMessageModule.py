from stariodemo.DataStructsPkg.MessageModule import MessageDto
from stariodemo.PiccoloPkg.MessageDbModule import MessageDb


async def AddMessage(msg: MessageDto) -> None:
    trsc = MessageDb.insert(
        MessageDb(
            id=msg.id,
            user_id=msg.user_id,
            username=msg.username,
            color=msg.color,
            text=msg.text,
            timestamp=msg.timestamp,
        )
    )
    result = await trsc.run()

    # keep only the last 100 messages
    newest_rows_qry = (
        MessageDb.select(
            MessageDb.id,
        )
        .order_by(
            MessageDb.timestamp,
            ascending=False,
        )
        .limit(100)
    )
    newest_rows = await newest_rows_qry.run()

    keep_ids = [row["id"] for row in newest_rows]

    if keep_ids:
        deleteQry = MessageDb.delete().where(
            MessageDb.id.not_in(keep_ids),
        )
        result = await deleteQry.run()
