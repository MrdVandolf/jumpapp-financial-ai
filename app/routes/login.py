from fastapi import APIRouter, Request, Response
from app.constants import DEFAULT_JWT_COOKIE


__all__ = ("LoginRouter", "LogoutRouter",)


LoginRouter = APIRouter(tags=["login"], prefix="/login")
LogoutRouter = APIRouter(tags=["logout"], prefix="/logout")


@LoginRouter.get(
    '',
    status_code=200,
)
async def login(request: Request):
    app_container = request.app.container
    templates = app_container.templates()
    return templates.TemplateResponse("pages/login.html", context={"request": request})


@LogoutRouter.post(
    '',
    status_code=200,
)
async def logout(request: Request, response: Response):
    response.delete_cookie(DEFAULT_JWT_COOKIE)
    return {}
