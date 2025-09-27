from pydantic import BaseModel, EmailStr


__all__ = ("AuthRequest", "AuthResponse",)


class AuthRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    success: bool
    message: str
