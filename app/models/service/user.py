from pydantic import BaseModel
from app.models.data.users import UserModel


__all__ = ("UserLoginResponse",)


class UserLoginResponse(BaseModel):
    found: bool
    logged_in: bool
    user: UserModel|None = None
    jwt: str|None = None
