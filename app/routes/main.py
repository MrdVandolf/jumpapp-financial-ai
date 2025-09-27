from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.constants import DEFAULT_JWT_COOKIE
from app.models.service.user import UserValidateJWTResponse


__all__ = ("MainRouter",)

from app.repository.chats import ChatsRepository

MainRouter = APIRouter(tags=["main"])


@MainRouter.get(
    '/',
    status_code=200,
)
async def main(request: Request):
    app_container = request.app.container
    templates = app_container.templates()
    user = request.app.user
    chat_repository = app_container.repository_container.chats()

    chats = await chat_repository.find_by_user(user.id)
    print(chats)
    context = {
        "request": request,
        "chats": chats,
    }
    return templates.TemplateResponse("pages/chat.html", context=context)
