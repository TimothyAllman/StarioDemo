from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDb
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUserDbModule import ChatAppUserDto


async def SetChatAppUserTyping(user_id: str, typing: bool) -> bool:
    # set up query
    qry = (
        ChatAppUserDb.select()
        .where(
            ChatAppUserDb.id == user_id,
        )
        .first()
    )

    # get result if empty/None nothing to update so return false
    result = await qry.run()
    if result is None:
        return False

    # validate types by instantiating userDto from data. check if the same nothing to update so return false
    dto = ChatAppUserDto(**result)
    if dto.typing == typing:
        return False

    # else update the typing column with the changed status
    qry = ChatAppUserDb.update(
        {ChatAppUserDb.typing: typing},
    ).where(
        ChatAppUserDb.id == user_id,
    )
    result = await qry.run()

    # return true i.e. and update to the db has occurred i.e. a users typing status has been changed
    return True
