from app.repository.base import BaseRepository
from app.models.data.chats import ChatModel
from app.models.data.messages import MessageModel


__all__ = ("ChatsRepository",)


class ChatsRepository(BaseRepository):

    async def find_by_user(self, user_id: int) -> list[ChatModel]:
        query = "select * from chats where user_id=%(user_id)s;"
        models = await self.connector.execute(query, {"user_id": user_id}, result="fetchall")
        return [ChatModel(**model) for model in models]

    async def read_chat_by_id(self, chat_id: int) -> list[MessageModel]:
        query = "select * from messages where chat_id=%(chat_id)s order by id asc;"
        models = await self.connector.execute(query, {"chat_id": chat_id}, result="fetchall")
        return [MessageModel(**model) for model in models]
