from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageDbModule import ChatAppMessageDto


async def AddMessage(msg: ChatAppMessageDto) -> None:
    trsc = ChatAppMessageDb.insert(
        ChatAppMessageDb(
            **msg.model_dump(),
        )
    )
    result = await trsc.run()

    # keep only the last 100 messages
    newest_rows_qry = (
        ChatAppMessageDb.select()
        .order_by(
            ChatAppMessageDb.timestamp,
            ascending=False,
        )
        .limit(100)
    )
    newest_rows = await newest_rows_qry.run()

    keep_ids = [ChatAppMessageDto(**row).id for row in newest_rows]

    if keep_ids:
        deleteQry = ChatAppMessageDb.delete().where(
            ChatAppMessageDb.id.not_in(keep_ids),
        )
        result = await deleteQry.run()
