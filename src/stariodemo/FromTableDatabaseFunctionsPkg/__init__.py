from stariodemo.DatabasePiccoloTablesPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppMessagesAddModule import AddMessage
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppMessagesGetModule import GetMessages
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUserAddModule import ChatAppUserAdd
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUserExistsModule import ChatAppUserExists
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUserGetModule import GetChatAppUser
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUserRemoveModule import RemoveUser
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUsersGetModule import GetChatAppUsers
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUserTypingSetModule import SetChatAppUserTyping


class PiccoloChatDb:
    async def add_user(
        self,
        user: ChatAppUserDto,
    ) -> None:
        await ChatAppUserAdd(user)

    async def add_message(
        self,
        msg: ChatAppMessageDto,
    ) -> None:
        await AddMessage(msg)

    async def get_messages(
        self,
        limit: int = 100,
    ) -> list[ChatAppMessageDto]:
        return await GetMessages(limit)

    async def remove_user(
        self,
        user_id: str,
    ) -> None:
        await RemoveUser(user_id)

    async def get_user(
        self,
        user_id: str,
    ) -> ChatAppUserDto | None:
        return await GetChatAppUser(user_id)

    async def get_users(
        self,
    ) -> dict[str, ChatAppUserDto]:
        return await GetChatAppUsers()

    async def user_exists(
        self,
        user_id: str,
    ) -> bool:
        return await ChatAppUserExists(user_id)

    async def set_user_typing(
        self,
        user_id: str,
        typing: bool,
    ) -> bool:
        return await SetChatAppUserTyping(user_id, typing)
