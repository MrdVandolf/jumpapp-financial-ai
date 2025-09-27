from pydantic import BaseModel


__all__ = ("ChatModel",)


class ChatModel(BaseModel):
    id: int
    user_id: int
    name: str
