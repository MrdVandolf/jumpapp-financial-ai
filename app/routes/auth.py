from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse
from app.models.routes.auth import AuthRequest, AuthResponse
from app.models.service.user import UserLoginResponse
from app.constants import DEFAULT_JWT_COOKIE, DEFAULT_JWT_LIFETIME


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

    response.set_cookie(
        key=DEFAULT_JWT_COOKIE,
        value=login_attempt.jwt,
        httponly=True,
        max_age=DEFAULT_JWT_LIFETIME,
        samesite="strict",
        secure=False,
    )
    return {"success": True, "message": ""}


@AuthRouter.get(
    '/google/in',
    status_code=200,
)
async def google_in(request: Request):
    google_service = request.app.container.service_container.google_service()
    return await google_service.authorize(request)


@AuthRouter.get(
    '/google/callback',
    status_code=200,
)
async def google_callback(request: Request, response: Response):
    app_container = request.app.container
    google_service = app_container.service_container.google_service()
    user_service = app_container.service_container.user_service()
    id_info = await google_service.authorize_access_token(request)

    sub = id_info.get("sub")
    email = id_info.get("email")
    name = id_info.get("name")

    login_attempt: UserLoginResponse = await user_service.login_user(email=email, by_google=True, google_id=sub)
    if not login_attempt.found:
        response.status_code = 404
        return {"success": False, "message": "No user is registered under this email"}

    response = RedirectResponse(url="/login")
    response.set_cookie(
        key=DEFAULT_JWT_COOKIE,
        value=login_attempt.jwt,
        httponly=True,
        max_age=DEFAULT_JWT_LIFETIME,
        samesite="lax",
        secure=False,
    )
    return response
