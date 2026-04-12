from stariodemo.PiccoloPkg.AddMessageModule import AddMessage
from stariodemo.PiccoloPkg.AddUserModule import AddUser
from stariodemo.PiccoloPkg.AddWidgetModule import AddWidget
from stariodemo.PiccoloPkg.GetMessagesModule import GetMessages
from stariodemo.PiccoloPkg.GetUserModule import GetUser
from stariodemo.PiccoloPkg.GetUsersModule import GetUsers
from stariodemo.PiccoloPkg.MessageDbModule import MessageDto
from stariodemo.PiccoloPkg.RemoveUserModule import RemoveUser
from stariodemo.PiccoloPkg.SeedWidgetModule import SeedWidget
from stariodemo.PiccoloPkg.SetUserTypingModule import SetUserTyping
from stariodemo.PiccoloPkg.UserDbModule import UserDto
from stariodemo.PiccoloPkg.UserExistsModule import UserExists
from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDto


class PiccoloChatDb:
    async def add_user(
        self,
        user: UserDto,
    ) -> None:
        await AddUser(user)

    async def add_message(
        self,
        msg: MessageDto,
    ) -> None:
        await AddMessage(msg)

    async def get_messages(
        self,
        limit: int = 100,
    ) -> list[MessageDto]:
        return await GetMessages(limit)

    async def remove_user(
        self,
        user_id: str,
    ) -> None:
        await RemoveUser(user_id)

    async def get_user(
        self,
        user_id: str,
    ) -> UserDto | None:
        return await GetUser(user_id)

    async def get_users(
        self,
    ) -> dict[str, UserDto]:
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
