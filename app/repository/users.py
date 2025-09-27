from app.repository.base import BaseRepository
from app.models.data.users import UserModel


__all__ = ("UsersRepository",)


class UsersRepository(BaseRepository):

    async def find_by_email(self, email: str) -> UserModel|None:
        query = "select * from users where email=%(email)s;"
        model = await self.connector.execute(query, {"email": email}, result="fetchone")
        return UserModel(**model) if model else None
