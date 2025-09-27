from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.constants import DEFAULT_JWT_COOKIE
from app.models.service.user import UserValidateJWTResponse


__all__ = ("MainRouter",)


MainRouter = APIRouter(tags=["main"])


@MainRouter.get(
    '/',
    status_code=200,
)
async def main(request: Request):
    app_container = request.app.container
    templates = app_container.templates()
    user_service = app_container.service_container.user_service()

    cookies = request.cookies
    if not cookies.get(DEFAULT_JWT_COOKIE):
        return RedirectResponse(url="/login")

    jwt = cookies[DEFAULT_JWT_COOKIE]
    data: UserValidateJWTResponse = await user_service.validate_user_jwt(jwt)
    if not data.success:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse("pages/main.html", context={"request": request})
