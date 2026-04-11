from stariodemo.DataStructsPkg.MessageModule import Message
from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.PiccoloPkg.AddMessageModule import AddMessage
from stariodemo.PiccoloPkg.AddUserModule import AddUser
from stariodemo.PiccoloPkg.GetMessagesModule import GetMessages
from stariodemo.PiccoloPkg.GetUserModule import GetUser
from stariodemo.PiccoloPkg.GetUsersModule import GetUsers
from stariodemo.PiccoloPkg.RemoveUserModule import RemoveUser
from stariodemo.PiccoloPkg.SetUserTypingModule import SetUserTyping
from stariodemo.PiccoloPkg.UserExistsModule import UserExists


class PiccoloChatDb:
    async def add_user(self, user: User) -> None:
        await AddUser(user)

    async def add_message(self, msg: Message) -> None:
        await AddMessage(msg)

    async def get_messages(self, limit: int = 100) -> list[Message]:
        return await GetMessages(limit)

    async def remove_user(self, user_id: str) -> None:
        await RemoveUser(user_id)

    async def get_user(self, user_id: str) -> User | None:
        return await GetUser(user_id)

    async def get_users(self) -> dict[str, User]:
        return await GetUsers()

    async def user_exists(self, user_id: str) -> bool:
        return await UserExists(user_id)

    async def set_user_typing(self, user_id: str, typing: bool) -> bool:
        return await SetUserTyping(user_id, typing)
