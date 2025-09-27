import hashlib
import hmac

from fastapi import APIRouter, Request, Response
from app.models.routes.auth import AuthRequest, AuthResponse
from app.models.service.user import UserLoginResponse


__all__ = ("AuthRouter",)


AuthRouter = APIRouter(tags=["auth"], prefix="/auth")


@AuthRouter.post(
    '/',
    status_code=200,
    response_model=AuthResponse,
)
async def main(body: AuthRequest, request: Request, response: Response):
    app_container = request.app.container
    user_service = app_container.service_container.user_service()

    login_attempt: UserLoginResponse = await user_service.login_user(email=body.email, password=body.password)
    if not login_attempt.found:
        response.status_code = 404
        return {"success": False, "message": "No user is registered under this email"}

    if not login_attempt.logged_in:
        response.status_code = 401
        return {"success": False, "message": "Wrong email or password"}

    return {"success": True, "message": "", "jwt": login_attempt.jwt}
