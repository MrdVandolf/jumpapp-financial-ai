from pydantic import BaseModel


__all__ = ("UserModel",)


class UserModel(BaseModel):
    id: int
    email: str
    google_id: str|None = None
    hash: str|None = ""
    salt: str|None = ""
    hubspot: str|None = None
