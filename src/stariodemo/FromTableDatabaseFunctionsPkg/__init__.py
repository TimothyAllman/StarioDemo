from stariodemo.FromTableDatabaseFunctionsPkg.AddMessageModule import AddMessage
from stariodemo.FromTableDatabaseFunctionsPkg.AddUserModule import AddUser
from stariodemo.FromTableDatabaseFunctionsPkg.AddWidgetModule import AddWidget
from stariodemo.FromTableDatabaseFunctionsPkg.GetMessagesModule import GetMessages
from stariodemo.FromTableDatabaseFunctionsPkg.GetUserModule import GetUser
from stariodemo.FromTableDatabaseFunctionsPkg.GetUsersModule import GetUsers
from stariodemo.FromTableDatabaseFunctionsPkg.RemoveUserModule import RemoveUser
from stariodemo.FromTableDatabaseFunctionsPkg.SeedWidgetModule import SeedWidget
from stariodemo.FromTableDatabaseFunctionsPkg.SetUserTypingModule import SetUserTyping
from stariodemo.FromTableDatabaseFunctionsPkg.UserExistsModule import UserExists
from stariodemo.FromTableDatabaseFunctionsPkg.WidgetDbModule import WidgetDto
from stariodemo.DatabasePiccoloTablesPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto


class PiccoloChatDb:
    async def add_user(
        self,
        user: ChatAppUserDto,
    ) -> None:
        await AddUser(user)

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
        return await GetUser(user_id)

    async def get_users(
        self,
    ) -> dict[str, ChatAppUserDto]:
        return await GetUsers()

    async def user_exists(
        self,
        user_id: str,
    ) -> bool:
        return await UserExists(user_id)

    async def set_user_typing(
        self,
        user_id: str,
        typing: bool,
    ) -> bool:
        return await SetUserTyping(user_id, typing)
