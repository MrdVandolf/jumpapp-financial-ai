from app.repository.base import BaseRepository
from app.models.data.chats import ChatModel
from app.models.data.messages import MessageModel


__all__ = ("ChatsRepository",)


class ChatsRepository(BaseRepository):

    async def create(self, user_id: int, name: str) -> ChatModel:
        query = "insert into chats(user_id, name) values (%(user_id)s, %(name)s) returning *;"
        model = await self.connector.execute(query, {"user_id": user_id, "name": name}, result="fetchone")
        return ChatModel(**model)

    async def write_user_message(self, chat_id: int, content: str) -> None:
        query = "insert into messages(chat_id, sender, content) values (%(chat_id)s, %(sender)s, %(content)s);"
        await self.connector.execute(query, {"chat_id": chat_id, "content": content, "sender": "user"})

    async def write_ai_message(self, chat_id: int, content: str) -> None:
        query = "insert into messages(chat_id, sender, content) values (%(chat_id)s, %(sender)s, %(content)s);"
        await self.connector.execute(query, {"chat_id": chat_id, "content": content, "sender": "ai"})

    async def find_by_user(self, user_id: int) -> list[ChatModel]:
        query = "select * from chats where user_id=%(user_id)s;"
        models = await self.connector.execute(query, {"user_id": user_id}, result="fetchall")
        return [ChatModel(**model) for model in models]

    async def find_by_id_and_user(self, user_id: int, chat_id: int) -> ChatModel:
        query = "select * from chats where user_id=%(user_id)s and id=%(chat_id)s;"
        model = await self.connector.execute(query, {"user_id": user_id, "chat_id": chat_id}, result="fetchone")
        return ChatModel(**model)

    async def read_chat_by_id(self, chat_id: int) -> list[MessageModel]:
        query = "select * from messages where chat_id=%(chat_id)s order by id asc;"
        models = await self.connector.execute(query, {"chat_id": chat_id}, result="fetchall")
        return [MessageModel(**model) for model in models]
