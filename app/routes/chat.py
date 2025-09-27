import logging
from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse


__all__ = ("ChatRouter",)


ChatRouter = APIRouter(tags=["chat"], prefix="/chat")


@ChatRouter.get(
    '/{chat_id}',
    status_code=200,
)
async def main(chat_id: int, request: Request, response: Response):
    app_container = request.app.container
    templates = app_container.templates()
    chat_repository = app_container.repository_container.chats()

    user = request.app.user
    chats = await chat_repository.find_by_user(user.id)
    chat = list(filter(lambda x: x.id == chat_id, chats))

    context = {
        "request": request,
        "chats": chats,
        "current_chat": [],
    }

    if not chat:
        logging.warning(f"No chat found: {chat_id=} for user {user.id} | {user.email}")
        return RedirectResponse(url="/")
    else:
        context["current_chat"] = await chat_repository.read_chat_by_id(chat_id)

    response.set_cookie(
        key="chat_id",
        value=str(chat_id),
        httponly=True,
        samesite="strict",
        secure=False,
    )
    return templates.TemplateResponse("pages/chat.html", context=context)
