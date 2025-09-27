from app.repository.base import BaseRepository
from app.models.data.chats import ChatModel


__all__ = ("ChatsRepository",)


class ChatsRepository(BaseRepository):

    async def find_by_user(self, user_id: int) -> list[ChatModel]:
        query = "select * from chats where user_id=%(user_id)s;"
        models = await self.connector.execute(query, {"user_id": user_id}, result="fetchall")
        return [ChatModel(**model) for model in models]
