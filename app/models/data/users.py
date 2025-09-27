from pydantic import BaseModel


__all__ = ("UserModel",)


class UserModel(BaseModel):
    id: int
    email: str
    hash: str
    salt: str
    hubspot: str|None = None
