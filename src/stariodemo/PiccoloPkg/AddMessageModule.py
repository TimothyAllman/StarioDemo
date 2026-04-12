from stariodemo.PiccoloPkg.MessageDbModule import MessageDb
from stariodemo.PiccoloPkg.MessageDbModule import MessageDto


async def AddMessage(msg: MessageDto) -> None:
    trsc = MessageDb.insert(
        MessageDb(
            **msg.model_dump(),
        )
    )
    result = await trsc.run()

    # keep only the last 100 messages
    newest_rows_qry = (
        MessageDb.select()
        .order_by(
            MessageDb.timestamp,
            ascending=False,
        )
        .limit(100)
    )
    newest_rows = await newest_rows_qry.run()

    keep_ids = [MessageDto(**row).id for row in newest_rows]

    if keep_ids:
        deleteQry = MessageDb.delete().where(
            MessageDb.id.not_in(keep_ids),
        )
        result = await deleteQry.run()
