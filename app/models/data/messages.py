from pydantic import BaseModel


__all__ = ("MessageModel",)


class MessageModel(BaseModel):
    id: int
    chat_id: int
    sender: str
    content: str
