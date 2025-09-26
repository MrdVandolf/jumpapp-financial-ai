from fastapi import APIRouter, Request, Response
from app.routes.models.auth import AuthRequest, AuthResponse


__all__ = ("AuthRouter",)


AuthRouter = APIRouter(tags=["auth"], prefix="/auth")


@AuthRouter.post(
    '/',
    status_code=200,
    response_model=AuthResponse,
)
async def main(body: AuthRequest, request: Request, response: Response):
    if body.email != "dasipos@gmail.com":
        response.status_code = 404
        return {"success": False, "message": "No user is registered under this email"}
    elif body.password != "123":
        response.status_code = 401
        return {"success": False, "message": "Wrong email or password"}
    return {"success": True, "message": ""}
