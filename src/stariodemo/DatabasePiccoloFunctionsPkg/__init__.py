from stariodemo.DatabasePiccoloFunctionsPkg.AddMessageModule import AddMessage
from stariodemo.DatabasePiccoloFunctionsPkg.AddUserModule import AddUser
from stariodemo.DatabasePiccoloFunctionsPkg.AddWidgetModule import AddWidget
from stariodemo.DatabasePiccoloFunctionsPkg.GetMessagesModule import GetMessages
from stariodemo.DatabasePiccoloFunctionsPkg.GetUserModule import GetUser
from stariodemo.DatabasePiccoloFunctionsPkg.GetUsersModule import GetUsers
from stariodemo.DatabasePiccoloFunctionsPkg.RemoveUserModule import RemoveUser
from stariodemo.DatabasePiccoloFunctionsPkg.SeedWidgetModule import SeedWidget
from stariodemo.DatabasePiccoloFunctionsPkg.SetUserTypingModule import SetUserTyping
from stariodemo.DatabasePiccoloFunctionsPkg.UserExistsModule import UserExists
from stariodemo.DatabasePiccoloFunctionsPkg.WidgetDbModule import WidgetDto
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
