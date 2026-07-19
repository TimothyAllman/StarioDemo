from stariodemo.DatabasePiccoloTablesPkg.ChatAppMessageDbModule import ChatAppMessageDto
from stariodemo.DatabasePiccoloTablesPkg.ChatAppUserDbModule import ChatAppUserDto
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppMessagesAddModule import AddMessage
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppUserAddModule import AddUser
from stariodemo.FromTableDatabaseFunctionsPkg.ChatAppMessagesGetModule import GetMessages
from stariodemo.FromTableDatabaseFunctionsPkg.GetWidgetModule import GetWidget
from stariodemo.FromTableDatabaseFunctionsPkg.GetWidgetsModule import GetChatAppUser
from stariodemo.FromTableDatabaseFunctionsPkg.RemoveWidgetModule import RemoveWidget
from stariodemo.DatabasePiccoloTablesPkg.SeedWidgetModule import SeedWidget
from stariodemo.FromTableDatabaseFunctionsPkg.SetWidgetTypingModule import SetWidgetTyping
from stariodemo.FromTableDatabaseFunctionsPkg.WidgetDbModule import WidgetDto
from stariodemo.FromTableDatabaseFunctionsPkg.WidgetExistsModule import WidgetExists


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
        await RemoveWidget(user_id)

    async def get_user(
        self,
        user_id: str,
    ) -> ChatAppUserDto | None:
        return await GetWidget(user_id)

    async def get_users(
        self,
    ) -> dict[str, ChatAppUserDto]:
        return await GetChatAppUser()

    async def user_exists(
        self,
        user_id: str,
    ) -> bool:
        return await WidgetExists(user_id)

    async def set_user_typing(
        self,
        user_id: str,
        typing: bool,
    ) -> bool:
        return await SetWidgetTyping(user_id, typing)
