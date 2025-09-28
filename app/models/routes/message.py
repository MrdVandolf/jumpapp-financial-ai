from pydantic import BaseModel, EmailStr


__all__ = ("MessageSendRequest", "MessageSendResponse",)


class MessageSendRequest(BaseModel):
    content: str


class MessageSendResponse(BaseModel):
    success: bool = False
    redirect_to: str|None = None
    message: str|None = None
